from flask import Flask, request, make_response

app = Flask(__name__)

# Route to set a cookie
@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie is being set")
    # Set a simple cookie (name: username, value: JohnDoe)
    resp.set_cookie('username', 'JohnDoe')
    return resp

# Route to get a cookie
@app.route('/get_cookie')
def get_cookie():
    # Retrieve the cookie from the request
    username = request.cookies.get('username')
    if username:
        return f'Cookie found! Username: {username}'
    return 'No cookie found!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
