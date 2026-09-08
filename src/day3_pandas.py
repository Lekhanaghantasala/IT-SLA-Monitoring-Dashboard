import pandas as pd

df = pd.read_csv("data/tickets.csv")

print("=== ALL TICKETS ===")
print(df)

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== COLUMNS ===")
print(df.columns.tolist())

print("\n=== P1 TICKETS ===")
p1 = df[df["priority"] == "P1"]
print(p1)

print("\n=== RESOLVED ===")
resolved = df[df["status"] == "Resolved"]
print(resolved)

print("\n=== OPEN ===")
open_t = df[df["status"] == "Open"]
print(open_t)