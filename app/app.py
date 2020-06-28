from datetime import datetime
import os

from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)


class Check(db.Model):
	check_id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(2000), nullable=False)
	status = db.Column(db.Integer, nullable=False)
	check_datetime = db.Column(db.DateTime, default=datetime.now)


class CheckSchema(ma.Schema):
	class Meta:
		fields = ('check_id', 'url', 'status', 'check_datetime')
		datetimeformat = '%Y-%m-%d %H:%M:%S'

check_schema = CheckSchema()
checks_schema = CheckSchema(many=True)


@app.route('/status', methods=['GET'])
def get_statuses():
	checks = Check.query.all()
	return jsonify(checks_schema.dump(checks))

@app.route('/hello', methods=['GET'])
def say_hi():
	return jsonify('Hello world')

@app.route('/status', methods=['POST'])
def add_status():
	req_data = request.json
	url = req_data['url']
	status = req_data['status']
	check = Check(url=url, status=status)
	db.session.add(check)
	db.session.commit()
	return check_schema.jsonify(check)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')