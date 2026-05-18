from flask import Flask, request, render_template, redirect

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

def gen_table(avg=False):
    columns = ['Фамилия', 'Имя', 'Отчество', 'Класс'] + subjects
    rows = []
    for student in students:
        row = [student[:-1]]
        marks = [marks[1] for marks in student[-1].items()]
        if avg:
            avgs=[]
            for subject_marks in marks:
                if subject_marks:
                    avgs.append([round(sum(subject_marks)/len(subject_marks), 2)])
                else:
                    avgs.append([0.00])
            row.append(avgs)
        else:
            row.append(marks)
        rows.append(row)
    return columns, rows

@app.route('/')
def root_page():
    return redirect('/marks')

@app.route('/marks')
def marks_page():
    average = request.args.get("average", default=False)
    columns, rows = gen_table(average)
    print(columns, rows, sep='\n')
    return render_template('root.html', columns=columns, rows=rows, average=average)


if __name__ == '__main__':
    bootstrap()
    app.run('127.0.0.1', port=25565, debug=True)