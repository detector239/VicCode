from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Colomn(db.Integer, primary_key=True)
    content = db.Colomn(db.String(200), nullable=False)
    completed = db.Colomn(db.Integer, default=True)
    data_crated = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)