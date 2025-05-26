# GenCostTracker – Your AI Usage Monitor
# Built for DevOps for GenAI Hackathon

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Simulated cost settings
COST_PER_1K_TOKENS = 0.002  # $0.002 per 1000 tokens
BUDGET = 1.00  # Set your estimated usage budget

# Load usage data
df = pd.read_csv("cost_log.csv")
df['Cost ($)'] = (df['Tokens Used'] / 1000) * COST_PER_1K_TOKENS
total_tokens = df['Tokens Used'].sum()
total_cost = df['Cost ($)'].sum()

# Page setup
st.set_page_config(page_title="GenCostTracker", layout="centered")
st.title("GenCostTracker Dashboard")
st.markdown("Track your GenAI token usage and cost estimates.")

# Show usage log table
st.subheader("Prompt Usage Log")
st.dataframe(df)

# Display totals
st.subheader("Summary")
st.markdown(f"Total Tokens Used: `{total_tokens}`")
st.markdown(f"Estimated Total Cost: `${total_cost:.4f}`")

# Visualize cost per prompt
st.subheader("Cost per Prompt")
fig, ax = plt.subplots()
ax.bar(df['Prompt'], df['Cost ($)'], color='skyblue')
ax.set_ylabel("Cost ($)")
ax.set_title("Prompt vs Estimated Cost")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Budget alert section
st.subheader("Budget Status")
if total_cost > BUDGET:
    st.error(f"Budget exceeded! Limit: ${BUDGET:.2f}, Current: ${total_cost:.4f}")
else:
    st.success(f"Within budget. Limit: ${BUDGET:.2f}, Current: ${total_cost:.4f}")

# Footer
st.markdown("---")
st.markdown("Developed by Sonam for the DevOps for GenAI Hackathon")
