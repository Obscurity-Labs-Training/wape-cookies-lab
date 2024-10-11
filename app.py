from flask import Flask, request, make_response
from datetime import datetime, timedelta

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

# Route to set a secure cookie with all security settings
@app.route('/get_secure_cookie')
def get_secure_cookie():
    resp = make_response("Secure cookie is being set")

    # Set cookie to expire in 1 hour
    expires = datetime.now() + timedelta(hours=1)

    # Set a cookie with security features
    resp.set_cookie(
        'secureUsername',                       # Cookie name
        'SecureJohnDoe',                        # Cookie value
        httponly=True,                          # HttpOnly flag (not accessible via JavaScript)
        secure=True,                            # Secure flag (only sent over HTTPS)
        samesite='Strict',                      # SameSite flag (restricts cross-site requests)
        expires=expires                         # Set expiration time
    )

    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
