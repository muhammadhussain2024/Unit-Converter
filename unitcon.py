import streamlit as st
import time

# Set page title and a more engaging theme
st.set_page_config(page_title="Unit Converter App 🌎", page_icon="🌍", layout="wide")

# Title with some fun styling
st.markdown("""
    <h1 style="text-align:center; color: #4CAF50;">🌎 **Unit Converter App** 🌍</h1>
    <h3 style="text-align:center; color: #ff6347;">Converts Length, Weight, and Time Instantly with a Fun Twist! 🎉</h3>
    <p style="text-align:center; font-size:18px; color: #4682b4;">Welcome! Select a category, Enter the value, and get the result real-time 🚀</p>
""", unsafe_allow_html=True)

# Category Selection with some more interactive styling
category = st.selectbox("Choose a category 🌟", ["Length 📏", "Weight ⚖", "Time ⏳"])

# Dynamic content based on selected category
if category == "Length 📏":
    unit = st.selectbox("Select Conversion 📍", ["Kilometers to miles", "Miles to kilometers"])
    st.markdown("<h4 style='color: #32cd32;'>Enter the value in Kilometers or Miles for conversion</h4>", unsafe_allow_html=True)
elif category == "Weight ⚖":
    unit = st.selectbox("Select Conversion ⚖️", ["Kilograms to pounds", "Pounds to kilograms"])
    st.markdown("<h4 style='color: #ff4500;'>Enter the value in Kilograms or Pounds for conversion</h4>", unsafe_allow_html=True)
elif category == "Time ⏳":
    unit = st.selectbox("Select Conversion ⏰", [
        "Seconds to minutes", "Minutes to seconds",
        "Minutes to hours", "Hours to minutes",
        "Hours to day", "Days to hours"
    ])
    st.markdown("<h4 style='color: #1e90ff;'>Enter the value in Seconds, Minutes, Hours, or Days</h4>", unsafe_allow_html=True)

# Number input field with a friendly hint
value = st.number_input("Enter the value to convert 💡", min_value=0.0, help="This is the number you want to convert! ✨", format="%.2f")

# Conversion function remains the same
def convert_units(category, value, unit):
    if category == "Length 📏":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
    elif category == "Weight ⚖":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
    elif category == "Time ⏳":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to day":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

# Add a cool loading spinner for conversion
if st.button("🚀 Convert!"):
    if value > 0:
        with st.spinner("Converting... Please wait! ⏳"):
            time.sleep(1)  # Simulate some processing time
            result = convert_units(category, value, unit)
            st.success(f"🎉 The result is **{result:.2f}** 🏆")

            # Show a fun message only after a successful conversion
            st.markdown("""
                <h3 style="text-align:center; color: #20b2aa;">🎉 You just converted something amazing! Keep experimenting with different values 🌟</h3>
                <p style="text-align:center; font-size:16px; color: #808080;">Unit conversion is fun. Let's make math feel like magic! 🔮</p>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a valid number greater than 0!")
