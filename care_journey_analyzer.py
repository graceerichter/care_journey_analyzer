import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Load the data (assuming care_journey_data.csv exists)
df = pd.read_csv('care_journey_data.csv')

# 2. Convert to datetime for logic
date_cols = ['inquiry_date', 'consult_date', 'first_session_date']
for col in date_cols:
    df[col] = pd.to_datetime(df[col])

# Set a mock 'today' date for the analysis
today = pd.to_datetime('2026-03-24')

# 3. Categorize patients by Operational Risk
def categorize_status(row):
    if pd.notnull(row['first_session_date']):
        return 'Active Care'
    if pd.notnull(row['consult_date']):
        # If consult happened > 7 days ago and no session booked
        days_since_consult = (today - row['consult_date']).days
        if days_since_consult > 7:
            return 'High Risk: Stalled Match'
        return 'Pending: Post-Consult'
    if pd.notnull(row['inquiry_date']):
        # If inquiry happened > 3 days ago and no consult booked
        days_since_inquiry = (today - row['inquiry_date']).days
        if days_since_inquiry > 3:
            return 'High Risk: No Consult'
        return 'New Inquiry'
    return 'Unknown'

df['status_category'] = df.apply(categorize_status, axis=1)

# 4. Generate Visual Insights
status_counts = df['status_category'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
status_counts.plot(kind='bar', color=['#4CAF50', '#FF9800', '#2196F3', '#F44336'])
plt.title('Care Journey Pipeline: Identifying Patient Drop-off', fontsize=14)
plt.ylabel('Number of Patients')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the visual for the portfolio
plt.savefig('care_journey_dashboard.png')
print("Analysis complete. Dashboard saved as care_journey_dashboard.png")
# 5. Create the Outreach List (Filtered for only High Risk/Pending)
outreach_list = df[df['status_category'].str.contains('High Risk|Pending')].copy()

# 6. Export the Actionable Spreadsheet
# 'index=False' prevents Python from adding an extra column of row numbers
outreach_list.to_csv('daily_outreach_report.csv', index=False)

# 7. Export the High-Level Summary (The stats for your manager)
status_counts.to_csv('executive_summary_report.csv', header=['Patient_Count'])

print("--- Reports Generated ---")
print("1. daily_outreach_report.csv (The to-do list)")
print("2. executive_summary_report.csv (The high-level stats)")
