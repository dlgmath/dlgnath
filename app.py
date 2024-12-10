from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for working with sessions

# Simulating a user database
users_db = {"admin": "password"}

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    return redirect(url_for('login'))  # Redirect to login page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users_db.get(username) == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Incorrect username or password"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            users_db[username] = password
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Passwords don't match"
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/themes')
def themes():
    return render_template('themes.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/answers')
def answers():
    return render_template('answers.html')

if __name__ == '__main__':
    app.run(debug=True)

