from flask import Flask

app = Flask(__name__)

# Configuration settings can be added here
app.config['DEBUG'] = True

# Import routes
from routes import *

if __name__ == '__main__':
    app.run()