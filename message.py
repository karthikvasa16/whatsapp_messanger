import streamlit as st
import pywhatkit

# Streamlit app title
st.title("WhatsApp Message Sender")

# Input fields for user to enter mobile number and message
mobile_number = st.text_input("Enter the recipient's mobile number (with country code):", "+91")
message = st.text_area("Enter the message you want to send:")

# Input fields for time (hours and minutes)
hour = st.number_input("Enter the hour (24-hour format):", min_value=0, max_value=23, value=10)
minute = st.number_input("Enter the minute:", min_value=0, max_value=59, value=55)

# Button to send the message
if st.button("Send WhatsApp Message"):
    try:
        # Sending message using pywhatkit
        pywhatkit.sendwhatmsg(mobile_number, message, hour, minute)
        st.success("Message successfully sent!")

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

