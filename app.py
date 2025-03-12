my_project/
│
├── app.py               # Flask backend code (your provided code)
├── templates/
│   └── index.html       # Frontend HTML file (where you’ll have your form)
└── static/
    └── style.css        # Optional CSS file for styling
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Simulate student data and room availability
students = []
rooms = list(range(101, 201))  # Room numbers between 101 and 200
used_rooms = set()

# Route to display the Staff portal
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle student addition
@app.route('/add_student', methods=['POST'])
def add_student():
    student_name = request.form['student_name']
    student_email = request.form['student_email']
    student_course = request.form['student_course']

    # Allot a room number
    if rooms:
        room_number = rooms.pop(random.randint(0, len(rooms) - 1))
        used_rooms.add(room_number)
    else:
        room_number = 'No available rooms'

    # Add student details (Simulated here as appending to a list)
    student = {
        'name': student_name,
        'email': student_email,
        'course': student_course,
        'room': room_number
    }
    students.append(student)

    return jsonify({"message": "Student added successfully", "student": student})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
