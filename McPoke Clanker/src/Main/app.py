'''
Created on Apr 16, 2026

@author: k2307731
'''
import subprocess
from flask import Flask, render_template
import sys



try:
    import flask
except ImportError:
    print("Flask not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    import flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('button.html') 

if __name__ == "__main__":
    app.run(debug=True)