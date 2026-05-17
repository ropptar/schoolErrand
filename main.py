from flask import Flask
import pandas as pd

app = Flask(__name__)

students, subjects, marks = [], [], []

def bootstrap():
    global students, subjects, marks
    with open('students.txt') as students_file, \
         open('subjects.txt') as subjects_file, \
         open('marks.txt') as marks_file:
        students = [line.strip().split()[1:] for line in students_file.readlines()]
        subjects = [line.strip().split()[1] for line in subjects_file.readlines()]
        marks = [line.strip().split() for line in marks_file.readlines()]
    return 0


bootstrap()
print(students,subjects,marks, sep='\n')