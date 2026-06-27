import requests
import streamlit as st

st.title("Temperature Checker")
city = st.text_input("Enter the city to check temperature: ")
if city:
    try:
        with st.spinner("Fetching weather..."):
            r = requests.get("https://api.weatherapi.com/v1/current.json?", params = {'key': "a069cc622063427abd692423261806", 'q' : city})
            r_dict = r.json()
            temp = r_dict['current']['temp_c']
            condition = r_dict['current']['condition']['text']
        st.metric(label = f"Temperature of {city}:", value = f"{temp}")
        st.write(f"Condition of {city}:", condition)
    except:
        st.error("Could not retrieve the weweather data. Please check the city name or your connection.")