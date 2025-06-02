
# Sentiment Analysis & Business Intelligence Dashboard

This project provides a data-driven sentiment analysis dashboard using **Streamlit** and **TextBlob**, analyzing reviews of fertility clinics across Ontario. It supports both **competitive benchmarking** and **quality assurance** for clinic performance using patient review data.

## Features

- Sentiment scoring from real patient review summaries
- Positive and negative phrase extraction for root cause analysis
- Interactive bar charts and tables (Plotly, Streamlit)
- Integrated top review platforms: RateMDs, Google, Yelp, etc.
- Auto-updated sentiment trends and insights

## Technologies Used

- Python 3.10+
- Streamlit
- TextBlob (NLP)
- Plotly (visualizations)
- Pandas

## 🗂Directory Structure

```
Sentiment-Analysis-BI-Dashboard/
├── app.py                  # Main Streamlit app
├── cleaned_appointment.csv # Optional dataset (if not private)
├── reviews_sample.json     # Optional: preloaded JSON of reviews
├── requirements.txt        # Required Python packages
├── README.md               # Project description and instructions
└── assets/                 # Optional: logos, screenshots
```

##  How to Run the App

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/Sentiment-Analysis-BI-Dashboard.git
cd Sentiment-Analysis-BI-Dashboard

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

## Data Sources

- Google Maps Reviews  
- RateMDs  
- Yelp Canada  
- Birdeye  
- FertilityMapper  
- NewLife Fertility Testimonials  
(And 15+ other trusted Canadian review sites)

## Potential Users
- Health Care Executives 
- Business Analysts in Healthcare
- Fertility Clinic Managers
- Patient Experience Researchers
- Competitive Intelligence Teams

## License

MIT License
