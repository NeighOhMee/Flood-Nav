import os
def startServer(success, distance):
	'''try:
	  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
	  from SocketServer import TCPServer as Server
	except ImportError:
	  from http.server import SimpleHTTPRequestHandler as Handler
	  from http.server import HTTPServer as Server

	# Read port selected by the cloud for our application
	PORT = int(os.getenv('PORT', 8000))
	# Change current directory to avoid exposure of control files
	os.chdir('C:\\Users\\nettr\\Dropbox\\Random Projects\\Hackathon\\Flood Nav\\Flood-Nav\\src\\static')

	httpd = Server(("", PORT), Handler)
	try:
	  print("Start serving at port %i" % PORT)
	  httpd.serve_forever()
	except KeyboardInterrupt:
	  pass
	httpd.server_close()'''
	from flask import Flask, render_template
	app = Flask(__name__, static_url_path='/static')

	@app.route('/')
	def index():
		if success:
			message = "Calculated"
		else:
			message = "Failed"
		if distance:
			distance_message = "Distance = "
			distance_message += str(distance)
		else:
			distance_message = ""
		return render_template('index.html', success=message, distance=distance_message)
	
	app.run(debug=True)