# from flask import Flask , jsonify , request

# app = Flask(__name__)

# users = [
# 	{
# 		'id' : 1,
# 		'name' :'Vikas',
# 		'age' : 20
# 	},
# 	{
# 		'id' : 3,
# 		'name' :'Neha',
# 		'age' : 19
# 	},
# 	{
# 		'id' : 2,
# 		'name' :'Ashima',
# 		'age' : 21
# 	}
# 	]

# @app.route('/')
# def index():
# 	return app.send_static_file('index.html')
# @app.route('/users')
# def getUsers():
# 	return jsonify(users)

# @app.route('/users/<id>')
# def getuser(id):
# 	f = list(filter(lambda u : str(u['id'])==id,users))
# 	return jsonify(f)

# if __name__ == "__main__":
# 	app.run()

from flask import Flask , jsonify , request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = [
	{
		'id' : 1,
		'name' :'Vikas',
		'age' : 20
	},
	{
		'id' : 3,
		'name' :'Neha',
		'age' : 19
	},
	{
		'id' : 2,
		'name' :'Ashima',
		'age' : 21
	}
	]

@socketio.on('message')
def handlemessage(data):
	socketio.emit('push',data,broadcast=True,include_self=False)

@app.route('/')
def index():
	return app.send_static_file('index.html')
@app.route('/users')
def getUsers():
	return jsonify(users)

@app.route('/users/<id>')
def getuser(id):
	f = list(filter(lambda u : str(u['id'])==id,users))
	return jsonify(f)

if __name__ == "__main__":
	socketio.run(app)

















