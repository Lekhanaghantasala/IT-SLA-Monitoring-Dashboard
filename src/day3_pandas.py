import pandas as pd

# Read CSV
df = pd.read_csv("data/tickets.csv")

# Display all data
print(df)

# First 5 rows
print(df.head())

# Dataset size
print(df.shape)

# Column names
print(df.columns)

# One column
print(df["priority"])

# Multiple columns
print(df[["ticket_id", "priority", "status"]])

# P1 tickets
p1_tickets = df[df["priority"] == "P1"]
print(p1_tickets)

# Resolved tickets
resolved = df[df["status"] == "Resolved"]
print(resolved)

# Open tickets
open_tickets = df[df["status"] == "Open"]
print(open_tickets)

# P2 and Resolved
result = df[
    (df["priority"] == "P2") &
    (df["status"] == "Resolved")
]
print(result)