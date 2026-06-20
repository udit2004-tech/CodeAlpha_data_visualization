import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 17000, 21000, 25000],
    "Profit": [3000, 4000, 5000, 4500, 6000, 7500]
}

df = pd.DataFrame(data)

sns.set_style("whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Sales Dashboard", fontsize=16)

sns.lineplot(
    x="Month",
    y="Sales",
    data=df,
    marker="o",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Monthly Sales")

sns.barplot(
    x="Month",
    y="Profit",
    data=df,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Monthly Profit")

sns.scatterplot(
    x="Sales",
    y="Profit",
    data=df,
    s=150,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Sales vs Profit")

axes[1, 1].pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)
axes[1, 1].set_title("Sales Distribution")

plt.tight_layout()
plt.show()