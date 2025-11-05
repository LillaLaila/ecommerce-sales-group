import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src import metrics, io_utils

# försäljning över tid (linje/månad)
def line_sales_over_time(df):
    df['date'] = pd.to_datetime(df['date']) #https://www.youtube.com/watch?v=vnTWXn9LtHM
    df['month'] = df['date'].dt.month_name()
    sales_by_mnth = df.groupby('month')['revenue'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(sales_by_mnth['month'], sales_by_mnth['revenue'], marker='o', linestyle="-")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.set_title("Sales over time by month")
    ax.grid()
    plt.show()


def barKategori(df):
    purchase = df["category"].value_counts()
    plt.figure(figsize=(8, 5))
    plt.bar(purchase.index, purchase.values)
    plt.ylabel("Antal köp")
    plt.grid(axis="y")
    plt.xlabel("Kategori")
    plt.title("Antal köp per kategori")
    plt.tight_layout()
    plt.show()

def barStader(df):
    staderIntakt = metrics.intaktStad(df)
    staderIntakt["revenue"] = pd.to_numeric(staderIntakt["revenue"], errors="coerce")
    staderIntakt["revenue"] = staderIntakt["revenue"]/1000  
    
    plt.figure(figsize=(8, 5))
    plt.bar(staderIntakt["city"], staderIntakt["revenue"])
    plt.ylabel("Intäkt per stad (tkr)")
    plt.xlabel("Städer")
    plt.title("Intäkter per stad")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()