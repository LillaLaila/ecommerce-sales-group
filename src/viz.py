import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src import metrics, io_utils



def barKategori(df):
    purchase = df["category"].value_counts()  # Räknar 
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