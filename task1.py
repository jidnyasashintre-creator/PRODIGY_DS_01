import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("tested.csv")

# Count males and females
gender_count = df["Sex"].value_counts()

# Create graph
ax = gender_count.plot(
    kind="bar",
    color=["skyblue", "pink"],
    figsize=(8,5)
)

# Add title and labels
plt.title("Distribution of Passengers by Gender", fontsize=14)
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)

# Add values on top of bars
for i, value in enumerate(gender_count):
    plt.text(i, value + 5, str(value), ha="center")

# Save graph
plt.savefig("gender_distribution.png")

plt.show()
# Histogram for Age Distribution

plt.figure(figsize=(8,5))

df["Age"].dropna().plot(
    kind="hist",
    bins=10,
    color="lightgreen",
    edgecolor="black"
)

plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.savefig("age_distribution.png")

plt.show()