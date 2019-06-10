import json
student={
    "name":"hacker",
    "age":12,
    "mobile":"123134421234"
}
print(type(student))
j_student=json.dumps(student)
print(type(j_student))
print("json对象是:{0}".format(j_student))
d_student = json.loads(j_student)
print(type(d_student))
print(d_student)