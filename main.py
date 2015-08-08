from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api_twitter')
def twitter_api():
    return 'twitter api'

@app.route("/api_braintree")
def braintree_api():
	return "braintree api"

@app.route("/api_facebook")
def facebook_api():
	return "facebook api"

if __name__ == '__main__':
    app.run()