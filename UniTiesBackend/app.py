from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017, username='User', password='4lNukg1PfxSL8SZj')
db = client['UniStud']
collection = db['sample_mflix']

@app.route('/')
def hello_world():  # put application's code here
    data = collection.find('movies')
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
