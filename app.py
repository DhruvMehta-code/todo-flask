from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SESSION_COOKIE_SECURE'] = False
db = SQLAlchemy(app)


class Do(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    work = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime , default = datetime.utcnow)

    def __repr__(self):
        return f"task {self.id}"


@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        db_task = request.form["user"]
        new_task = Do(work=db_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "there was an error to add !!!!!"
    else:
        tasks = Do.query.order_by(Do.date_created).all()
        return render_template("index.html",tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task_delet = Do.query.get_or_404(id)
    try :
        db.session.delete(task_delet)
        db.session.commit()
        return redirect("/")
    except:
        return "error to delete"

@app.route("/update/<int:id>",methods=["POST","GET"])
def update(id):
    task = Do.query.get_or_404(id)
    if request.method == "POST":
        task.work = request.form["user"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "Not Update !!!!" 
    else:
        return render_template("update.html",task=task)


if __name__ == ("__main__"):
    app.run(debug=True)