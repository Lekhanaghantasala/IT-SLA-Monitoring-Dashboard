import pandas as pd

df = pd.read_csv("data/tickets.csv")

print("=== ALL TICKETS ===")
print(df)
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())

print("\n=== FIRST 3 ===")
print(df.head(3))

print("\n=== P1 TICKETS ===")
print(df[df["priority"] == "P1"])

print("\n=== RESOLVED ===")
print(df[df["status"] == "Resolved"])

print("\n=== OPEN ===")
print(df[df["status"] == "Open"])

print("\n=== P2 AND RESOLVED ===")
print(df[(df["priority"] == "P2") & (df["status"] == "Resolved")])
