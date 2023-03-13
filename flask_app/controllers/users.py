from flask import Flask, render_template, redirect, request
from flask_app.models.user import User
from flask_app import app

@app.route('/')
def home():
    users = User.get_all()
    return render_template('home.html', users = users)

@app.route('/user')
def user():
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

@app.route('/user/show/<int:user_id>')
def show(user_id):
    user = User.get_one(user_id)
    return render_template("show_user.html", user = user)

@app.route('/user/update/<int:user_id>')
def show_update(user_id):
    user = User.get_one(user_id)
    return render_template("update_user.html", user = user)

@app.route('/user/update', methods=["POST"])
def update_user():
    User.update(request.form)
    return redirect('/')

@app.route('/user/delete/<int:user_id>')
def delete_user(user_id):
    User.delete(user_id)
    return redirect('/')