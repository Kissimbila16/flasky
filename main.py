from flask import Flask, render_template
from models import model  # Assuming this imports a model

app = Flask(__name__)

@app.route('/')
def home():  # Renamed from 'index' for clarity
    return render_template("index.html")

@app.route('/routes')
def routes():  # Renamed from 'index'
    return render_template("routes.html")

    
@app.route('/about')
def about():  # Renamed from 'index'
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
