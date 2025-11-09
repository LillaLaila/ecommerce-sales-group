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


# Intäkt per kategori /Milda
def income_by_category(df):
    income_by_cat = df.groupby('category')['revenue'].sum().reset_index()
    max_cat_name = income_by_cat['category'][income_by_cat['revenue'].idxmax()]
    max_cat_value = income_by_cat['revenue'].max()

    print(f"Intäkt per kategori:\n{income_by_cat}")
    print(f"Tabellen visar intäkter per kategori.\nDen högsta intäkten är i kategorien {max_cat_name} {max_cat_value} kr.\n")
    return income_by_cat

# Intäkt per stad /Milda
def income_by_city(df):
    income_city = df.groupby('city')['revenue'].sum().reset_index()
    max_city_name = income_city['city'][income_city['revenue'].idxmax()]
    max_city_value = income_city['revenue'].max()
    

    print(f"Intäkt per stad:\n{income_city}")
    print(f"Tabellen visar intäkter per stad.\n{max_city_name} har den högsta intäkten {max_city_value} kr.")
    return income_city


#Totala intäkter /Ben
def total_revenue(df):
    total_rev = df["revenue"].sum().round(2)
    print(f"Totala intäkter är: {total_rev} kr.")
    return total_rev

#Totalt antal enheter /Ben
def total_units(df):
    total_units = df["units"].sum()
    print(f"Totalt antal sålda enheter är: {total_units} st.")
    return total_units