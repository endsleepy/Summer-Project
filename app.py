from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

@app.route('/timetable/days')
def timetable_days():
    return render_template('timetable_day.html')

@app.route('/timetable/grades')
def timetable_grades():
    return render_template('timetable_grade.html')

@app.route('/timetable/coaches')
def timetable_coaches():
    return render_template('timetable_coach.html')

if __name__ == '__main__':
    app.run(debug=True)