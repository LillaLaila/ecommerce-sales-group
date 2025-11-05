import pandas as pd
from src import io_utils


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


def intaktStad(df):
    
    intakt_per_stad = (df.groupby("city")["revenue"]
                   .sum()
                   .sort_values(ascending=False)
                   .reset_index()
                    )
    return intakt_per_stad

# Total intäkt /Ben




# Totalt antal enheter /Ben



# Intäkt per kategori /Milda
def income_by_category(df):
    income_by_cat = df.groupby('category')['revenue'].sum().reset_index()
    return income_by_cat

# Intäkt per stad /Milda
def income_by_city(df):
    income_city = df.groupby('city')['revenue'].sum().reset_index()
    return income_city
