def write_data():
    data = input("Enter the data you want to write into the file: ")
    
    file = open("file.txt", "w")
    file.write(data + '\n')
    
def append_data():
    data = input("Enter the data you want to append to the file: ")
    
    file = open("file.txt", "a")
    file.write(data +'\n')
    file.close()
    
    
def read_data():
    
    file = open('file.txt', 'r')
    for line in file.readlines():
        print(line.strip())
    file.close()
    
while True:
    choice = input("Enter the desired choice (read/write/append) or q to quit: ").lower().strip()
    if choice =="q":
        print("Nice time ")
        break
    if choice == "read":
        read_data()
    elif choice == "write":
        write_data()
    elif choice == "append":
        append_data()
    else:
        print("Invalid input, try again!")
        continue
        