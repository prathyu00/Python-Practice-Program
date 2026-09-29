employees = [
    {"name": "appu", "salary": 45000000.50, "active": True},
    {"name": "prathyush", "salary": 52000000.75, "active": False},
]

for emp in employees:
    status = "Active" if emp["active"] else "Inactive"
    print(f"{emp['name']} earns {emp['salary']} and is{status}")