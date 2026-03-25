Care Journey & Operational Bottleneck Analyzer

📌 Project Overview
In mental healthcare, the "Time-to-Care" (the gap between a client’s initial inquiry and their first therapy session) is the most critical predictor of patient success. If a match stalls, the likelihood of a patient disengaging increases exponentially.

This Python-based Operational Suite automates the triaging process for Care Coordination teams. It identifies exactly where patients are stuck in the funnel and generates high-priority outreach lists, transforming a reactive workflow into a proactive, data-driven strategy.

🚀 Key Features

Dynamic Risk Segmentation: Automatically categorizes patients into "High Risk," "Pending," or "Active" based on time-delays in the care journey.

Visual Pipeline Dashboard: Generates a .png bar chart highlighting the distribution of patient statuses for executive-level reporting.

Automated Triage Reporting: Exports a daily_outreach_report.csv, providing coordinators with a pre-filtered "To-Do" list of clients needing immediate intervention.

KPI Tracking: Calculates the "Time-to-Care" delta to help management identify systemic bottlenecks in the matching process.

🛠️ Tech Stack & Dependencies

Python 3.x

Pandas: For data wrangling, cleaning, and date-delta calculations.

Matplotlib: For programmatic data visualization.

Subprocess/OS: For automated file generation and system-level reporting.

📁 Project Structure

data_generator.py: A utility script to create 50+ rows of realistic, "messy" patient data for testing.

care_journey_analyzer.py: The core logic engine that processes data and runs the risk-assessment functions.

care_journey_dashboard.png: A visual snapshot of the current patient pipeline.

daily_outreach_report.csv: The actionable spreadsheet for the Care Coordination team.

📊 Business Logic (The "Why")

The script uses a 7-day "Stalled Match" threshold.

If a patient has completed a matching consult but hasn't booked a first session within 7 days, they are flagged as High Risk.

This allows the operations team to focus 100% of their manual outreach on the 20% of patients most likely to drop off, significantly increasing the "conversion-to-care" rate.
