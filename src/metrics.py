import pandas as pd

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

#AOV (Average Order Value) /Tobias




# Top-3 kategorier efter intäkt (eventuella avvikelser) /Tobias