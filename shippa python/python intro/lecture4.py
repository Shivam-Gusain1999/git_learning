# dictionary = {
#    "table" : ("a piece of furniture", "kuch bhii"),
#    "cat": "a small animal",

# }
# print(dictionary)

# classroom = {"java", "python", "python", "java", "javascript", "c", "c", "c++", "c++"}
# print(len(classroom))

dictionary = {}
maths = input("enter the marks of maths :")
dictionary.update({"mathss" : maths})
physics = input("enter the marks of physics :")
dictionary.update({"physiccs": physics})
computer = input("enter the marks of computer :")
dictionary.update({"computer": computer} )

print(dictionary)