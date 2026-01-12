# 🏙️ City Simulation (CustomTkinter)

A **city simulation dashboard** built with **Python and CustomTkinter**, where population, resources, and random events evolve over time.  
The simulation runs in real-time with adjustable speed, visual resource indicators, and an event log that explains *why* the city changes.

This project focuses on **state management, simulation loops, and UI synchronization** rather than complex graphics.

---

## ✨ Features

### Core Simulation
- Day-by-day city progression
- Adjustable simulation speed (×1, ×2, ×5)
- Start / Pause control
- Automatic city collapse detection

### City Systems
- **Population**
  - Grows or declines based on food and energy availability
- **Resources**
  - Food
  - Energy
  - Money
- Production and consumption are tied directly to population size

### Random Events
Events occur randomly and affect the city for several days:
- 🌾 Drought (reduces food production)
- ⚡ Power Outage (reduces energy production)
- 💰 Economic Boom (boosts money production)
- 🦠 Disease (reduces population)

Each event:
- Has a duration
- Modifies city behavior
- Is logged clearly in the event log

### User Interface (CustomTkinter)
- Dashboard-style layout
- Live-updating labels
- Progress bars for each resource
- Scrollable event log showing cause → effect

---

## 🧠 Architecture Overview

The project is structured around **clear separation of concerns**:

### `CityState`
- Holds all city data (population, resources, events, logs)
- Acts as the single source of truth

### `SimulationEngine`
- Updates city state on every tick
- Handles:
  - Resource math
  - Population growth / decline
  - Random events
  - Collapse conditions

### `CitySimUI`
- Displays city state using CustomTkinter
- Sends user actions (start, pause, speed) to the engine
- Refreshes UI without handling simulation logic

This mirrors real-world software design patterns.

---

## 🖥️ Controls

| Action | Description |
|------|-------------|
| Start / Pause | Toggle simulation |
| Speed ×1 | Normal speed |
| Speed ×2 | Faster simulation |
| Speed ×5 | Very fast simulation |

---

## ⚠️ City Collapse Conditions

The city will automatically collapse if:
- Population reaches **zero**

Warnings appear in the log if:
- Food reaches zero
- Money reaches zero

Once collapsed, the simulation stops.

---

## 📦 Requirements

- Python **3.9+**
- `customtkinter`

Install CustomTkinter:
```bash
pip install customtkinter
