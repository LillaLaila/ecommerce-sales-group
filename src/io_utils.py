import pandas as pd

def load_data(path="data/ecommerce_sales.csv"):

    df = pd.read_csv(path)
    
    return df

if __name__ == "__main__":
    df = load_data()
   
    df.info() # inga NaN värden eller tomma rader

    print(df.head())