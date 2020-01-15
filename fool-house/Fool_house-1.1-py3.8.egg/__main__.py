from fool_house import schizo_count, from_int_to_schizo_str
print("Welcome to durka shell")

while True:
    command = input("corpsman>").split()
    if command[0] == "exit":
        break
    if command[0] == "num":
        print(from_int_to_schizo_str(command[1]))
    elif command[0] == "help":
        print("Каждый уважающий себя математик должен знать счёт древних шизов")
        for digit in schizo_count:
            print(digit)
        print("Так считали наши шизопредки")
