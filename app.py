import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Blockchain Anomaly Detector")

#Load data
@st.cache_data
def load_data():
    wallets = pd.read_csv("flagged_wallets.csv")
    tx_interactions = pd.read_csv("flagged_interactions_with_blacklist.csv")
    wallets['wallet_address'] = wallets['wallet_address'].str.lower()
    tx_interactions['from'] = tx_interactions['from'].str.lower()
    tx_interactions['to'] = tx_interactions['to'].str.lower()
    return wallets, tx_interactions

wallets, tx_data = load_data()

#Title

st.title("🧠 Blockchain Wallet Anomaly Detection Dashboard")
st.markdown("Analyze suspicious wallets flagged by anomaly detection and enriched with mixer/bridge exploit data.")

#Sidebar filter

st.sidebar.header("🔎 Filters")
min_score = st.sidebar.slider("Minimum anomaly score", float(wallets['anomaly_score'].min()), float(wallets['anomaly_score'].max()), float(wallets['anomaly_score'].min()))
risk_labels = st.sidebar.multiselect("Filter by risk label", options=wallets['risk_label'].dropna().unique())

filtered_wallets = wallets[wallets['anomaly_score'] >= min_score]
if risk_labels:
    filtered_wallets = filtered_wallets[filtered_wallets['risk_label'].isin(risk_labels)]

#Display DataFrame

st.subheader("📋 Flagged Wallets")
st.dataframe(filtered_wallets[['wallet_address', 'anomaly_score', 'tx_count', 'total_eth_sent', 'risk_label']].sort_values(by='anomaly_score'))

#Risk breakdown chart

st.subheader("🛑 Risk Label Distribution")
risk_counts = wallets['risk_label'].fillna("Unlabeled").value_counts()
st.bar_chart(risk_counts)

#Anomaly score distribution

st.subheader("📊 Anomaly Score Distribution")
fig, ax = plt.subplots()
ax.hist(wallets['anomaly_score'], bins=50, color='orange', edgecolor='black')
ax.set_xlabel("Anomaly Score")
ax.set_ylabel("Wallet Count")
st.pyplot(fig)

#Wallet drill-down

st.subheader("🔍 Investigate a Wallet")
selected_wallet = st.selectbox("Select a flagged wallet", options=wallets['wallet_address'].tolist())

wallet_info = wallets[wallets['wallet_address'] == selected_wallet].iloc[0]
st.markdown(f""" 
**Wallet Address:** {selected_wallet}
**Anomaly Score:** {wallet_info['anomaly_score']:.4f}
**Tx Count:** {wallet_info['tx_count']}
**Total ETH Sent:** {wallet_info['total_eth_sent']}
**Risk Label:** {wallet_info['risk_label'] if pd.notna(wallet_info['risk_label']) else "N/A"}
""")

#Show interactions

wallet_txs = tx_data[tx_data['from'] == selected_wallet]
if not wallet_txs.empty:
    st.markdown(f"### 🧾 Transactions to High-Risk Addresses")
    st.dataframe(wallet_txs[['to', 'label', 'value_eth', 'gas', 'blockNumber']])
else:
    st.info("This wallet has no known interactions with risky addresses.")