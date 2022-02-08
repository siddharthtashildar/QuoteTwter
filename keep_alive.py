#Import modules
from flask import Flask
from threading import Thread

#Create a basic webpage for url
app = Flask('')


#Main Fuctions

@app.route('/')
def home():
    return "I'm alive, I'm revived, I survived You surprised? Gonna cry about it? You should see the other guy I've returned and I've waited my turn A decade of time to make everything mine!"
    

def run():
    app.run(host='0.0.0.0',port=8080)


#Thread
def keep_alive():
    t = Thread(target=run)
    t.start()