# todo-flask

this is simple todo list website using flask and sqlite3 database and deploy using heroku cloud. 
Simple todo list is the website that you add work list of the day & watch which work is remaining . 

about flask :
flask is lightweight web-framework . It has easy syntax and boilerplate. If you know python basic and want to do web-development so you can start with flask , it's easy to learn 

here are boilerplate :
```
from flask import Flask #(import flask)

app = Flask(__name__) #(intialize your app in flask)

@app.route("/")
def name():
	functionality
  
if __name__ == "__main__":

   app.run(debug=True)    #(run application & debug = True means live changes)
```

here is the link :

https://daytodaytask.herokuapp.com/


