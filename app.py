from flask import Flask, render_template
import logging

# Initialize Flask App
app = Flask(__name__)

# Configure Logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the second page
@app.route('/second')
def second():
    return render_template('second.html')

# Error Handling for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    # Log the error
    app.logger.error(f"Page not found: {e}")
    return render_template('404.html'), 404

# Running the App
if __name__ == '__main__':
    app.run(debug=True)
