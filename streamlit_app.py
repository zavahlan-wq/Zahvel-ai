import streamlit as st
from google import genai

st.set_page_config(page_title="Zahvel AI Engineering Assistant", page_icon="⚡")

st.title("⚡ Zahvel AI Engineering Assistant")
st.write("Test our real-time AI assistant for data architecture, SQL optimization, and workflow automation.")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

task_type = st.selectbox(
    "Select Engineering Mode",
    [
        "Data & SQL Query Optimization",
        "Workflow Automation Design",
        "System Architecture & Bottleneck Fix",
        "Business Data Summary"
    ]
)

user_input = st.text_area(
    "Describe your data, SQL, or workflow challenge",
    height=150,
    placeholder="Example: Our daily sales report SQL query takes 4 minutes to run on 50 million rows..."
)

if st.button("Generate Engineering Solution", type="primary"):
    if not user_input.strip():
        st.warning("Please enter a question, dataset snippet, or workflow problem first.")
    else:
        with st.spinner("Analyzing technical challenge..."):
            prompt = (
                f"You are an expert Analytical & Systems Engineer at Zavahlan Company Ltd. (Zahvel.com). "
                f"Task: {task_type}.\n\n"
                f"Provide a clear, practical, technical solution for:\n{user_input}"
            )
            response = None
            last_error = ""
            for model_name in ["gemini-flash-latest", "gemini-2.5-flash-lite", "gemini-3.8-flash"]:
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=prompt,
                    )
                    break
                except Exception as e:
                    last_error = str(e)
                    continue

            if response:
                st.markdown("### Engineering Solution")
                st.write(response.text)
            else:
                st.info("Our AI servers are currently experiencing heavy traffic. Please wait 10 seconds and click Generate again.")
