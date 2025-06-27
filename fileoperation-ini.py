with open("devops.txt", "r") as file:
    content = file.read()
    print(content)
with open("devops.txt", "w") as file:
    file.write("Hello User\n")
with open("devops.txt", "a") as file:
    file.write("What are you doing?")
