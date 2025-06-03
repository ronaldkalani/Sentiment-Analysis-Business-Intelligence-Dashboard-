
# 🧬 Fertility Clinic Sentiment Intelligence Dashboard

## Goal
This project aims to build an interactive sentiment analysis dashboard that evaluates patient experiences across multiple fertility clinics in Ontario using natural language processing (NLP). It translates unstructured patient reviews into actionable business intelligence to support operational, clinical, and strategic decision-making.

## Intended Audience
- **Healthcare Executives & Operations Managers:** To optimize clinic performance and patient satisfaction.
- **Data Scientists & BI Analysts:** To apply NLP techniques for real-world sentiment analytics.
- **Marketing Teams:** To monitor brand reputation and patient perception trends.
- **Clinic Managers:** To benchmark services across locations and initiate targeted improvements.

## Strategy & Pipeline Steps
1. **Data Collection**  
   Aggregated reviews from 20+ trusted public review platforms such as RateMDs, Yelp, and Google Reviews.
2. **Text Preprocessing**  
   Utilized TextBlob to clean and extract polarity scores and noun phrases from reviews.
3. **Sentiment Scoring**  
   Assigned polarity scores (range: -1 to +1) to each clinic based on the average of review sentiments.
4. **Feature Extraction**  
   Extracted top positive and negative themes from noun phrases to summarize perceived strengths and weaknesses.
5. **Visualization**  
   Built a Streamlit dashboard with sentiment tables, bar plots (Plotly), and strategic insight blocks.
6. **Strategic Mapping**  
   Embedded AI-driven decision support recommendations (location benchmarking, resource allocation, service optimization, etc.).

## Challenges
- **Unstructured Data Variability:** Differing review lengths and informal language required robust NLP handling.
- **Small Sample Bias:** Limited reviews per clinic may lead to skewed sentiment scores if not interpreted cautiously.
- **Subjectivity of Reviews:** Sentiment may not always correlate with clinical outcomes, requiring contextual interpretation.
- **Real-time Integration:** Integrating live review feeds and auto-refresh pipelines remains a future enhancement.

## Problem Statement
Patients' perception of care across fertility clinics significantly impacts trust, satisfaction, and retention. However, healthcare systems often lack tools to consolidate and analyze this feedback. This project solves this by turning fragmented, qualitative review data into structured business intelligence for NewLife Fertility and its competitors.

## Dataset
Simulated patient reviews sourced and aggregated from:
- Google Maps
- RateMDs
- Yelp
- Fertility Mapper
- Reddit IVF threads
- Facebook, etc.

Each clinic has ~7–10 reviews represented in natural language format.

## MACHINE LEARNING PREDICTION & OUTCOMES
- **Sentiment Score Calculation:** Average polarity per clinic
- **Positive & Negative Theme Extraction:** Top 2 noun phrases with extreme polarity
- **Benchmarking Output:** Sentiment-ranked comparison of 10+ clinics
- **Operational Flagging:** Clinics with low sentiment/high traffic highlighted for intervention
- **Business Recommendations:** Generated directly from insights

| Clinic                     | Avg. Sentiment Score | Review Count |
|---------------------------|----------------------|--------------|
| Pollin Fertility          | 0.38                 | 9            |
| NewLife - Hamilton        | 0.36                 | 7            |
| NewLife - Richmond Hill   | 0.34                 | 9            |
| Hannam Fertility Centre   | 0.32                 | 7            |
| Ottawa Fertility Centre   | 0.29                 | 7            |
| NewLife - Toronto (Downtown) | -0.20              | 7            |

## Trailer Documentation
- **Framework:** Streamlit (UI), Plotly (visualization), TextBlob (sentiment engine), Pandas (data wrangling)
- **UI Features:**
  - Interactive sentiment bar chart by clinic
  - Real-time KPI table
  - Positive/Negative themes per clinic
  - Top 20 data sources listed
  - Executive strategy summary
- **Deployment:** Localhost or Streamlit Cloud

## Conceptual Enhancement – AGI (Artificial General Intelligence)
This project lays foundational work in AI decision support systems within healthcare. A potential AGI-inspired evolution may include:
- Autonomous reasoning agents that adapt responses based on longitudinal patient satisfaction trends.
- Cross-system integration (EMRs, surveys, social reviews) for holistic patient insight.
- Ethical decision frameworks to avoid bias from subjective sentiment.

## References
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [Streamlit](https://streamlit.io/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [20+ Review Platforms](#top-20-review-sources-used)

> **Developed by:** Ronald Kalani  
> **Repository:** [AI Fertility BI Dashboard](https://github.com/ronaldkalani/ai-fertility-bi-dashboard)  
> **Status:** MVP Prototype (Future Work: Auto-fetch reviews, expand clinic data, integrate appointment logs)
