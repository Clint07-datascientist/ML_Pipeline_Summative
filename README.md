# AgroInsightX ML Pipeline

A machine learning pipeline for agricultural disease and pest detection in maize crops.

---

## 📽️ Demo Video

👉 [Watch Demo on YouTube](https://youtube.com/your-demo-link-here)  
🎯 Shows prediction, retraining, and flood testing

---

# 🌐 Live API

> **Base URL**: `https://maize-api.example.com`

- `POST /predict` — Predict class of a maize leaf image
- `POST /upload` — Upload bulk images for retraining
- `POST /retrain` — Trigger model retraining

---

## 📄 Project Description

This project demonstrates a real-world Precision Agriculture use case, specifically:

- Classifying **7 maize leaf conditions**:
  - `Fall Armyworm`, `Grasshopper`, `Healthy`, `Leaf Beetle`, `Leaf Blight`, `Leaf Spot`, and `Streak Virus`.
- Creating an **end-to-end ML lifecycle** with:
  - Offline training
  - Model versioning
  - Retraining trigger via API
  - API for serving predictions
  - Web UI for interaction
  - Cloud deployment
  - Load testing

---

## 📦 Dataset

> 📥 **Source**: [Mendeley Maize Disease Dataset](https://data.mendeley.com/datasets/bwh3zbpkpv/1)

- Over 4,000 high-resolution maize leaf images
- Annotated into 7 disease classes
- Used for training, testing, and retraining the model

---

## Dataset Structure

This project uses a comprehensive dataset with over 10,000 images for training and testing machine learning models to identify various maize crop conditions.

### Categories
- **Fall Armyworm** - Pest identification
- **Grasshopper** - Pest identification  
- **Healthy** - Healthy crop identification
- **Leaf Beetle** - Pest identification
- **Leaf Blight** - Disease identification
- **Leaf Spot** - Disease identification
- **Streak Virus** - Disease identification

---

### Project Structure
```
ML_Pipeline_Summative/
│
├── README.md # This file
├── notebook/
│   └── ml_pipeline.ipynb        # Full training notebook
│
├── src/
│   ├── preprocessing.py                # Preprocessing logic
│   ├── model.py                        # Model training + retraining logic
│   └── prediction.py                   # Predict single image
│
├── data/
│   ├── train/
│   └── test/
│
├── models/
│   └── maize_model.h5
│
├── api/
│   ├── main.py                         # FastAPI app
│   └── utils.py                        # Shared logic for upload/retrain
│
├── ui/
│   └── app.py                          # Streamlit UI
│
├── Dockerfile
└── requirements.txt                      

```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Clint07-datascientist/ML_Pipeline_Summative.git
   cd ML_Pipeline_Summative
   ```

2. **Create and activate virtual environment**
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **Or use the provided activation script:**
   ```bash
   activate_env.bat
   ```
   
   **macOS/Linux:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set up Jupyter kernel (optional)**
   ```bash
   python -m ipykernel install --user --name=agroinsightx --display-name="AgroInsightX ML Pipeline"
   ```

5. **Obtain the dataset** 

6. **Run the ML pipeline**
   ```bash
   jupyter notebook notebook/ml_pipeline.ipynb
   ```
7. **Install all the requirements**
   ```bash
   pip install -r requirements.txt
   ```
8. **Start FastAPI server**
   ```bash
   uvicorn api.main:app --reload --port 8000
   ```
9. **Use Streamlit UI**
   ```bash
   streamlit run ui/app.py
   ```
10. **Simulate Flood testing using locust**
    ```bash
    locust -f locustfile.py --host=http://localhost:8000
    ```

---

## Locust Load Testing Results


