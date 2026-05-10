# AIDRA: Adaptive Intelligent Disaster Response Assistant

**AIDRA** is a hybrid AI-based simulation system designed for autonomous disaster response in highly dynamic and resource-constrained environments. Developed using **Python** and **Pygame**, the system integrates multiple Artificial Intelligence paradigms into a unified framework to optimize rescue operations under high uncertainty.

## 🚀 Key Features

* **Hybrid AI Framework**: Seamlessly integrates search algorithms, Constraint Satisfaction Problems (CSP), machine learning, reinforcement learning, and fuzzy logic.
* **Dynamic Simulation Environment**: A 2D grid-based environment ($10 \times 11$) featuring spreading fire zones, blocked roads, and stochastic aftershocks that trigger real-time agent replanning.
* **Intelligent Pathfinding**: Implements a suite of algorithms including **A*** (with fire penalty weights), **BFS**, **DFS**, and **Greedy Best First Search** for optimal and safety-aware routing.
* **Smart Resource Allocation**: Utilizes a **CSP Solver** with **Backtracking**, **MRV heuristics**, and **Forward Checking** to manage ambulance-to-victim assignments under strict capacity constraints.
* **Predictive Analytics**: 
    * **KNN & MLP**: A hybrid ML module for survival probability estimation, balancing instance-based reasoning with non-linear pattern learning.
    * **Q-Learning**: An episodic Reinforcement Learning agent using an **Epsilon-Greedy** strategy to discover and exploit safe rescue policies.
    * **Fuzzy Logic**: Handles environmental uncertainty by computing continuous urgency and risk scores based on victim health and hazards.
* **Open-Box AI Dashboard**: Real-time visualization providing deep transparency into AI decision-making, including live confusion matrices, "Algorithm Battles," and side-by-side path comparisons.

## 🛠️ System Architecture

AIDRA follows a structured **Layered Architecture** to ensure modularity and coordinated response[cite: 305, 311]:
1.  **User Layer**: Interface for rescue operators.
2.  **Presentation Layer**: Real-time visualization via Pygame and Tkinter.
3.  **Simulation Layer**: Core engine managing grid states, hazards, and victim health decay.
4.  **Search & Planning Layer**: Computation of optimal navigation routes.
5.  **AI Decision Layer**: Integration of ML, RL, and Fuzzy Logic modules.
6.  **Constraint Satisfaction Layer**: Efficient resource and task allocation.
7.  **Analytics & Data Layer**: Performance monitoring, decision logging, and live state foundation.

## 📊 Performance Summary

* **Navigation**: $A^*$ Search achieved **12–18% shorter paths** in hazardous scenarios compared to BFS by accounting for fire penalties.
* **Learning**: The hybrid ML system achieved a peak accuracy of **91%** after the experience buffer reached maturity.
* **Optimization**: CSP heuristics (MRV and Forward Checking) reduced expanded search tree nodes by **65%** and decreased allocation latency by **50%**.

---
*Developed by Maryam Khalid and Rohan Munir at Bahria University, Islamabad.*
