# AIDRA: Adaptive Intelligent Disaster Response Assistant

[cite_start]**AIDRA** is a hybrid AI-based simulation system designed for autonomous disaster response in highly dynamic and resource-constrained environments[cite: 287]. [cite_start]Developed using **Python** and **Pygame**, the system integrates multiple Artificial Intelligence paradigms into a unified framework to optimize rescue operations under high uncertainty[cite: 289, 449].

## 🚀 Key Features

* [cite_start]**Hybrid AI Framework**: Seamlessly integrates search algorithms, Constraint Satisfaction Problems (CSP), machine learning, reinforcement learning, and fuzzy logic[cite: 301, 517].
* [cite_start]**Dynamic Simulation Environment**: A 2D grid-based environment ($10 \times 11$) featuring spreading fire zones, blocked roads, and stochastic aftershocks that trigger real-time agent replanning[cite: 330, 331, 336].
* [cite_start]**Intelligent Pathfinding**: Implements a suite of algorithms including **A*** (with fire penalty weights), **BFS**, **DFS**, and **Greedy Best First Search** for optimal and safety-aware routing[cite: 307, 393, 395].
* [cite_start]**Smart Resource Allocation**: Utilizes a **CSP Solver** with **Backtracking**, **MRV heuristics**, and **Forward Checking** to manage ambulance-to-victim assignments under strict capacity constraints[cite: 308, 407, 408].
* **Predictive Analytics**: 
    * [cite_start]**KNN & MLP**: A hybrid ML module for survival probability estimation, balancing instance-based reasoning with non-linear pattern learning[cite: 309, 416, 422].
    * [cite_start]**Q-Learning**: An episodic Reinforcement Learning agent using an **Epsilon-Greedy** strategy to discover and exploit safe rescue policies[cite: 438].
    * [cite_start]**Fuzzy Logic**: Handles environmental uncertainty by computing continuous urgency and risk scores based on victim health and hazards[cite: 443, 444].
* [cite_start]**Open-Box AI Dashboard**: Real-time visualization providing deep transparency into AI decision-making, including live confusion matrices, "Algorithm Battles," and side-by-side path comparisons[cite: 448, 463, 464].

## 🛠️ System Architecture

[cite_start]AIDRA follows a structured **Layered Architecture** to ensure modularity and coordinated response[cite: 305, 311]:
1.  [cite_start]**User Layer**: Interface for rescue operators[cite: 311].
2.  [cite_start]**Presentation Layer**: Real-time visualization via Pygame and Tkinter[cite: 311].
3.  [cite_start]**Simulation Layer**: Core engine managing grid states, hazards, and victim health decay[cite: 311].
4.  [cite_start]**Search & Planning Layer**: Computation of optimal navigation routes[cite: 312].
5.  [cite_start]**AI Decision Layer**: Integration of ML, RL, and Fuzzy Logic modules[cite: 312].
6.  [cite_start]**Constraint Satisfaction Layer**: Efficient resource and task allocation[cite: 313].
7.  [cite_start]**Analytics & Data Layer**: Performance monitoring, decision logging, and live state foundation[cite: 314].

## 📊 Performance Summary

* [cite_start]**Navigation**: $A^*$ Search achieved **12–18% shorter paths** in hazardous scenarios compared to BFS by accounting for fire penalties[cite: 478, 479].
* [cite_start]**Learning**: The hybrid ML system achieved a peak accuracy of **91%** after the experience buffer reached maturity[cite: 435].
* [cite_start]**Optimization**: CSP heuristics (MRV and Forward Checking) reduced expanded search tree nodes by **65%** and decreased allocation latency by **50%**[cite: 488, 492].

---
[cite_start]*Developed by Maryam Khalid and Rohan Munir at Bahria University, Islamabad[cite: 281, 283, 286].*
