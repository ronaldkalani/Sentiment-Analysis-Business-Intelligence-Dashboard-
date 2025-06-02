import streamlit as st
import pandas as pd
from textblob import TextBlob
import plotly.express as px
from collections import Counter
from datetime import date

# --- Streamlit Setup ---
st.set_page_config(page_title="Fertility Clinic Sentiment Dashboard", layout="wide")
st.title("🧬 Fertility Clinic Sentiment Analysis Dashboard")
st.markdown("Compare sentiment across 10 NewLife Fertility locations and top-rated Ontario fertility clinics based on review summaries.")
today = date.today().strftime("%B %d, %Y")

# --- Sample Reviews (Expanded with Trusted Sources)
clinic_reviews = {
    "NewLife - Mississauga": [
        "Great service", "Very helpful staff", "Wait times were long", "Clinic was overcrowded", "Doctors were kind",
        "Felt rushed", "IVF was successful", "Receptionist was rude", "Follow-up was delayed", "Clean and modern space"
    ],
    "NewLife - Brampton": [
        "Clean environment", "Felt rushed", "Staff were not responsive", "Very professional", "Consultation was rushed",
        "Comfortable experience", "Billing was confusing", "Good communication", "Waiting time was too long"
    ],
    "NewLife - Burlington": [
        "Efficient and friendly", "Receptionist was cold", "Top IVF doctors", "Doctors were great", "Too crowded",
        "Felt neglected", "Average communication", "Happy with results", "Not enough support"
    ],
    "NewLife - Richmond Hill": [
        "Supportive nurses", "Excellent consultation", "Rescheduled multiple times", "Doctors didn’t explain well",
        "Very busy", "Clean facility", "Rushed visit", "Positive pregnancy", "Great front desk"
    ],
    "NewLife - Milton": [
        "Very caring staff", "Bit expensive", "Always on time", "Felt dismissed", "Good consultation",
        "Friendly nurses", "Doctor was impatient", "Clean clinic"
    ],
    "NewLife - Concord": [
        "Fast and reliable", "Too crowded", "Doctors lacked empathy", "Staff was great", "Not very responsive",
        "Wonderful lab", "Long wait", "No personal attention"
    ],
    "NewLife - Scarborough": [
        "Very attentive", "Organized and clean", "Parking was difficult", "Staff seemed rushed", "Supportive team",
        "Doctor didn’t listen", "Clinic location was noisy"
    ],
    "NewLife - Toronto (Downtown)": [
        "Modern facilities", "Helpful from start to finish", "Receptionist was rude", "Bad experience with nurse",
        "No proper follow-up", "Felt supported", "Doctor was cold"
    ],
    "NewLife - Oakville": [
        "Professional, well-equipped", "Nurses were rushed", "Great care", "Had to wait 40 minutes", "Lab was delayed",
        "Happy with service", "Felt rushed by doctor"
    ],
    "NewLife - Hamilton": [
        "Exceptional care", "Felt heard", "Clinic was far", "Staff was very kind", "No privacy during consultation",
        "Doctors were excellent", "Receptionist seemed untrained"
    ],
    "TRIO Fertility": [
        "Highly professional", "Long waitlist but worth it", "Caring staff", "Organized system", "Expensive",
        "Strong outcomes", "Friendly staff", "Felt prioritized", "Hard to get appointment"
    ],
    "Pollin Fertility": [
        "Great experience with Dr. Taerk", "Beautiful clinic", "Quick responses", "Staff are supportive and caring",
        "Appointments were on time", "Booking appointments was easy", "Access to blood results was quick",
        "Clinic is very busy on Mondays and Fridays", "Wait times improved over time"
    ],
    "Ottawa Fertility Centre": [
        "Awesome clinic", "Staff were welcoming and helpful", "Diverse and friendly team", "Efficient processes",
        "Positive first impressions", "Quick appointment scheduling", "Clear explanations from doctors"
    ],
    "Hannam Fertility Centre": [
        "Exceptional service", "Warm and friendly staff", "Minimal wait times", "Clean and organized facility",
        "Highly professional doctors", "Supportive team", "Positive experiences with IVF treatments"
    ]
}

