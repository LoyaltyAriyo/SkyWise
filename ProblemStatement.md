# Problem Statement – SkyWise Telescope Scheduler

### Background
Astronomical observations are constrained by weather, moonlight, and limited telescope time. Large observatories use complex scheduling software, but amateur astronomers and student observatories often lack access to such tools. A lightweight, automated scheduler can make observation planning more efficient and accessible.

### Problem
Manually planning telescope sessions is inefficient and prone to errors:
- Clear sky windows may be missed without weather forecasts.
- Targets too close to the Moon or too low on the horizon reduce data quality.
- Conflicts arise when multiple high-priority targets compete for the same hours.
- Without optimization, valuable telescope time can be wasted.

### Goal
Design and implement **SkyWise**, a telescope scheduler that:
- Integrates **weather forecasts, lunar constraints, and astronomical calculations**.  
- Ranks targets based on **visibility, sky conditions, and scientific priority**.  
- Assigns observation time slots using a **greedy optimization approach**.  
- Produces professional outputs: **CSV schedule, Gantt chart visualization, and summary stats**.

### Scope (Version 1)
- **In scope**:
  - Configurable site info (latitude, longitude, elevation, timezone).
  - Target list with RA/Dec and priority.
  - Astronomical night detection (sun < –18°).
  - Constraints: cloud cover, altitude, airmass, moon separation.
  - Greedy scheduling algorithm with scoring function.
  - Outputs: schedule.csv, Gantt chart, summary report.
- **Future expansion**:
  - Web UI for multiple users.
  - Advanced optimization algorithms (e.g., integer programming).
  - Real-time telescope hardware integration.

### Expected Impact
SkyWise will demonstrate real-world **resource optimization under constraints**, combining **astronomy, data integration, and algorithm design**. It can serve as a practical tool for small observatories and as a strong portfolio project for showcasing applied software engineering skills.


