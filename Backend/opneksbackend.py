from flask import Flask, jsonify, request
import json
import mysql.connector

# Create Flask instance
app = Flask(__name__)

# database vars
hostname = 'localhost'
username = 'root'
password = '12345'
database = 'opnexam2019'

# MYSQL_connector connection
def db_conn():
	# Connect to db
	db = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
	return db;
	
# POST method
@app.route("/person", methods = ['post'])
def post():
	# Post/Insert into db
	dbc = db_conn()
	sql = "INSERT INTO persons (Firstname, Lastname) VALUES (%s, %s)"
	val = (request.form[firstname], request.form[lastname])
	
	dbc.cursor().execute(sql,val)
	dbc.commit()
	
	return (dbc.cursor().rowcount, " record inserted")
	
@app.route("/persons", methods = ['get'])
def get():

	# Fetch data from db
	dbc = db_conn()
	sql = "SELECT * FROM persons"
	dbc.cursor().execute(sql)
	result = dbc.cursor().execute().fetchall
	
	# Initialize array and dictionary
	array = []
	dict = {}
	
	for opnexam2019 in result:
		dict = { 'PersonID': opnexam2019[0], 'Firstname': opnexam2019[1], 'Lastname': opnexam2019[2] }
		array.append(dict)
		dict = {}
	
	return jsonify(array)
	
	
if __name__ == "__main__":
 print("Running App")
 app.run(port=5000, debug=True)
	
	
	
	
