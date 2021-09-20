from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'secret'
app.permanent_session_lifetime = timedelta(seconds=30)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
	if request.method == 'POST':
		session.permanent = True
		user = request.form['name']
		session['user'] = user
		flash('Logged In')

		return redirect(url_for('profile'))
	else:
		if 'user' in session:
			flash('Logged In Already')

			return redirect(url_for('profile'))

		return render_template('auth.html')

@app.route('/profile')
def profile():
	if 'user' in session:
		user = session['user']

		return render_template('profile.html', user=user)
	else:
		flash('Not Logged In')

		return redirect(url_for('auth'))

@app.route('/logout')
def logout():
	flash('Logged Out', 'info')
	session.pop('user', None)

	return redirect(url_for('auth'))

if __name__ == '__main__':
	app.run(debug=True)