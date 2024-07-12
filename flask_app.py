## Python script to run Flask app

from flask import Flask

app = Flask(__name__)

@app.route('/')
def func1():
    return "Welcome...Hello World.!!!!"
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=9001)