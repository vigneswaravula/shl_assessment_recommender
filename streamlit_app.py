import streamlit as st
import requests
import pandas as pd

API_URL ="https://shl-assessment-recommender-backend.onrender.com/recommend"

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")
st.title("🔍 SHL Assessment Recommender")

query = st.text_area("Enter your assessment needs in plain English:", height=100)

if st.button("Recommend"):
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Getting recommendations..."):
            try:
                response = requests.post(API_URL, json={"query": query})
                data = response.json()
                recs = data.get("recommendations", [])

                if not recs:
                    st.info("No suitable recommendations found.")
                else:
                    # Removed the st.write(recs) line here, as we only want to display the formatted table

                    # Update the column names based on the actual fields in 'recs'
                    df = pd.DataFrame(recs)
                    
                    # Check the columns of 'recs' and adjust accordingly
                    if "duration" not in df.columns:
                        df = df[["name", "type", "remote_support", "adaptive_support", "url"]]
                        df.columns = ["Name", "Type", "Remote Support", "Adaptive", "Link"]
                    else:
                        df = df[["name", "type", "duration", "remote_support", "adaptive_support", "url"]]
                        df.columns = ["Name", "Type", "Duration", "Remote Support", "Adaptive", "Link"]

                    # Convert the links to clickable hyperlinks
                    df['Link'] = df['Link'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')

                    st.success("Here are your recommended assessments:")
                    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
