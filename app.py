from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier

app = Flask(__name__)


def load_data_and_models():
    df = pd.read_csv("heart.csv")
    X = df.drop('HeartDisease', axis=1)
    y = df['HeartDisease']
    encoder = OneHotEncoder(handle_unknown='ignore')
    categorical_columns = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
    X_encoded = encoder.fit_transform(X[categorical_columns])
    model = XGBClassifier(n_estimators=500, learning_rate=0.1, verbosity=1, random_state=55)
    model.fit(X_encoded, y)
    return encoder, model

encoder, model = load_data_and_models()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        user_data = pd.DataFrame([{
            'Sex': request.form['Sex'],
            'ChestPainType': request.form['ChestPainType'],
            'RestingECG': request.form['RestingECG'],
            'ExerciseAngina': request.form['ExerciseAngina'],
            'ST_Slope': request.form['ST_Slope']
        }])
        
        user_input_encoded = encoder.transform(user_data)
        prediction = model.predict(user_input_encoded)
        result = "Heart Disease" if prediction[0] == 1 else "No Heart Disease"
        return render_template('index.html', prediction=result)
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
