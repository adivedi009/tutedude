def main():
    try:
        openFile = open("./task1.txt","r")
        readFile = openFile.readlines()
        print(type(readFile))
        for i, line in enumerate(readFile, 1):
            print(f"Line{i}: {line}")
        openFile.close()
    except FileNotFoundError:
        print("Error: The file was not found.")

if __name__ == "__main__":
    main()