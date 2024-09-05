import streamlit as st
import pandas as pd
import plotly.express as px

# Read Excel file from GitHub
df = pd.read_excel("https://raw.githubusercontent.com/Mirwais-Farahi/lta-datasets/main/dataset.xlsx")

st.set_page_config(
    page_title='Real-Time Survey Dashboard',
    page_icon=':bar_chart:',
    layout='wide'
)

# Dashboard title
st.title("Real-Time / Live Survey Dashboard")

# Top-level filters
project_symbol_filter = st.selectbox("Select Project Symbol", pd.unique(df['project_symbol']))
assistance_type_filter = st.selectbox("Select Assistance Type", pd.unique(df['assistance_type']))

# Dataframe filter
df_filtered = df[(df['project_symbol'] == project_symbol_filter) & (df['assistance_type'] == assistance_type_filter)]

# Display total number of surveys in each district and province
district_summary = df_filtered.groupby(['district', 'province']).size().reset_index(name='Number of Surveys')
st.markdown("### Total Surveys by District")
st.write(district_summary)

# Create a visualization of surveys by district
fig_district = px.bar(district_summary, x='district', y='Number of Surveys', color='province', title="Surveys by District")
st.write(fig_district)

# Count number of surveys each enumerator collected
enumerator_summary = df_filtered['respondent_name'].value_counts().reset_index()
enumerator_summary.columns = ['Enumerator', 'Number of Surveys']
st.markdown("### Surveys Collected by Each Enumerator")
st.write(enumerator_summary)

# Create a visualization of surveys collected by each enumerator
fig_enumerator = px.bar(enumerator_summary, x='Enumerator', y='Number of Surveys', title="Surveys Collected by Enumerator")
st.write(fig_enumerator)
