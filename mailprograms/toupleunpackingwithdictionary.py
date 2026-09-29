students = [("appu", 88), ("Anu", 92), ("Kiran", 75)]
result = {}
for name, score in students:
    result[name] = score >= 80  

print(result)