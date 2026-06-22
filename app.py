import streamlit as st
import pandas as pd

st.title("Restaurant Growth Analysis Dashboard")

st.write("Restaurant Growth Analysis using Business Analytics")

df = pd.read_csv("Final_Restaurant_Analysis (4).csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Summary Statistics")
st.write(df.describe())

st.success("Project deployed successfully using Streamlit")
