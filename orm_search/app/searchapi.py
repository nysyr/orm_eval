from flask import Flask, jsonify, Response, current_app
from flask_sqlalchemy import SQLAlchemy
from config import Config
import pprint
import os
import psycopg2
import json

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
pp = pprint.PrettyPrinter(width=55, compact=True)

class Work(db.Model):
    __tablename__ = 'works'
    work_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), index = True, unique = True)
    authors = db.Column(db.String(50), index = True)
    isbn = db.Column(db.String(50), index = True, unique = True)
    description = db.Column(db.String(255))

@app.route('/', methods=['GET'])
def home():
    return "Please query the catalog for all titles, or a specific work ID for more details."

@app.route('/catalog', methods=['GET'])
def handle_work():
    works =  db.session.execute(db.select(Work.work_id, Work.title, Work.authors).order_by(Work.title)).all()
    results = [
        {
            "work_id": work.work_id,
            "title": work.title,
            "authors": work.authors
        } for work in works
    ]
    return results

@app.route('/catalog/<int:work_id>', methods=['GET'])
def work_inspect(work_id):
    work_descs = Work.query.get_or_404(work_id)
    results = [
        {
            "title": work_descs.title,
            "authors": work_descs.authors,
            "isbn": work_descs.isbn,
            "description": work_descs.description
        }
    ]
    return results

if __name__ == '__main__':
    app.run(debug=True)