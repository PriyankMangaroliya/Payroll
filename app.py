from config import init_app, mongo
from api.auth_routes.auth_login_routes import login
from api.auth_routes.forgot_password_routes import forgotpassword
from api.auth_routes.auth_register_routes import register
from flask import Flask, render_template, jsonify, redirect, send_from_directory, session

app = Flask(__name__)
init_app(app)

# Register blueprints (routes)
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(forgotpassword, url_prefix='/forgotpassword')
app.register_blueprint(register, url_prefix='/register')


@app.route('/')
def home():
    return render_template("auth/auth-login.html")


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    response = jsonify({'message': 'Logged out successfully!'})
    response.set_cookie('token', '', expires=0)
    response = redirect('/')# Clear the cookie
    return response

@app.errorhandler(404)
def handle_404_error(e):
    return render_template('error/errors-404.html')
    # return jsonify({'status': 'error shubham', 'message': 'Resource not found (404)'}), 404


@app.errorhandler(500)
def handle_500_error(e):
    return render_template('error/errors-500.html')
    # return jsonify({'status': 'error', 'message': 'Internal server error (500)'}), 500


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
