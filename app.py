
import streamlit as st
import pandas as pd
from recommend import recommend_products

df = pd.read_csv(r"C:\Users\REETE\Desktop\rs\products.csv")

st.title("🛍️ Product Recommendation System")
product = st.selectbox("Select a Product", df['name'].tolist())

if st.button("Recommend Similar Products"):
    recs = recommend_products(product)
    st.subheader("You may also like:")
    for r in recs:
        st.write("👉", r)
