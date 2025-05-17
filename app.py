from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

# In-memory storage (for demonstration only)
users = []

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        age = request.form.get('age')
        
        # Basic validation
        if not username or not email or not password:
            flash('Username, email, and password are required!', 'error')
            return redirect(url_for('register'))
        
        # Check if username or email already exists
        if any(user['username'] == username for user in users):
            flash('Username already taken!', 'error')
            return redirect(url_for('register'))
            
        if any(user['email'] == email for user in users):
            flash('Email already registered!', 'error')
            return redirect(url_for('register'))
        
        # Add user to storage
        user_data = {
            'username': username,
            'email': email,
            'password': password,  # In real app, hash this password
            'first_name': first_name,
            'last_name': last_name,
            'age': age
        }
        users.append(user_data)
        
        flash('Registration successful!', 'success')
        return redirect(url_for('registered_users'))
    
    return render_template('register.html')

@app.route('/users')
def registered_users():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)