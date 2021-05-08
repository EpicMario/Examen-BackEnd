from students import students
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})


@app.route('/students', methods=['GET'])
def getStudents():
    return jsonify(students)


@app.route('/students', methods=['POST'])
def addStudent():
    new_student = {
        "name": request.json['name'],
        "career": request.json['career']
    }
    students.append(new_student)
    return jsonify({"message": "Estudiante añadido", "students": students})


if __name__ == '__main__':
    app.run(port=5000)
