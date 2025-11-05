import pandas as pd
from src import io_utils

# df = pd.read_csv("ecommerce_sales.csv")


def mean(df):
    print("Medelvärde per order är: ", df["revenue"].mean().round(2),"kr.")


def top_3(df):
    top_3 = (
        df.groupby("category")["revenue"]  
        .sum()
        .round(2)                           
        .sort_values(ascending=False)    
        .head(3)    
        .reset_index()                  
    )
    top_3.index = top_3.index +1
    print(top_3)


def purchasesCategory(df):
    print(df["category"].value_counts())


def intaktStad(df):
    
    intakt_per_stad = (df.groupby("city")["revenue"]
                   .sum()
                   .sort_values(ascending=False)
                   .reset_index()
                    )
    return intakt_per_stad
