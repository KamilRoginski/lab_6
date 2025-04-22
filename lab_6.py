#Name: Kamil Roginski
#Date: 21 APR 2025
#Professor: Mark Babcock
#Course: CYOP 300

"""
Lab 6: Simple Flask application displaying:
- Three routes: home, about, contact
- Rendering templates with render_template
- Passing current date and time to templates
"""

from datetime import datetime as dt
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page with date and time."""
    now = dt.now()
    return render_template('home.html', now=now)

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

if __name__ == '__main__':
    # Run the development server
    app.run(debug=True)
