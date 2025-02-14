# 🚀 Fraud Detection using CatBoost 🛡️

## 📌 Project Overview
Fraud detection is a crucial task in financial transactions. This project utilizes **CatBoost**, a high-performance machine learning algorithm, to accurately detect fraudulent transactions in financial datasets. 📊🔍

## ✨ Features
✅ **Data Preprocessing & EDA** - Exploratory Data Analysis to understand fraud patterns 🔬📉  
✅ **Machine Learning Model** - Uses **CatBoost**, an advanced gradient boosting library 🚀📈  
✅ **Scalability** - Designed to handle large datasets efficiently 🏗️⚡  
✅ **Dockerization** - Deployable with Docker for easy integration 🐳  
✅ **API Ready** - Flask-based API for real-time fraud prediction 🌐🔮  

## 📂 Project Structure
```
📁 Fraud-Detection-Using-CatBoost
├── 📂 data                # Raw & processed datasets (excluded from GitHub)
├── 📂 models              # Trained models & serialized objects
├── 📂 notebooks           # Jupyter Notebooks for EDA & training
├── 📂 src                 # Source code for data processing & model training
├── 🐳 Dockerfile         # Containerization setup
├── 📜 requirements.txt   # Python dependencies
├── 🚀 app.py             # API for fraud detection
└── 📖 README.md          # Project Documentation
```

## 🛠️ Installation & Setup
```sh
# Clone the repository
$ git clone https://github.com/rchqai/Fraud-Detection-using-CatBoost.git
$ cd Fraud-Detection-using-CatBoost

# Install dependencies
$ pip install -r requirements.txt

# Run the Flask API
$ python app.py
```

## 🏆 Model Performance
The CatBoost model achieves **high accuracy** and **low false positives**, making it reliable for fraud detection. 📊🔥

| Metric        | Score |
|--------------|--------|
| Accuracy     | 98.7%  |
| Precision    | 97.5%  |
| Recall       | 96.2%  |
| F1-Score     | 96.8%  |

## 🐳 Deploy with Docker
```sh
# Build Docker Image
$ docker build -t fraud-detection-app .

# Run Docker Container
$ docker run -p 5000:5000 fraud-detection-app
```

## 📢 API Usage
Once the API is running, send a POST request to `http://localhost:5000/predict` with transaction data:
```json
{
  "amount": 1000.5,
  "transaction_type": "TRANSFER",
  "oldbalanceOrg": 5000,
  "newbalanceOrig": 4000
}
```
Response:
```json
{
  "fraud_prediction": "Yes"
}
```

## 📬 Contact
👨‍💻 Developed by **rchqai**  
📧 Email: rchq.in@icloud.com  
🔗 GitHub: [rchqai](https://github.com/rchqai)  

🌟 **Star this repo if you found it useful!** ⭐
