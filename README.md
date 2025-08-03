# AgroInsightX ML Pipeline

A machine learning pipeline for agricultural disease and pest detection in maize crops.

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

5. **Obtain the dataset** (contact repository owner for access)

6. **Run the ML pipeline**
   ```bash
   jupyter notebook notebook/ml_pipeline.ipynb
   ```
