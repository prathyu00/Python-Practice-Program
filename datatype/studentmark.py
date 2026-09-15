subjects=("python","sql","excel")
marks={
    "python":85,
    "sql":78,
    "excel":92
}
total=sum(marks.values())
average=total/len(subjects)

print("subjects: ",subjects)
print("marks: ",marks)
print("total marks: ",total)
print("average marks: ",average)