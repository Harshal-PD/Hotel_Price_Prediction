import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load("models/hotel_price_model.pkl")

st.title("🏨 Hotel Room Price Predictor")

# User inputs
lead_time = st.slider("Lead Time (days)", 0, 365, 30)
stay_duration = st.slider("Stay Duration (nights)", 1, 30, 2)
total_guests = st.slider("Total Guests", 1, 10, 2)

meal = st.selectbox("Meal Plan", ["BB", "HB", "FB", "SC"])
market_segment = st.selectbox("Market Segment", ["Online TA", "Offline TA/TO", "Direct", "Groups", "Corporate"])
assigned_room_type = st.selectbox("Assigned Room Type", ["A", "B", "C", "D", "E", "F", "G", "H", "L", "P"])
booking_changes = st.slider("Booking Changes", 0, 10, 0)

# 👉 Add Room View (optional)
room_view = st.selectbox("Room View", ["Inside", "Outside"])

# Map string inputs to numeric if needed
meal_map = {"BB": 0, "HB": 1, "FB": 2, "SC": 3}
market_segment_map = {"Online TA": 0, "Offline TA/TO": 1, "Direct": 2, "Groups": 3, "Corporate": 4}
assigned_room_type_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "L": 8, "P": 9}
room_view_map = {"Resort Hotel": 0, "City Hotel": 1}

# Create input dataframe
input_data = pd.DataFrame([{
    "lead_time": lead_time,
    "stay_duration": stay_duration,
    "total_guests": total_guests,
    "meal": meal_map[meal],
    "market_segment": market_segment_map[market_segment],
    "assigned_room_type": assigned_room_type_map[assigned_room_type],
    "booking_changes": booking_changes,
    # Optional if your model needs it:
    # "room_view": room_view_map[room_view],
}])

if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)[0]
        
        
        st.success(f"💵 Predicted Price: ${prediction:.2f} (RandomForest)")
    except Exception as e:
        st.error(f"Error: {e}")
