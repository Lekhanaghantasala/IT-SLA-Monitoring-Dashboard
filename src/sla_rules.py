import pandas as pd

# -----------------------------
# 1. SLA Rules
# -----------------------------

sla_rules = {
    "P1": {"frt": 1, "ttr": 8},
    "P2": {"frt": 4, "ttr": 24},
    "P3": {"frt": 8, "ttr": 48},
    "P4": {"frt": 24, "ttr": 72}
}

# -----------------------------
# 2. Read Data
# -----------------------------

df = pd.read_csv("data/tickets.csv")

# -----------------------------
# 3. Convert Dates
# -----------------------------

df["created_at"] = pd.to_datetime(df["created_at"])
df["first_response_at"] = pd.to_datetime(df["first_response_at"])
df["resolved_at"] = pd.to_datetime(df["resolved_at"])

# -----------------------------
# 4. Calculate FRT
# -----------------------------

df["frt_hours"] = (
    df["first_response_at"] - df["created_at"]
).dt.total_seconds() / 3600

# -----------------------------
# 5. Calculate TTR
# -----------------------------

df["ttr_hours"] = (
    df["resolved_at"] - df["created_at"]
).dt.total_seconds() / 3600

# -----------------------------
# 6. Add SLA Targets
# -----------------------------

df["frt_target_hours"] = df["priority"].map(
    lambda x: sla_rules[x]["frt"]
)

df["ttr_target_hours"] = df["priority"].map(
    lambda x: sla_rules[x]["ttr"]
)

# -----------------------------
# 7. FRT SLA Status
# -----------------------------

df["frt_sla_status"] = df.apply(
    lambda row: "Met"
    if row["frt_hours"] <= row["frt_target_hours"]
    else "Breached",
    axis=1
)

# -----------------------------
# 8. TTR SLA Status
# -----------------------------

df["ttr_sla_status"] = df.apply(
    lambda row:
        "Not Available"
        if pd.isna(row["ttr_hours"])
        else (
            "Met"
            if row["ttr_hours"] <= row["ttr_target_hours"]
            else "Breached"
        ),
    axis=1
)

# -----------------------------
# 9. Overall SLA Status
# -----------------------------

def calculate_sla_status(row):

    if row["frt_sla_status"] == "Breached":
        return "Breached"

    if row["status"] == "Resolved":

        if row["ttr_sla_status"] == "Breached":
            return "Breached"

        return "Met"

    return "In Progress"


df["sla_status"] = df.apply(
    calculate_sla_status,
    axis=1
)

# -----------------------------
# 10. Display Results
# -----------------------------

print(df[[
    "ticket_id",
    "priority",
    "status",
    "frt_hours",
    "frt_target_hours",
    "ttr_hours",
    "ttr_target_hours",
    "frt_sla_status",
    "ttr_sla_status",
    "sla_status"
]])

df.to_csv("data/tickets_processed.csv", index=False)
print("Processed dataset saved successfully.")