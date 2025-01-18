from flask import Flask  
from flask_sqlalchemy import SQLAlchemy  
# from flask_migrate import Migrate  
  
# Initialize the app  
app = Flask(__name__)  
# app.config.from_object(Config)  
  
# # Initialize the database and migration engine  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use SQLite for simplicity, replace with your actual DB URI  
db = SQLAlchemy(app) 

# Participant.__table__.create(db.session.bind) 
# migrate = Migrate(app, db)  
  
# Import the routes  
from app.main import routes as main_routes  
  
# Register the blueprints  
app.register_blueprint(main_routes.bp)  
# app.register_blueprint(api_routes.bp)  
  
# At the end of the file, import the models  
from app import models  