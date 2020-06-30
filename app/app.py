from datetime import datetime
import os

from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite://')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super_secret_jwt_key'
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
CORS(app)


class Check(db.Model):
	__tablename__ = "checks"

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


@app.route('/', methods=['GET'])
def index():
	return jsonify('Status API')


@app.route('/status', methods=['POST'])
@jwt_required
def add_status():
	req_data = request.json
	url = req_data['url']
	status = req_data['status']
	check = Check(url=url, status=status)
	db.session.add(check)
	db.session.commit()
	return check_schema.jsonify(check)


@app.route('/login', methods=['POST'])
def login():
	req_data = request.json
	username = req_data.get('username')
	password = req_data.get('password')
	
	if not req_data or not username or not password:
		return jsonify({'msg': 'Incomplete auth data'}), 400
	if username != 'test' or password != 'test':
		return jsonify({'msg': 'Invalid auth data'}), 403

	return jsonify(access_token=create_access_token(username))
