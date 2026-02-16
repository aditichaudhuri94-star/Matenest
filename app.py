from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'matenest_super_secret_key'

# MySQL Configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '#Aditichaudhuri12345'  # <--- UPDATE THIS
app.config['MYSQL_DB'] = 'matenest'

mysql = MySQL(app)

@app.route('/')
def index():
    search_query = request.args.get('location')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if search_query:
        query = "SELECT * FROM users WHERE location LIKE %s ORDER BY created_at DESC"
        cursor.execute(query, ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT * FROM users ORDER BY created_at DESC")
        
    roommates = cursor.fetchall()
    return render_template('index.html', roommates=roommates)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            d = request.form
            cur = mysql.connection.cursor()
            cur.execute("""INSERT INTO users(username, email, password, budget, location, gender, bio) 
                           VALUES(%s, %s, %s, %s, %s, %s, %s)""", 
                        (d['username'], d['email'], 'default_pass', d['budget'], 
                         d['location'], d['gender'], d['bio']))
            mysql.connection.commit()
            cur.close()
            flash('Profile created successfully! Welcome to the nest.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)