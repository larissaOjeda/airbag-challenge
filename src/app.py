from flask import Flask 

from config import config

#Routes
from routes import exercises

app = Flask(__name__)

def page_not_found(error): 
    text = 'Page not found'
    return text

if __name__ == '__main__':
    app.config.from_object(config['development']) # from the dictionary
    
    #Blueprints
    app.register_blueprint(exercises.main, url_prefix = '/api/combinations')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    
    app.run()