# file = open("practice.txt", "w")
# file.write("hi everyone,\n this is a text file python\n, we are learning python")
# file.close()

# with open("practice1.txt", "r") as file:
#      data = file.read()
# new_data = data.replace("python", "html")
# print(new_data)

# with open("practice1.txt", "w") as file:
#     file.write(new_data)

word = "texxt"
with open("practice1.txt", "r") as file:
    data = file.read()
    if(data.find(word)!= -1):
        print("found")
    else:
        print("not found")
