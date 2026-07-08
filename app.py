import streamlit as st
from agents.report_generator import generate_report
from tools.search_tool import search
st.title("AI RESEARCH ASSISTANT")
topic = st.text_input("Enter the topic you want to research: ")
options = ["Short", "Medium", "Long"]
level = st.selectbox(label = "Choose the level: ", options = options, index = 1, placeholder = "Select an option.")
if st.button(label = "Generate Report"):
    st.write(f"Topic: {topic}")
    st.write(f"Level: {level}")
    if (not st.write()):
        st.warning("Please enter a topic.")
    with st.spinner("""🔍 Searching trusted sources...
                        🧠 Analyzing information...
                        📝 Writing report..."""):
        report, search_results = generate_report(topic, level)
        st.markdown(report)
        st.subheader("Sources")
        for i, source in enumerate(search_results, start=1):
            st.markdown(f"### {i}. {source['title']}")
            st.markdown(f"**URL:** {source['url']}")
            st.write(source["content"][:180] + "...")
            st.divider()


    
