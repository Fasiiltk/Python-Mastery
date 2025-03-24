# file_reader_writer.py
while True:
    print("\n1. Write to file\n2. Read file\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        text = input("Enter text: ")
        with open("myfile.txt", "a") as f:
            f.write(text + "\n")
    elif choice == "2":
        try:
            with open("myfile.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found!")
    elif choice == "3":
        break
    else:
        print("Invalid choice")