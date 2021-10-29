# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo
# import dnspython
MONGODB_URI = 'mongodb+srv://saint:Saintwithataint123@daysofpython.y1jbf.mongodb.net/DaysOfPython?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

db = client.DaysOfPython
db.students.insert_one({'name': 'Varun', 'country': 'India', 'city': 'Mumbai', 'age': 34})

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

