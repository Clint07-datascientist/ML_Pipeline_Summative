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

### Data Organization
```
data/
├── train_set/
│   ├── fall armyworm/
│   ├── grasshoper/
│   ├── healthy/
│   ├── leaf beetle/
│   ├── leaf blight/
│   ├── leaf spot/
│   └── streak virus/
└── test_set/
    ├── fall armyworm/
    ├── grasshoper/
    ├── healthy/
    ├── leaf beetle/
    ├── leaf blight/
    ├── leaf spot/
    └── streak virus/
```

## Note on Dataset

⚠️ **Dataset not included in repository**: Due to the large size (10,000+ images), the actual image dataset is excluded from version control via `.gitignore`. 

To use this project:
1. Clone this repository
2. Obtain the dataset separately (contact repository owner for access)
3. Place images in the `data/` folder structure shown above

## Getting Started

[Add your setup and usage instructions here]