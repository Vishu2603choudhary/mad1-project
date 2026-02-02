from flask import Flask 
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite:///hosdata.db
app.config['SQLALCHEMY-TASK-MODIFICATION'] = False
db = SQLALchemy(app)