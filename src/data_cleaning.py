import pandas as pd

# Read CSV
df = pd.read_csv("data/tickets.csv")

print("Original Data")
print(df)

# Check missing values
print("Missing Values")
print(df.isnull().sum())

# Check data types
print("Data Types")
print(df.dtypes)

# Convert date columns
df["created_at"] = pd.to_datetime(df["created_at"])

df["first_response_at"] = pd.to_datetime(df["first_response_at"])

df["resolved_at"] = pd.to_datetime(df["resolved_at"])

# Check updated data types
print("Updated Data Types")
print(df.dtypes)

# Check duplicate ticket IDs
print("Duplicate Ticket IDs")
print(df["ticket_id"].duplicated().sum())

# Clean category
df["category"] = df["category"].str.strip()

# Show open tickets
print("Open Tickets")
print(df[df["status"] == "Open"])

# Show tickets without resolution time
print("Tickets Without Resolution Time")
print(df[df["resolved_at"].isnull()])

print("Cleaned Data")
print(df)