# --- Sentiment and Feature Extraction ---
def analyze_sentiment(text_list):
    scores = [TextBlob(text).sentiment.polarity for text in text_list]
    return round(sum(scores) / len(scores), 2), len(scores)

def extract_features(reviews, polarity_type="positive"):
    phrases = []
    for review in reviews:
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        if polarity_type == "positive" and polarity > 0:
            phrases.extend(blob.noun_phrases)
        elif polarity_type == "negative" and polarity < 0:
            phrases.extend(blob.noun_phrases)
    return [phrase for phrase, _ in Counter(phrases).most_common(2)]

# --- Process Data ---
results = []
positive_features = {}
negative_features = {}

for clinic, reviews in clinic_reviews.items():
    avg_score, count = analyze_sentiment(reviews)
    positives = extract_features(reviews, "positive")
    negatives = extract_features(reviews, "negative")
    
    results.append({
        "Clinic": clinic,
        "Avg Sentiment Score": avg_score,
        "Review Count": count,
        "Date Reported": today
    })
    positive_features[clinic] = positives
    negative_features[clinic] = negatives

df_sentiment = pd.DataFrame(results).sort_values(by="Avg Sentiment Score", ascending=False)

# --- Display Table ---
st.subheader("📋 Sentiment Score Table")
st.dataframe(df_sentiment, use_container_width=True)

# --- Bar Chart ---
st.subheader("📊 Sentiment Comparison Chart")
fig = px.bar(
    df_sentiment,
    x="Clinic",
    y="Avg Sentiment Score",
    color="Clinic",
    color_discrete_sequence=px.colors.qualitative.Set3,
    title="Average Sentiment Score by Clinic"
)
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)

# --- What Clinics Did Best ---
st.subheader("✅ What Clinics Did Best (Positive Mentions)")
for clinic in df_sentiment["Clinic"]:
    pos = positive_features.get(clinic, [])
    st.markdown(f"**{clinic}**: Known for *{', '.join(pos) if pos else 'no clear strengths mentioned'}*.")

# --- Common Complaints ---
st.subheader("⚠️ Common Patient Complaints (Negative Mentions)")
for clinic in df_sentiment["Clinic"]:
    neg = negative_features.get(clinic, [])
    st.markdown(f"**{clinic}**: Common concerns include *{', '.join(neg) if neg else 'no significant complaints detected'}*.")

# --- Top 20 Review Sources ---
st.subheader("🔗 Top 20 Review Sources Used")
review_sites = [
    "1. [RateMDs](https://www.ratemds.com/)",
    "2. [Yelp Canada](https://www.yelp.ca/)",
    "3. [Birdeye](https://birdeye.com/)",
    "4. [Reddit IVF Threads](https://www.reddit.com/r/IVF/)",
    "5. [Fertility Mapper](https://fertilitymapper.com/)",
    "6. [NewLife Fertility Testimonials](https://newlifefertility.com/testimonials/)",
    "7. [ReviewedToronto](https://www.reviewedtoronto.com/)",
    "8. [TheBestToronto](https://www.thebesttoronto.com/)",
    "9. [Facebook Reviews](https://www.facebook.com/)",
    "10. [Google Maps Reviews](https://www.google.com/maps)",
    "11. [Trustpilot](https://www.trustpilot.com/)",
    "12. [BBB Canada](https://www.bbb.org/ca/)",
    "13. [IVF.ca Clinic Finder](https://ivf.ca/forums/page/clinicfinder.html)",
    "14. [Healthgrades](https://www.healthgrades.com/)",
    "15. [Zocdoc](https://www.zocdoc.com/)",
    "16. [MDreview](https://mdreview.com/)",
    "17. [N49 Reviews](https://www.n49.com/)",
    "18. [Canada411 Reviews](https://www.canada411.ca/)",
    "19. [Clinic Advisor](https://www.clinicadvisor.com/)",
    "20. [Top Doctors Canada](https://www.topdoctors.ca/)"
]

for site in review_sites:
    st.markdown(site)







