# O N Y X
## The Spam Classifier
![ONYX Web app Screenshot.png](https://github.com/Ananya-yv/ONYX-Spam-Classifier/blob/606cfb9c5fee478f3cf951496fa1873b526c9b2c/ONYX%20Web%20app%20Screenshot.png)

##  Overview
This project is a **Spam Classifier** designed to detect spam messages in **English**. It leverages **SBERT (Sentence-BERT) for text embeddings** and **Support Vector Machine (SVM) for classification**.

##  Features
- **Handles English text messages**
- **Uses SBERT for high-quality text embeddings**
- **Employs SVM for efficient spam classification**
- **Handles class imbalance using SMOTE**
- **Provides model evaluation metrics (confusion matrix, accuracy, classification report)**
- **Live and accessible via Streamlit.**

##  Dataset
The dataset consists of about **5575** English text messages labeled as **spam** or **not spam** .

##  Methodology
1. **Text Embeddings:** SBERT converts text messages into high-dimensional vectors.
2. **Data Balancing:** SMOTE is used to address class imbalance.
3. **Classification:** SVM classifies the messages as spam or not spam.
4. **Evaluation:** The model is evaluated using accuracy, confusion matrix, and classification reports.

##  Results
-  **Model accuracy - 99.01%.**
  
| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
|ham    | 0.99      | 1.00   | 0.99     | 971     |
|spam   | 1.00      | 0.92   | 0.96     | 144     |


##  Deployment
I developed and deployed using **Streamlit**. The web app is available for use at:

🔗 [Live Demo](https://onyx-spam-classifier.streamlit.app/)

##  Future Improvements
- Working on Spam detection of Indian Languages

