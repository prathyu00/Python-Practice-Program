student = {
    "name": "appu",       
    "age": 20,             
    "height": 6.0,               
    "subjects": ["Python", "Aiml", "cybersecurity"],   
    "address": ("karkala", "Karnataka"),      
    "hobbies": {"eating", "sleeping"},        
    "is_passed": True      
}
for key, value in student.items():
    print(f"{key}:{value} --{type(value).__name__}")