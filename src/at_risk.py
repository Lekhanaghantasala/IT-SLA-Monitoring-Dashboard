import pandas as pd

# SLA rules
sla_rules = {
    "P1": {"frt": 1, "ttr": 8},
    "P2": {"frt": 4, "ttr": 24},
    "P3": {"frt": 8, "ttr": 48},
    "P4": {"frt": 24, "ttr": 72}
}

# Read dataset
df = pd.read_csv("data/tickets.csv")

# Convert date columns
df["created_at"] = pd.to_datetime(df["created_at"])
df["first_response_at"] = pd.to_datetime(df["first_response_at"])
df["resolved_at"] = pd.to_datetime(df["resolved_at"])

# Add TTR target
df["ttr_target_hours"] = df["priority"].map(
    lambda x: sla_rules[x]["ttr"]
)

# Fixed analysis time for project demonstration
current_time = pd.Timestamp("2026-09-03 09:00")

# Calculate current ticket age
df["current_age_hours"] = (
    current_time - df["created_at"]
).dt.total_seconds() / 3600


# Calculate risk status
def calculate_risk(row):

    if row["status"] == "Resolved":
        return "Resolved"

    if row["current_age_hours"] >= row["ttr_target_hours"]:
        return "Breached"

    if row["current_age_hours"] >= (
        row["ttr_target_hours"] * 0.80
    ):
        return "At Risk"

    return "Safe"


df["risk_status"] = df.apply(
    calculate_risk,
    axis=1
)

# Calculate remaining SLA time
df["remaining_sla_hours"] = (
    df["ttr_target_hours"]
    - df["current_age_hours"]
)

# Calculate next action
def next_action(row):

    if row["risk_status"] == "At Risk":
        return "Prioritize"

    if row["risk_status"] == "Breached":
        return "Escalate"

    if row["risk_status"] == "Safe":
        return "Monitor"

    return "No Action"


df["next_action"] = df.apply(
    next_action,
    axis=1
)

# Display results
print("AT-RISK ANALYSIS")
print(
    df[[
        "ticket_id",
        "priority",
        "category",
        "assignee_id",
        "status",
        "current_age_hours",
        "ttr_target_hours",
        "remaining_sla_hours",
        "risk_status",
        "next_action"
    ]]
)

# Save processed data
df.to_csv("data/tickets_at_risk.csv",
    index=False
)

print("At-risk dataset saved successfully.")