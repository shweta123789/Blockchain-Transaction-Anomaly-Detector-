# Blockchain-Transaction-Anomaly-Detector-
Blockchain Transaction Anomaly Detector uses machine learning to identify suspicious or unusual blockchain transactions in real time. By analyzing patterns in transaction data, it flags potential fraud, money laundering, or network manipulation, enhancing security and trust in blockchain systems.

# Blockchain Transaction Anomaly Detector

Blockchain Transaction Anomaly Detector is a machine learning–based system designed to monitor and detect unusual or suspicious blockchain transactions in real time. It analyzes transaction patterns to flag potential fraud, money laundering, or network manipulation, improving blockchain security and trust.


### BLOCKCHAIN WALLET ANOMALY DETECTION DASHBOARD

<img width="1864" height="873" alt="Screenshot 2025-09-28 223146" src="https://github.com/user-attachments/assets/5c4a48ae-6373-4992-a8b7-859a818aeb4b" />


### ANOMALY SCORE DISTRIBUTION 

<img width="910" height="786" alt="Screenshot 2025-09-28 223307" src="https://github.com/user-attachments/assets/11809271-fccb-4cd0-9020-9e6051845e9e" />


### Detect anomalies as transactions occur.

<img width="1028" height="793" alt="Screenshot 2025-09-28 223327" src="https://github.com/user-attachments/assets/9c4eacce-6891-4546-89d1-91a53ca16911" />

---

## 🚀 Features
- **Real-Time Analysis** – Detect anomalies as transactions occur.
- **Multiple Detection Algorithms** – Isolation Forest, Local Outlier Factor, clustering, etc.
- **Data Preprocessing** – Handles noisy and raw blockchain transaction data.
- **Scalable Design** – Works with large volumes of transactions.
- **Visualization** – Dashboards for flagged transactions and anomaly trends.

---

## 📂 Project Structure
├── data/

│ ├── blacklist

│ ├── Ethereum_Transaction

│ └── flagged_interactions_with_blacklist

├── notebooks/ Block Chain Projects

│ ├── app.py

│ ├── detection.py

│ └── visualization.py

└── BlockChain.iml

🧠 Algorithms Used
Isolation Forest:
Isolation Forest is an unsupervised anomaly detection algorithm that works by randomly selecting features and splitting data points to isolate them. Since anomalies are few and different, they are easier to isolate and require fewer splits compared to normal data points. This property makes Isolation Forest efficient, scalable, and well-suited for detecting outliers in large, high-dimensional datasets such as blockchain transaction records.
