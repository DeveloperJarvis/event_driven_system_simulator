# Event-Driven System Simulator

**Author:** Developer Jarvis (Pen Name)
**Contact:** [https://github.com/DeveloperJarvis](https://github.com/DeveloperJarvis)

---

## Overview

The **Event-Driven System Simulator** is a Python-based framework for modeling and simulating real-world systems using **discrete-event simulation (DES)**. Instead of progressing time in fixed intervals, the simulator processes events in chronological order, making it efficient for large-scale simulations.

It can model systems such as:

- Traffic intersections and road networks
- Service queues (banks, call centers, hospitals)
- Resource scheduling and multi-server systems
- Any scenario where events occur over time

---

## Features

- **Event abstraction:** Easily define custom event types and behaviors
- **Priority queue-based engine:** Ensures events are processed in chronological order
- **System state modeling:** Track entities like vehicles, customers, servers, and queues
- **Metrics collection:** Capture statistics such as throughput, waiting times, and resource utilization
- **Deterministic simulation:** Reproducible results with controlled random seeds
- **Extensible design:** Add new event types or system behaviors without modifying the engine

---

## Architecture

The simulator consists of the following components:

1. **Simulation Engine:** Orchestrates the simulation, manages the global clock, and executes events.
2. **Event Queue:** A min-heap priority queue that stores future events ordered by timestamp.
3. **Event Base Class:** Abstract class representing events; custom events inherit and implement the `process()` method.
4. **System State:** Represents the current state of the modeled system (queues, servers, traffic lights, vehicles, etc.).
5. **Metrics Collector:** Collects and reports statistics during or after the simulation.

---

## Event Types (Examples)

### Queue Simulation

- **CustomerArrival:** Adds customers to the queue and schedules service if a server is free
- **ServiceStart:** Begins serving a customer and schedules ServiceEnd
- **ServiceEnd:** Frees the server and continues with the next queued customer

### Traffic Simulation

- **VehicleArrival:** Adds a vehicle to the network or intersection
- **LightChange:** Updates traffic signal states and triggers vehicle departures
- **VehicleDeparture:** Moves vehicles through intersections

---

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/DeveloperJarvis/event-driven-simulator.git
```

2. Set up Python environment (Python 3.9+ recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Create a simulation scenario by defining **events** and **system state**, then run the **SimulationEngine**.

---

## Extending the Simulator

- Add new **Event subclasses** by implementing `process(simulation_context)`
- Modify or extend **SystemState** to include new entities or resources
- Customize **MetricsCollector** for additional statistics

---

## Advantages

- Efficient for large-scale simulations due to event-driven processing
- Flexible for multiple domains without rewriting the core engine
- Provides detailed analytics for system optimization

---

## Author

**Developer Jarvis** (Pen Name)
GitHub: [https://github.com/DeveloperJarvis](https://github.com/DeveloperJarvis)
