import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def create_sales_by_category_chart(df):
    """Creates a horizontal bar chart of average spending by item category."""
    avg_spend = df.groupby('Item Purchased')['Purchase Amount (USD)'].mean().sort_values(ascending=False).reset_index()
    
    fig = px.bar(
        avg_spend,
        y='Item Purchased',
        x='Purchase Amount (USD)',
        title='Average Spend per Item Category',
        orientation='h',
        template='plotly_white',
        color='Purchase Amount (USD)',
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(
        height=600,
        showlegend=False,
        title_font_size=18,
        title_x=0.5
    )
    
    return fig

def create_age_distribution_chart(df):
    """Creates an age distribution chart by gender."""
    fig = px.histogram(
        df,
        x='Age',
        color='Gender',
        nbins=20,
        title='Age Distribution by Gender',
        template='plotly_white',
        color_discrete_sequence=['#FF6B6B', '#4ECDC4']
    )
    
    fig.update_layout(
        height=400,
        title_font_size=18,
        title_x=0.5,
        bargap=0.1
    )
    
    return fig

def create_seasonal_heatmap(df):
    """Creates a heatmap showing seasonal popularity of items."""
    seasonal_data = pd.crosstab(df['Item Purchased'], df['Season'])
    seasonal_data = seasonal_data[['Spring', 'Summer', 'Fall', 'Winter']]
    
    fig = go.Figure(data=go.Heatmap(
        z=seasonal_data.values,
        x=seasonal_data.columns,
        y=seasonal_data.index,
        colorscale='YlGnBu',
        showscale=True
    ))
    
    fig.update_layout(
        title='Seasonal Popularity of Item Categories',
        height=500,
        title_font_size=18,
        title_x=0.5
    )
    
    return fig

def create_top_locations_chart(df):
    """Creates a bar chart of top 10 customer locations."""
    top_locations = df['Location'].value_counts().nlargest(10).reset_index()
    top_locations.columns = ['Location', 'Count']
    
    fig = px.bar(
        top_locations,
        x='Count',
        y='Location',
        title='Top 10 Customer Locations',
        orientation='h',
        template='plotly_white',
        color='Count',
        color_continuous_scale='plasma'
    )
    
    fig.update_layout(
        height=500,
        showlegend=False,
        title_font_size=18,
        title_x=0.5
    )
    
    return fig

def create_payment_methods_chart(df):
    """Creates a donut chart of preferred payment methods."""
    payment_counts = df['Preferred Payment Method'].value_counts()
    
    fig = px.pie(
        values=payment_counts.values,
        names=payment_counts.index,
        title='Preferred Payment Methods',
        template='plotly_white',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig.update_layout(
        height=400,
        title_font_size=18,
        title_x=0.5
    )
    
    return fig