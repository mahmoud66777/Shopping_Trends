from flask import Flask, render_template
import pandas as pd
import plotly.io as pio
from plotting_utils import (
    create_sales_by_category_chart,
    create_age_distribution_chart,
    create_seasonal_heatmap,
    create_top_locations_chart,
    create_payment_methods_chart
)

app = Flask(__name__)

@app.route('/')
def dashboard():
    df = pd.read_csv('data/shopping_trends.csv')
    
    # Calculate KPIs
    total_sales = df['Purchase Amount (USD)'].sum()
    total_purchases = len(df)
    avg_purchase = df['Purchase Amount (USD)'].mean()
    
    # Create multiple charts
    sales_fig = create_sales_by_category_chart(df)
    age_fig = create_age_distribution_chart(df)
    seasonal_fig = create_seasonal_heatmap(df)
    locations_fig = create_top_locations_chart(df)
    payment_fig = create_payment_methods_chart(df)
    
    # Convert figures to HTML
    sales_html = pio.to_html(sales_fig, full_html=False, div_id="sales-chart")
    age_html = pio.to_html(age_fig, full_html=False, div_id="age-chart")
    seasonal_html = pio.to_html(seasonal_fig, full_html=False, div_id="seasonal-chart")
    locations_html = pio.to_html(locations_fig, full_html=False, div_id="locations-chart")
    payment_html = pio.to_html(payment_fig, full_html=False, div_id="payment-chart")

    return render_template('dashboard.html', 
                         total_sales=f"${total_sales:,.2f}",
                         total_purchases=f"{total_purchases:,}",
                         avg_purchase=f"${avg_purchase:.2f}",
                         sales_html=sales_html,
                         age_html=age_html,
                         seasonal_html=seasonal_html,
                         locations_html=locations_html,
                         payment_html=payment_html)

if __name__ == '__main__':
    app.run(debug=True)