import streamlit as st
import pandas as pd
from scraper import scrape_books

st.set_page_config(
    page_title="Advanced Web Scraper",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 E-Commerce Web Scraper")
st.write("Scrape product information and export as CSV")

st.markdown("---")

pages = st.slider(
    "Select Number of Pages to Scrape",
    1,
    5,
    2
)

if st.button("Start Scraping 🚀"):

    progress = st.progress(0)
    status = st.empty()

    data = []

    for i in range(1, pages+1):

        status.text(f"Scraping Page {i}...")
        page_data = scrape_books(i)

        data.extend(page_data)

        progress.progress(i/pages)

    st.success("Scraping Completed Successfully ✅")

    df = pd.DataFrame(data)

    st.subheader("Scraped Products")

    st.dataframe(df, use_container_width=True)

    st.write("Total Products:", len(df))

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "Download CSV 📥",
        csv,
        "products.csv",
        "text/csv"
    )
