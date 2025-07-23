# app/charts.py
import pandas as pd
import matplotlib.pyplot as plt

def generate_chart(q):
    if "sales" in q.lower():
        df = pd.read_sql("SELECT * FROM total_sales", engine)
        df.plot(x='product_id', y='total_sales', kind='bar')
        path = "demo/sales_chart.png"
        plt.savefig(path)
        return path
    return "No chart available"
