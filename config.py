from flask_pymongo import PyMongo

mongo = PyMongo()

def init_app(app):
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/Payroll'
    mongo.init_app(app)

