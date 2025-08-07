from flask import Flask, request, render_template
from model import train_model
import numpy as np

app = Flask(__name__)
model = train_model()

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            input_data = np.array([[num1, num2]])
            prediction = model.predict(input_data, verbose=0)
            result = f"Predicted Sum: {prediction[0][0]:.2f}"
        except:
            result = "Invalid input. Please enter valid numbers."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
