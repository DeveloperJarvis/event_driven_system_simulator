# **LLD (Low-Level Design) of an Event-Driven System Simulator**

> Example domains: traffic systems, service queues
> Skills: simulation modeling, priority queues
> In Python — but without writing code

So we’ll design it like you would in a real interview or production spec.

---

# 1⃣ What Is an Event-Driven Simulator?

Instead of advancing time in fixed steps (Δt), we:

- Maintain a **global simulation clock**
- Maintain a **priority queue of events**
- Always process the **next earliest event**
- Jump the clock forward to that event’s timestamp

This is called **Discrete Event Simulation (DES)**.

---

# 2⃣ Core Design Goals

We want a system that:

- Supports multiple event types
- Uses a **priority queue (min-heap)** ordered by event time
- Allows new events to be scheduled dynamically
- Can model different domains:
  - Traffic intersections
  - Bank queues
  - Call centers
  - CPU scheduling

---

# 3⃣ Core Components (LLD)

---

## 🔹 1. Event

Represents something that happens at a specific time.

### Responsibilities:

- Store timestamp
- Store event type
- Store metadata (payload)
- Execute its logic

### Attributes:

- `timestamp: float`
- `event_type: Enum`
- `payload: dict`
- `id: unique identifier`

### Methods:

- `process(simulation_context)`

---

## 🔹 2. EventQueue

Responsible for storing future events in time order.

### Data Structure:

- **Min-heap (priority queue)**
- Ordered by `timestamp`

### Responsibilities:

- Insert new event
- Pop next event
- Peek next event
- Check if empty

### Internal Structure:

- Heap of `(timestamp, event_id, event_object)`
  - `event_id` prevents tie-breaking issues

---

## 🔹 3. SimulationEngine

The orchestrator.

### Attributes:

- `current_time`
- `event_queue`
- `is_running`
- `metrics_collector`
- `system_state`

### Core Method:

```
run(until_time=None)
```

### Execution Loop:

1. While event_queue not empty:
2. Pop earliest event
3. Advance current_time to event.timestamp
4. Call event.process(self)
5. Event may schedule new events
6. Stop if until_time reached

---

## 🔹 4. SystemState

Represents the real-world modeled system.

This is domain-specific.

For example:

### Traffic System

- List of intersections
- Vehicles in network
- Signal states

### Queue System

- Queue length
- Server availability
- Waiting customers

The SimulationEngine passes this state to events.

---

## 🔹 5. MetricsCollector

Collects statistics:

- Average waiting time
- Throughput
- Max queue length
- Utilization
- Event count

Updated during event processing.

---

# 4⃣ Event Types (Example: Queue Simulation)

Consider a bank queue system.

---

## Event Types:

### 1⃣ CustomerArrival

- Adds customer to queue
- If server idle → schedule ServiceStart
- Schedule next arrival (Poisson process)

---

### 2⃣ ServiceStart

- Removes customer from queue
- Schedules ServiceEnd

---

### 3⃣ ServiceEnd

- Marks server free
- If queue not empty → schedule ServiceStart

---

# 5⃣ Example Flow (Queue System)

Initial Setup:

- Schedule first CustomerArrival at time = 0

Simulation:

| Time | Event           |
| ---- | --------------- |
| 0.0  | CustomerArrival |
| 1.2  | CustomerArrival |
| 1.5  | ServiceEnd      |
| 2.3  | CustomerArrival |

The engine jumps time:

```
0 → 1.2 → 1.5 → 2.3
```

No wasted computation between events.

---

# 6⃣ Example Flow (Traffic System)

Model:

- Intersections
- Vehicles
- Traffic signals

Event Types:

- VehicleArrival
- LightChange
- VehicleDeparture

Example:

1. Vehicle arrives at red light
2. LightChange scheduled at +30s
3. When LightChange occurs:
   - All waiting vehicles get departure events

---

# 7⃣ Data Model (High-Level UML Style)

```
SimulationEngine
 ├── EventQueue
 ├── SystemState
 ├── MetricsCollector
 └── run()

Event (abstract)
 ├── timestamp
 ├── process()

CustomerArrival(Event)
ServiceStart(Event)
ServiceEnd(Event)

SystemState
 ├── Queue
 ├── Servers
 ├── TrafficLights
```

---

# 8⃣ Priority Queue Role (Critical)

This is the heart of the system.

Why?

Because:

- Events must execute in strict time order
- New events can be added at any time
- Complexity:
  - Insert → O(log n)
  - Pop → O(log n)

If we used a list → O(n) insertion.

Heap makes system scalable.

---

# 9⃣ Extensibility Design

To make it clean:

### Use Event as Base Class

Each event implements:

```
process(context)
```

This allows:

- Open/Closed principle
- Adding new event types without changing engine

---

# 🔟 Threading Considerations

Basic simulator → single-threaded

For large systems:

- Partition simulation space
- Use distributed event queues
- Synchronize via conservative or optimistic algorithms

(Advanced topic)

---

# 1⃣1⃣ Determinism

To make simulation reproducible:

- Seed random number generator
- Avoid system clock
- Control event ordering

---

# 1⃣2⃣ Edge Cases to Handle

- Two events at same timestamp
- Infinite event scheduling loop
- Event scheduling in the past
- Memory growth of event queue
- Simulation stop conditions

---

# 1⃣3⃣ Time Complexity

If:

- E = number of events

Total complexity:

```
O(E log E)
```

Because each event insertion/pop is log E.

---

# 1⃣4⃣ Example Use Cases

This architecture can simulate:

- ATM queues
- Airport runway scheduling
- Traffic intersections
- Elevator systems
- CPU job scheduling
- Hospital ER flow
- Packet routing networks

---

# 1⃣5⃣ How This Impresses in Interviews

If you explain:

- Discrete-event simulation model
- Priority queue usage
- Clean event abstraction
- Separation of engine & domain logic
- Metrics collection
- Deterministic replay

You’re operating at **strong backend/system design level**.
