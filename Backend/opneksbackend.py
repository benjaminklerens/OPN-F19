from flask import Flask, jsonify, request
import json
import mysql.connector

# Create Flask instance
app = Flask(__name__)

# MYSQL_connector connection
def mysql_connect():
	# Connect to db
	db = mysql.connector.connect(
		host='database',
		database='opnexam2019',
		user='root')
	return db;
	
# POST method
@app.route('/person', methods = ['POST'])
def POST():
	# Post/Insert into db
	dbc = mysql_connect()
	sql = "INSERT INTO persons (Firstname, Lastname) VALUES (%s, %s)"
	val = (request.form[firstname], request.form[lastname])
	
	dbc.cursor().execute(sql,val)
	dbc.commit()
	
	return (dbc.cursor().rowcount, " record inserted")
	
@app.route('/persons', methods = ['GET'])
def GET():

	# Fetch data from db
	dbc = mysql_connect()
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
	
	
if __name__ == '__main__':
	app.run()
	
	
	
	
