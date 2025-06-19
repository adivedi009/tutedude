def main():
    inWrite = input("Enter text to write to the file: ")
    fopen = open("./output.txt", "r+")
    fopen.write(inWrite)
    print("Data successfully written to output.txt.")
    inWrite = input("Enter additional text to append: ")
    fopen.write("\n" + inWrite)  # Use write() with newline instead of append()
    print("Data successfully appended.")
    fopen.close()

    fopen = open("./output.txt", "r+")
    fread = fopen.read()
    print(f"The final content of the file is:")
    print(fread)

    fopen.close()

if __name__ == "__main__":
    main()
