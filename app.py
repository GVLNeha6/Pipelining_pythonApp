from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__)

def run_command(cmd):
    """
    Run a shell/batch command and return its output.
    """
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

# Home route to render dashboard
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Build route
@app.route('/build', methods=['POST'])
def build():
    # Call build script
    script_path = os.path.join(os.getcwd(), "build.bat")  # Windows batch file
    output = run_command(script_path)
    return output

# Deploy route
@app.route('/deploy', methods=['POST'])
def deploy():
    # Call deploy script
    script_path = os.path.join(os.getcwd(), "deploy.bat")  # Windows batch file
    output = run_command(script_path)
    return output

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
