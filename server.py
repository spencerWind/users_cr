from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route('/')
def home():
    users = User.get_all()
    return render_template('home.html', users = users)

@app.route('/user')
def user():
    users = User.get_all()
    print(users)
    return render_template('/user.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
    }
    User.save(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=5001)