import pandas as pd

# Load your 15-column file
df = pd.read_csv('data/tickets_processed.csv')

# Add 4 new columns for master dataset

# 1. current_age_hours - simulated age (for demo)
# For Resolved tickets, age = target + 10, for Open = target - remaining
df['current_age_hours'] = df.apply(lambda x: x['ttr_target_hours'] + 10 if x['sla_status']=='Met' else x['ttr_target_hours'] - 2 if x['ticket_id'] in ['T003','T009'] else x['ttr_target_hours'] + 20, axis=1)

# 2. remaining_sla_hours
df['remaining_sla_hours'] = df['ttr_target_hours'] - df['current_age_hours']

# 3. risk_status
def get_risk(row):
    if row['sla_status'] == 'Met':
        return 'Resolved'
    elif row['remaining_sla_hours'] <= 0:
        return 'Breached'
    elif row['remaining_sla_hours'] <= 5:
        return 'At Risk'
    else:
        return 'Safe'

df['risk_status'] = df.apply(get_risk, axis=1)

# 4. next_action
def get_action(risk):
    if risk == 'Resolved': return 'No Action'
    if risk == 'At Risk': return 'Prioritize'
    if risk == 'Breached': return 'Escalate'
    return 'Monitor'

df['next_action'] = df['risk_status'].apply(get_action)

# 5. Reorder to 19 columns
# Make sure we have all expected columns
final = df

# Save FINAL master
final.to_csv('data/tickets_processed_final.csv', index=False)

print(f"Final master created: {final.shape}")
print(final[['ticket_id','sla_status','remaining_sla_hours','risk_status','next_action']].to_string())
print(f"Columns: {list(final.columns)}")