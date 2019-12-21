from flask import Flask, jsonify, request
import json
import mysql.connector

# Create Flask instance
app = Flask(__name__)

# database vars
hostname = 'database'
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
	mycursor = dbc.cursor()
	sql = "INSERT INTO persons (Firstname, Lastname) VALUES (%s, %s)"
	val = (request.form['firstname'], request.form['lastname'])
	
	mycursor.execute(sql, val)
	
	dbc.commit()
		
	return ("1 record inserted")
	
@app.route("/persons", methods = ['get'])
def get():

	# Fetch data from db
	dbc = db_conn()
	mycursor = dbc.cursor()
	sql = "SELECT * FROM persons"
	rows = mycursor.execute(sql)
	result = mycursor.fetchall()
	
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
	
	
	
	
