## Project Title: Cardiovascular Disease Prediction

### Overview:
Cardiovascular diseases (CVDs) are the leading cause of death globally, responsible for millions of deaths each year. Early detection and management are crucial in combating these diseases. In this project, we aim to develop machine learning models to predict the likelihood of individuals developing cardiovascular diseases based on various health attributes.

### Dataset:
The dataset used in this project is sourced from Kaggle and contains 11 features related to cardiovascular health. These features include:

- **Age**: Age of the patient (in years)
- **Sex**: Gender of the patient (Male or Female)
- **ChestPainType**: Type of chest pain (Typical Angina, Atypical Angina, Non-Anginal Pain, Asymptomatic)
- **RestingBP**: Resting blood pressure (mm Hg)
- **Cholesterol**: Serum cholesterol level (mm/dl)
- **FastingBS**: Fasting blood sugar (1: if FastingBS > 120 mg/dl, 0: otherwise)
- **RestingECG**: Resting electrocardiogram results (Normal, ST, LVH)
- **MaxHR**: Maximum heart rate achieved (Numeric value between 60 and 202)
- **ExerciseAngina**: Exercise-induced angina (Yes or No)
- **Oldpeak**: ST depression induced by exercise (Numeric value measured in depression)
- **ST_Slope**: The slope of the peak exercise ST segment (Up, Flat, Down)
- **HeartDisease**: Output class (1: Heart disease, 0: Normal)

### Code:
The code provided utilizes various machine learning algorithms to build predictive models for cardiovascular disease. It involves the following steps:

1. **Data Preprocessing**:
    - Removal of binary variables as one-hot encoding wouldn't affect them.
    - One-hot encoding of categorical variables with three or more values.

2. **Model Building**:
    - Decision Tree Classifier: Tuning parameters such as min_samples_split and max_depth.
    - Random Forest Classifier: Optimization of parameters including min_samples_split, max_depth, and n_estimators.
    - XGBoost Classifier: Fine-tuning parameters like n_estimators and learning_rate.

3. **Evaluation**:
    - Assessment of model performance using accuracy metrics on both training and test datasets.

### Instructions to Run the Code:
1. Install necessary dependencies (NumPy, Pandas, Scikit-learn, XGBoost).
2. Load the provided dataset ('heart.csv') from Kaggle.
3. Execute the code blocks sequentially to preprocess the data, build models, and evaluate their performance.

### Conclusion:
The developed machine learning models demonstrate promising accuracy in predicting the likelihood of individuals developing cardiovascular diseases. Further optimization and refinement of these models can potentially enhance their predictive capabilities, contributing to early detection and management of cardiovascular health issues.

For detailed implementation and results, refer to the provided code.

### Contributors:
- [Your Name/Username]
- [Additional contributors if any]

### License:
[Specify the license under which the project is distributed, if applicable]

### Contact Information:
For inquiries or suggestions, please contact [Your Email Address].
