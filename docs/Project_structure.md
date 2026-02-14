# Project structure

```
event-driven-simulator/
│
├── README.md
├── requirements.txt
├── setup.py                # Optional if packaging as a module
├── LICENSE
│
├── simulator/              # Core simulation engine
│   ├── __init__.py
│   ├── engine.py           # SimulationEngine class (main loop, event processing)
│   ├── event.py            # Base Event class and helper methods
│   ├── event_queue.py      # Priority queue implementation for event scheduling
│   ├── metrics.py          # MetricsCollector for tracking statistics
│   └── utils.py            # Utility functions (time formatting, logging, random seed control)
│
├── models/                 # Domain-specific system models
│   ├── __init__.py
│   ├── queue_system.py     # Queue-based systems (customers, servers)
│   ├── traffic_system.py   # Traffic simulation (vehicles, lights)
│   └── generic_system.py   # Base system state classes for custom scenarios
│
├── events/                 # Predefined event types for various systems
│   ├── __init__.py
│   ├── queue_events.py     # CustomerArrival, ServiceStart, ServiceEnd
│   ├── traffic_events.py   # VehicleArrival, LightChange, VehicleDeparture
│   └── custom_events.py    # Placeholder for user-defined events
│
├── scenarios/              # Example simulations / scripts
│   ├── __init__.py
│   ├── queue_simulation.py
│   └── traffic_simulation.py
│
└── tests/                  # Unit tests
    ├── __init__.py
    ├── test_engine.py
    ├── test_events.py
    └── test_metrics.py
```

### ✅ Key Points About This Structure:

1. **Separation of Concerns**
   - `simulator/` handles the **engine** and **core infrastructure**
   - `models/` defines **system states**
   - `events/` defines **event types**

2. **Extensibility**
   - Adding a new system (e.g., hospital simulation) is as simple as creating `models/hospital_system.py` and `events/hospital_events.py`.

3. **Scenario-Based Testing**
   - `scenarios/` folder allows running different simulations without touching the engine.

4. **Testable Modules**
   - All core logic is in separate files, making **unit testing** straightforward.
