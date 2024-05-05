from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__, static_url_path='/static')


# Configure MySQL connection
conn = pymysql.connect(
    host='nebula-db.cjiiukefoksp.us-east-1.rds.amazonaws.com',
    user='admin',
    password='master123',
    database='nebula'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student-dashboard')
def student_dashboard():
    return render_template('student-dashboard.html')


@app.route('/api/students')
def get_students():
    cur = conn.cursor()
    cur.execute("SELECT name FROM Basic_Details")  # Assuming 'name' is the column you want to display
    students_data = cur.fetchall()
    
    cur.execute("SELECT DISTINCT cohort_name FROM Basic_Details")  # Fetch unique cohort names
    cohorts_data = cur.fetchall()

    cur.close()
    
    students = [row[0] for row in students_data]  # Extracting student names
    cohorts = [row[0] for row in cohorts_data]  # Extracting unique cohort names
    
    return jsonify({'students': students, 'cohorts': cohorts})

if __name__ == '__main__':
    app.run(debug=True)
