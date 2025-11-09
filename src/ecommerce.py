from src import io_utils, metrics, viz

class EcommerceAnalyzer:
    def __init__(self, data=None):
        self.data= data

    def load_data(self):
        df = io_utils.load_data()
        return df

    def top_3(self, df):
       top_3 = metrics.top_3(df)
       return top_3
    
    def mean(self, df):
        mean = metrics.mean(df)
        return mean
    
    def intaktStad(self, df):
        intaktperStad = metrics.intaktStad(df)
        return intaktperStad
    
    def barKategori(self, df):
        barChartKategori = viz.barKategori(df)
        return barChartKategori
    
    def barStader(self, df):
        barChartStader = viz.barStader(df)
        return barChartStader
    
    
    def total_revenue(self, df):
        return metrics.total_revenue(df)
    
    def total_units(self, df):
        return metrics.total_units(df)