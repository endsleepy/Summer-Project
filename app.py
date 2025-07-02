from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_templates('index.html')

@app.route('/registration')
def registration():
    return render_templates('register.html')

@app.route('/timetable')
def timetable():
    return render_templates('timetable.html')

@app.route('/timetable/days')
def timetable_days():
    return render_templates('timetable_day.html')

@app.route('/timetable/grades')
def timetable_grades():
    return render_templates('timetable_grade.html')

@app.route('/timetable/coaches')
def timetable_coaches():
    return render_templates('timetable_coach.html')

if __name__ == '__main__':
    app.run(debug=True)