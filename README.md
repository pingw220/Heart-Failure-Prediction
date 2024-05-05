## Project Title: Cardiovascular Disease Prediction

### Overview
Cardiovascular diseases (CVDs) are the leading cause of death globally. Early detection and management are crucial in combating these diseases. This project aims to develop machine learning models that predict the likelihood of individuals developing cardiovascular diseases based on various health attributes.

### Dataset
The dataset used in this project is sourced from Kaggle and consists of 11 features related to cardiovascular health, including Age, Sex, Chest Pain Type, Resting Blood Pressure, Cholesterol, and more.

### Code
The project utilizes various machine learning algorithms including Decision Tree, Random Forest, and XGBoost to build predictive models for cardiovascular disease. Key steps in the project include:

1. **Data Preprocessing**:
   - One-hot encoding of categorical variables.
   - Normalization of numerical variables.

2. **Model Building**:
   - **Decision Tree Classifier**: Tuned min_samples_split and max_depth.
   - **Random Forest Classifier**: Optimized min_samples_split, max_depth, and n_estimators.
   - **XGBoost Classifier**: Fine-tuned n_estimators and learning_rate.

3. **Evaluation**:
   - Models are evaluated based on their accuracy metrics on both training and test datasets.

### Interactive Website
To use the interactive web application:

1. Ensure you have Python and Flask installed.
2. Clone the repository and navigate to the project directory.
3. Install required Python packages: `pip install -r requirements.txt`.
4. Run the Flask app: `python app.py`.
5. Open a web browser and go to `http://127.0.0.1:5000/` to interact with the application.
6. Input your health attributes in the form provided and submit to receive a prediction.

### Model Accuracies
The accuracies of the models on the test dataset are as follows:
- **Decision Tree Classifier**: 70%
- **Random Forest Classifier**: 82%
- **XGBoost Classifier**: 85%

These accuracies highlight the potential of advanced ensemble methods like Random Forest and XGBoost in improving predictive performance.

### How to Run the Code
1. Install necessary dependencies including NumPy, Pandas, Scikit-learn, and XGBoost.
2. Download the `heart.csv` dataset from Kaggle and place it in the project directory.
3. Execute the code blocks sequentially to preprocess the data, build models, and evaluate their performance.

### Conclusion
The developed machine learning models demonstrate promising accuracy in predicting the likelihood of cardiovascular diseases. Further optimization and refinement can enhance their predictive capabilities, contributing significantly to the early detection and management of cardiovascular health issues.
