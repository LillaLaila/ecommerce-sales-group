import pandas as pd
import matplotlib.pyplot as plt

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
   