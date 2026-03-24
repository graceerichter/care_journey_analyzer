# care_journey_analyzer
A Python analytics tool for healthcare operations. It identifies bottlenecks in the patient journey, calculates 'Time-to-Care' deltas, and flags high-risk stalled matches to improve clinical onboarding and ensure no patient falls through the cracks.

*Overview*
In mental healthcare coordination, the transition from a matching consult to the first therapy session is a critical window. Delays in this "Time-to-Care" period are highly correlated with patient drop-off.

This project is a Python-based decision-support tool designed to help Care Coordination teams move from manual triaging to data-driven outreach. It analyzes patient milestone data to identify exactly where the "leaky bucket" is in the onboarding funnel and flags specific clients who require immediate follow-up.


*Features*
Automated Risk Categorization: Uses custom logic to flag "High Risk" cases where a match has stalled for more than 7 days.

Time-to-Care Metrics: Calculates the average duration between inquiry, consultation, and the first session.

Operational Dashboard: Generates a visual bar chart (via Matplotlib) to give leadership a bird's-eye view of the current patient pipeline.

Actionable Outreach List: Filters and exports a high-priority list of clients needing intervention, saving coordinators hours of manual spreadsheet review.


*Tech Stack*
Python 3

Pandas: For data manipulation and datetime delta calculations.

Matplotlib: For data visualization and pipeline reporting.


*How It Works*
Data Ingestion: The script reads a care_journey_data.csv containing patient milestones.

Date Processing: Converts raw strings into datetime objects to calculate precise "days-since" metrics.

Risk Mapping: Applies a logic function to segment patients into categories like High Risk: Stalled Match, Pending, or Active Care.

Reporting: Outputs a summary of urgent tasks and saves a visual distribution chart (care_journey_dashboard.png).


*Impact*
This tool transforms the Care Coordinator role from reactive to proactive. By identifying bottlenecks in real-time, operations teams can:

Improve Retention: Intervene before a patient disengages from the process.

Optimize Workflows: Identify if specific stages of the funnel (e.g., insurance verification) are causing systemic delays.

Scale Operations: Automate the "who do I call today?" decision-making process.
