import pygame

from search_algorithm import a_star, bfs, dfs, greedy_best_first
from dashboard_data import add_log, record_replanning, search_stats
from metrics import Metrics

from mainn import grid, state, ai_engine, metrics

# =========================
# PATH COMPUTATION
# =========================
def compute_path(current_algo, start, goal):
    if current_algo == "bfs":
        return bfs(start, goal, grid, 10, 11, BLOCKED)
    elif current_algo == "dfs":
        return dfs(start, goal, grid, 10, 11, BLOCKED)
    elif current_algo == "greedy":
        return greedy_best_first(start, goal, grid, 10, 11, BLOCKED)
    else:
        return a_star(start, goal, grid, 10, 11, BLOCKED)

# =========================
# SAFE TARGET CHECK
# =========================
def clear_invalid_target(amb, state):
    if amb.target and (amb.target.rescued or amb.target.dead):
        state.reserved_victims.discard((amb.target.row, amb.target.col))
        amb.target = None
        amb.path = []
        amb.path_index = 0

# =========================
# MAIN UPDATE LOOP
# =========================
def update_ambulances(ambulances, victims, hospitals, current_algo):
    global medical_kits

    for amb_index, amb in enumerate(ambulances):

        clear_invalid_target(amb, state)

        # -------------------------
        # VICTIM ASSIGNMENT
        # -------------------------
        if (
            not amb.going_to_hospital and
            amb.carry < amb.max_capacity and
            amb.target is None
        ):

            best = None
            best_score = float("-inf")

            for v in victims:
                if v.rescued or v.dead or v.removed:
                    continue
                if (v.row, v.col) in state.reserved_victims:
                    continue

                result = ai_engine.evaluate_victim(
                    {
                        "row": v.row,
                        "col": v.col,
                        "severity": v.severity,
                        "health": v.health
                    },
                    tuple(amb.pos)
                )

                metrics.ml_predictions_made += 1

                if result["score"] > best_score:
                    best_score = result["score"]
                    best = v

            if best:
                state.reserved_victims.add((best.row, best.col))
                amb.target = best

                goal = (best.row, best.col)
                amb.path = compute_path(current_algo, tuple(amb.pos), goal)
                amb.path_index = 0

                add_log("TARGET", f"Assigned victim ({best.row},{best.col})", "HIGH", "ACTIVE")

        # -------------------------
        # PATH FINISHED
        # -------------------------
        if amb.path and amb.path_index >= len(amb.path):
            amb.path = []
            amb.path_index = 0
            amb.target = None

        # -------------------------
        # MOVE
        # -------------------------
        if amb.path and amb.path_index < len(amb.path):

            nr, nc = amb.path[amb.path_index]

            if grid[nr][nc] == BLOCKED:

                goal = None
                if amb.going_to_hospital:
                    goal = find_nearest_hospital(amb.pos, hospitals)
                elif amb.target:
                    goal = (amb.target.row, amb.target.col)

                if goal:
                    replan_ambulance(
                        amb, amb_index, goal,
                        current_algo, "Route blocked"
                    )
                return

            amb.pos = list(amb.path[amb.path_index])
            amb.visited_path.append(tuple(amb.pos))
            amb.path_index += 1

        # -------------------------
        # RESCUE
        # -------------------------
        if amb.target and not amb.going_to_hospital:

            if tuple(amb.pos) == (amb.target.row, amb.target.col):

                if state.medical_kits > 0:

                    state.medical_kits -= 1
                    victim = amb.target
                    victim.rescued = True

                    metrics.victims_saved += 1
                    state.victims_saved += 1
                    metrics.rescued_count += 1

                    amb.carry += 1

                    grid[victim.row][victim.col] = EMPTY

                    add_log("RESCUE",
                            f"Victim rescued at ({victim.row},{victim.col})",
                            "HIGH", "SUCCESS")

                    state.reserved_victims.discard((victim.row, victim.col))
                    amb.target = None

                    remaining = [
                        v for v in victims
                        if not v.rescued and not v.dead and not v.removed
                    ]

                    if amb.carry >= amb.max_capacity or len(remaining) == 0:

                        hospital = find_nearest_hospital(amb.pos, hospitals)
                        amb.going_to_hospital = True

                        replan_ambulance(
                            amb, amb_index,
                            hospital,
                            current_algo,
                            "Hospital transfer"
                        )

        # -------------------------
        # HOSPITAL
        # -------------------------
        elif amb.going_to_hospital:

            if tuple(amb.pos) in hospitals:

                amb.carry = 0
                state.medical_kits = min(10, state.medical_kits + 1)

                add_log("DELIVERY",
                        "Victims transferred to hospital",
                        "MEDIUM", "COMPLETED")

                amb.going_to_hospital = False
                amb.path = []
                amb.path_index = 0
                amb.target = None

# =========================
# REPLAN FUNCTION
# =========================
def replan_ambulance(amb, amb_index, goal, current_algo, trigger):

    old_path = amb.path[:]
    start = pygame.time.get_ticks()

    new_path = compute_path(current_algo, tuple(amb.pos), goal)

    time_taken = pygame.time.get_ticks() - start

    record_replanning(
        trigger,
        f"AMB-{amb_index + 1}",
        old_path,
        new_path[:],
        current_algo,
        time_taken
    )

    metrics.replanning_count += 1
    search_stats[current_algo]["replans"] += 1
    search_stats[current_algo]["searches"] += 1
    search_stats[current_algo]["path_length"] += len(new_path)

    if new_path:
        amb.path = new_path
        amb.path_index = 0
        amb.isolated = False
        return True

    amb.path = []
    amb.path_index = 0
    amb.isolated = True

    dispatch_rescue_team_for_block(amb, goal)

    add_log(
        "ROUTE",
        f"No available route for AMB-{amb_index + 1}",
        "CRITICAL",
        "WAITING"
    )

    return False