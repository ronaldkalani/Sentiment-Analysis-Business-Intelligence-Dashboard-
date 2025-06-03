## AI/ML Project Title: Fertility Clinic Sentiment Intelligence Dashboard

# Goal:
Transform qualitative patient reviews into structured sentiment analytics to support clinic optimization and strategic planning.

# Intended Audience:
- Healthcare Executives & Clinic Managers
- Data Scientists & Business Intelligence Analysts
- Patient Experience & Marketing Teams

# Strategy & Pipeline Steps:
1. Data Collection from 20+ review platforms
2. NLP-based Sentiment Scoring using TextBlob
3. Feature Extraction: Themes and Polarity
4. Sentiment Aggregation per Clinic
5. Dashboard Development in Streamlit
6. Strategic Insights Generation

# Challenges:
- Review subjectivity and tone variance
- Small sample bias across locations
- Real-time feedback integration
- Linking sentiment to operational KPIs

# Problem Statement:
Fertility clinics receive feedback across many online platforms, but they lack a unified sentiment analysis system. This project extracts actionable business insights from review text to inform service design, communication strategy, and patient experience optimization.

# Dataset:
Simulated reviews (7–10 per clinic) sourced from RateMDs, Google Reviews, Yelp, and fertility forums.

# MACHINE LEARNING PREDICTION & OUTCOMES
--------------------------------------
- Avg. Sentiment Score per Clinic
- Positive/Negative Theme Identification
- Ranking by Sentiment
- Strategic Flags: Underperforming Clinics
- No-show Prediction Support

# Business Decision Support – Actionable Insights from Sentiment Analytics
------------------------------------------------------------------------

| Clinic                        | Avg. Sentiment | Reviews |
|------------------------------|----------------|---------|
| Pollin Fertility             | 0.38           | 9       |
| NewLife - Hamilton           | 0.36           | 7       |
| NewLife - Richmond Hill      | 0.34           | 9       |
| Hannam Fertility Centre      | 0.32           | 7       |
| Ottawa Fertility Centre      | 0.29           | 7       |
| NewLife - Oakville           | 0.24           | 7       |
| NewLife - Mississauga        | 0.23           | 10      |
| NewLife - Concord            | 0.23           | 8       |
| NewLife - Burlington         | 0.19           | 9       |
| NewLife - Brampton           | 0.14           | 9       |
| NewLife - Scarborough        | 0.13           | 7       |
| NewLife - Milton             | 0.12           | 8       |
| TRIO Fertility               | 0.03           | 9       |
| NewLife - Toronto Downtown   | -0.20          | 7       |


## Strategic Business Implications for NewLife Fertility Clinics

1. Location Benchmarking & Prioritization
Top-performing NewLife locations (Hamilton, Richmond Hill, Oakville) exhibit strong sentiment associated with keywords like "supportive," "excellent," and "great care."
Lower-performing sites (Toronto Downtown, Milton, Scarborough) show sentiment gaps due to reception issues, communication delays, or perceived inefficiencies.
✅ Action: Conduct service audits, retrain front-line staff, and replicate high-performing clinic strategies at underperforming branches.

2. Resource Allocation
Clinics like Brampton, Burlington, and Toronto Downtown receive high traffic but lower sentiment, indicating potential patient dissatisfaction.
✅ Action: Reassign senior staff, enhance clinic support capacity, and implement automated intake tools (chatbots, self-check-in systems).

3. Service Design Optimization
Positive Themes: “Clean environment,” “kind staff,” “modern clinic,” “great IVF success.”
Negative Themes: “Long wait times,” “billing issues,” “rude receptionist,” “unclear communication.”
✅ Action: Deploy AI-powered scheduling tools and SMS reminders to reduce wait times.
          - Provide clarified billing guides and multilingual support.

4. Marketing & Reputation Management
Promote high-rated clinics like Hamilton, Richmond Hill, Mississauga in digital campaigns.
Launch reputation recovery programs for Toronto Downtown, including responding to reviews, showcasing new initiatives, and targeted ads.
✅ Action: Use sentiment keywords like “modern IVF care,” “supportive staff,” “great experience” in your clinic website, Google Business posts, and paid ads.

5. Predictive Analytics for No-Show Risk
Combine sentiment score, satisfaction rating, and location-level performance to predict no-show likelihood.

✅ Action: Identify patients likely to miss appointments and provide reminder calls, telehealth options, or personalized outreach.

6. Executive Dashboards: Monitor KPI trends with Tableau or Streamlit.

# Trailer Documentation:
- Libraries: Streamlit, Plotly, TextBlob, Pandas
- Data Type: Simulated reviews (text)
- Deployment: Streamlit Cloud or local

# Conceptual Enhancement – AGI:
Future potential includes:
- EMR-integrated insights
- Auto-generated satisfaction diagnostics
- Ethical AI feedback systems

# Developer: 
           # Ronald Kalani, Master of Science in Technology Management (MSc), Graduate Certificates (GC) in Artificial Intelligence, Regulatory Affairs, and Bioinformatics

