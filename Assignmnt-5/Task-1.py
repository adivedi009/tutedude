# Task 1: Create a Dictionary of Student Marks
def main():
    Dict = {'Alice': 85, 'Bob': 48, 'Common':85 }
    student = input('Enter student\'s name: ')
    if  Dict.__contains__(student):
        print(f'{student}\'s Marks: {Dict.get(student)}')
    else:
        print('Student not found')
    
if __name__ == "__main__":
    main()