import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src import metrics, io_utils

# försäljning över tid (linje/månad)
def line_sales_over_time(df):
    df['date'] = pd.to_datetime(df['date']) #https://www.youtube.com/watch?v=vnTWXn9LtHM
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.month_name()
    sales_by_mnth = df.groupby(['month', 'month_name'])['revenue'].sum().reset_index().sort_values('month')

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(sales_by_mnth['month_name'], sales_by_mnth['revenue'], marker='o', linestyle="-")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Inkomst")
    ax.set_title("Försäljning under första halvåret (per månad)")
    ax.grid()
    plt.show()
    print(f"Diagrammet visar hur intäkterna förändras från januari till june.\nVi ser en ökning av försäljningen från mars till maj, medan intäkterna minskar från januari till mars och från maj till june.")



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


def barintaktkategori(df):
    income_by_cat =metrics.income_by_category(df)
    income_by_cat["revenue"] = pd.to_numeric(income_by_cat["revenue"], errors="coerce")
    income_by_cat["revenue"] = income_by_cat["revenue"] /1_000_000

    plt.figure(figsize=(8, 5))
    plt.bar(income_by_cat["category"], income_by_cat["revenue"], color="skyblue", edgecolor = "black")
    plt.ylabel("Intäkt (miljoner kr)")
    plt.xlabel("Kategori")
    plt.title("Intäkt per kategori")
    plt.grid(axis="y", linestyle = "--", alpha=0.7)
    plt.tight_layout()
    plt.show()
    print("Diagrammet visar totala intäkter per kategori. ")