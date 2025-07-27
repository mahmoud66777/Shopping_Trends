# 🛍️ Shopping Analytics Dashboard

A comprehensive web-based analytics dashboard for shopping trends data analysis, built with Flask and interactive visualizations using Plotly.

![Dashboard Preview](static/dashboard-preview.png)

## 📊 Overview

This project provides an interactive dashboard to analyze shopping trends and customer behavior patterns. It features modern UI design, multiple chart types, and key performance indicators (KPIs) to help understand customer purchasing patterns, seasonal trends, and demographic insights.

## ✨ Features

### 📈 Interactive Visualizations
- **Sales by Category**: Horizontal bar chart showing average spending per item category
- **Age Distribution**: Histogram displaying customer age distribution by gender
- **Seasonal Trends**: Heatmap showing seasonal popularity of different item categories
- **Geographic Analysis**: Bar chart of top 10 customer locations
- **Payment Methods**: Donut chart showing preferred payment method distribution

### 🎯 Key Performance Indicators
- Total Revenue
- Total Orders
- Average Order Value

### 🎨 Modern UI/UX
- Responsive design with gradient backgrounds
- Glass-morphism effect cards
- Smooth animations and hover effects
- Professional color schemes using Plotly color palettes
- Mobile-friendly responsive layout

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly Express & Graph Objects
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design patterns
- **Database**: CSV file (easily extensible to SQL databases)

## 📁 Project Structure

```
shopping-analytics-dashboard/
├── app.py                 # Main Flask application
├── plotting_utils.py      # Chart generation utilities
├── requirements.txt       # Python dependencies
├── data/
│   └── shopping_trends.csv # Sample dataset
├── templates/
│   └── dashboard.html     # Main dashboard template
├── static/
│   └── myplot.png        # Static assets
├── notebook/
│   └── EDA_Shopping_Trends.ipynb # Exploratory data analysis
├── utils/
│   └── db_utils.py       # Database utilities
└── sql/
    └── connect_test.sql  # SQL connection tests
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/shopping-analytics-dashboard.git
   cd shopping-analytics-dashboard
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000` to view the dashboard

## 📊 Dataset Information

The dashboard uses a comprehensive shopping trends dataset with the following features:

- **Customer Demographics**: Age, Gender, Location
- **Purchase Details**: Item, Category, Purchase Amount, Season
- **Preferences**: Size, Color, Payment Method, Shipping Type
- **Behavior**: Review Rating, Previous Purchases, Frequency
- **Marketing**: Discount Applied, Promo Code Usage, Subscription Status

**Dataset Size**: 3,900+ customer records

## 🎨 Visualization Details

### 1. Sales by Category Analysis
- **Type**: Horizontal Bar Chart
- **Purpose**: Identify highest-revenue product categories
- **Color Scheme**: Viridis gradient for visual appeal

### 2. Customer Demographics
- **Type**: Age Distribution Histogram
- **Purpose**: Understand customer age distribution by gender
- **Insights**: Gender-based purchasing patterns

### 3. Seasonal Trends
- **Type**: Heatmap
- **Purpose**: Visualize seasonal popularity of item categories
- **Use Case**: Inventory planning and seasonal marketing

### 4. Geographic Distribution
- **Type**: Horizontal Bar Chart
- **Purpose**: Identify top customer locations
- **Color Scheme**: Plasma gradient

### 5. Payment Preferences
- **Type**: Donut Chart
- **Purpose**: Analyze preferred payment methods
- **Insights**: Payment infrastructure optimization

## 🔧 Customization

### Adding New Visualizations

1. **Create chart function** in `plotting_utils.py`:
   ```python
   def create_new_chart(df):
       fig = px.chart_type(df, ...)
       fig.update_layout(...)
       return fig
   ```

2. **Update Flask route** in `app.py`:
   ```python
   new_chart_html = pio.to_html(create_new_chart(df), full_html=False)
   ```

3. **Add to template** in `dashboard.html`:
   ```html
   <div class="chart-container">
       {{ new_chart_html | safe }}
   </div>
   ```

### Styling Modifications

- Modify CSS variables in `dashboard.html` for color schemes
- Adjust grid layouts for different screen sizes
- Customize animation timing and effects

## 📱 Responsive Design

The dashboard is fully responsive and optimized for:
- **Desktop**: Full-width multi-column layout
- **Tablet**: Adaptive grid system
- **Mobile**: Single-column stacked layout

## 🚀 Deployment Options

### Local Development
```bash
python app.py  # Development server
```

### Production Deployment
- **Heroku**: Deploy with Procfile
- **AWS**: Use Elastic Beanstalk or EC2
- **DigitalOcean**: App Platform deployment
- **Docker**: Containerized deployment

### Docker Setup (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📈 Future Enhancements

- [ ] Real-time data updates
- [ ] Advanced filtering and search
- [ ] Export functionality (PDF, Excel)
- [ ] User authentication and personalization
- [ ] Machine learning predictions
- [ ] Database integration (PostgreSQL, MongoDB)
- [ ] API endpoints for data access
- [ ] Dark/Light theme toggle

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset inspired by e-commerce analytics requirements
- UI design influenced by modern dashboard patterns
- Plotly.js for exceptional interactive visualizations
- Flask community for excellent documentation

## 🐛 Issues and Bug Reports

If you encounter any issues, please [create an issue](https://github.com/yourusername/shopping-analytics-dashboard/issues) with:
- Detailed description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

## 💬 Contact

- **Developer**: Mahmoud Ehab
- **Email**: mahmoud404ehab@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/mahmoud-ehab-430b01318/
- **Kaggle**: https://www.kaggle.com/mahmoudehab6677
