def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    newList = list1[:5]
    print(f"Original list: {list1}")
    print(f"Extracted first five elements: {newList}")
    newList.reverse()
    print(f"Reversed extracted elements: {newList}")


if __name__ == "__main__":
    main()