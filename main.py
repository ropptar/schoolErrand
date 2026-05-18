from flask import Flask, render_template

app = Flask(__name__)

students, subjects  = [], []

def bootstrap():
    global students, subjects, marks
    with open('students.txt') as students_file, \
         open('subjects.txt') as subjects_file, \
         open('marks.txt') as marks_file:
        students = [line.strip().split()[1:] for line in students_file.readlines()]
        subjects = [line.strip().split()[1] for line in subjects_file.readlines()]
        for student in students:
            student.append({subject:[] for subject in subjects})
        for line in marks_file.readlines():
            line = list(map(int, line.strip().split()))
            student = line[0]-1
            subject = subjects[line[1]-1]
            mark = line[2]
            students[student][-1][subject].append(mark)
    return 0

@app.route('/')
def root_page():
    columns = ['Фамилия', 'Имя', 'Отчество', 'Класс'] + subjects
    rows = [[ \
            student[:-1], \
            [marks[1] for marks in student[-1].items()]] \
            for student in students]
    return render_template('root.html', columns=columns, rows=rows)


if __name__ == '__main__':
    bootstrap()
    app.run('127.0.0.1', port=25565, debug=True)