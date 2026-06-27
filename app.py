import streamlit as st
from agents.researcher import generate_report
st.title("AI RESEARCH ASSISTANT")
topic = st.text_input("Enter the topic you want to research: ")
options = ["Short", "Medium", "Long"]
level = st.selectbox(label = "Choose the level: ", options = options, index = 1, placeholder = "Select an option.")
if st.button(label = "Generate Report"):
    st.write(f"Topic: {topic}")
    st.write(f"Level: {level}")
    with st.spinner("Generating report..."):
        st.header(topic)
        report = generate_report(topic, level)
        st.write(report)

    
