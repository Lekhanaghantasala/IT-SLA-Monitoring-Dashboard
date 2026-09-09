import pandas as pd

# Read data
df = pd.read_csv("data/tickets.csv")

# Convert timestamps to datetime
df["created_at"] = pd.to_datetime(df["created_at"])
df["first_response_at"] = pd.to_datetime(df["first_response_at"])
df["resolved_at"] = pd.to_datetime(df["resolved_at"])

# Calculate FRT
df["frt"] = df["first_response_at"] - df["created_at"]

# Convert FRT to hours
df["frt_hours"] = df["frt"].dt.total_seconds() / 3600

# Calculate TTR
df["ttr"] = df["resolved_at"] - df["created_at"]

# Convert TTR to hours
df["ttr_hours"] = df["ttr"].dt.total_seconds() / 3600

# Display results
print(df[[
    "ticket_id",
    "priority",
    "status",
    "frt_hours",
    "ttr_hours"
]])

# Summary
print(f"Average FRT: {df['frt_hours'].mean():.2f} hours")
print(f"Average TTR (resolved only): {df['ttr_hours'].mean():.2f} hours")