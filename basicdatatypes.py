""" Basic Data types """

""" You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. 
The marks can be floating values. The user enters some integer N followed by the names and marks for students. 
You are required to save the record in a dictionary data type. 
The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places."""

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    if query_name in student_marks:
        average = sum(student_marks[query_name]) / len(student_marks[query_name])
        print "%.2f" % average

"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given scores. Store them in a list and find the score of the runner-up."""

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    scores = arr
    
    first = max(scores)
    i = 0
    while i < n:
        if first in scores:
            scores.remove(first)
        i += 1
        
    second = max(scores)
    print second