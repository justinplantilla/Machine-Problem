listko = []

while True:
    print("\nChoose number to perform operation")
    print("1. Append")
    print("2. Insert")
    print("3. Remove")
    print("4. Pop")
    print("5. Clear")
    print("6. Index")
    print("7. Count")
    print("8. Sort")
    print("9. Reverse")
    print("10. View listko")
    print("11. Exit")

    user_input = input("Enter choice to perform: ")

    try:
        choice = int(user_input)
    except ValueError:
        print("Invalid choice. Please enter a number.")
        continue

    if choice == 1:
        try:
            num_input = int(input("How many elements you want to append: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        for _ in range(num_input):
            while True:
                data_type = input("What data type you want to append (STRING, INT, FLOAT, BOOLEAN): ").upper()
                if data_type == "STRING":
                    data_store = input("Enter string: ")
                    listko.append(data_store)
                    break
                elif data_type == "INT":
                    try:
                        data_store = int(input("Enter integer: "))
                        listko.append(data_store)
                        break
                    except ValueError:
                        print("Invalid input. Enter a whole number.")
                elif data_type == "FLOAT":
                    try:
                        data_store = float(input("Enter float: "))
                        listko.append(data_store)
                        break
                    except ValueError:
                        print("Invalid input. Enter a decimal number.")
                elif data_type == "BOOLEAN":
                    data_store = input("Enter boolean (True/False): ").capitalize()
                    if data_store in ["True", "False"]:
                        listko.append(data_store == "True")
                        break
                    else:
                        print("Invalid input. Enter True or False.")
                else:
                    print("Invalid data type. Choose STRING, INT, FLOAT, BOOLEAN.")

        print(f"Current listko: {listko}")

    elif choice == 2:
        try:
            num_input = int(input("How many elements you want to insert: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        for _ in range(num_input):
            while True:
                data_type = input("What data type you want to insert (STRING, INT, FLOAT, BOOLEAN): ").upper()
                if data_type == "STRING":
                    data_store = input("Enter string: ")
                elif data_type == "INT":
                    try:
                        data_store = int(input("Enter integer: "))
                    except ValueError:
                        print("Invalid input. Enter a whole number.")
                        continue
                elif data_type == "FLOAT":
                    try:
                        data_store = float(input("Enter float: "))
                    except ValueError:
                        print("Invalid input. Enter a decimal number.")
                        continue
                elif data_type == "BOOLEAN":
                    val = input("Enter boolean (True/False): ").capitalize()
                    if val in ["True", "False"]:
                        data_store = val == "True"
                    else:
                        print("Invalid input. Enter True or False.")
                        continue
                else:
                    print("Invalid data type.")
                    continue

                try:
                    data_index = int(input("Enter index: "))
                    listko.insert(data_index, data_store)
                    break
                except ValueError:
                    print("Invalid input. Enter whole number for index.")

        print(f"Current listko: {listko}")

    elif choice == 3:
        try:
            num_input = int(input("How many elements you want to remove: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        for _ in range(num_input):
            data_remove = input("Enter the element you want to remove (case sensitive): ")
            if data_remove.isdigit():
                data_remove = int(data_remove)
            elif data_remove.lower() == "true":
                data_remove = True
            elif data_remove.lower() == "false":
                data_remove = False
            else:
                try:
                    data_remove = float(data_remove)
                except:
                    pass

            if data_remove in listko:
                listko.remove(data_remove)
                print(f"'{data_remove}' has been removed.")
            else:
                print(f"'{data_remove}' not found in list.")

        print(f"Current listko: {listko}")

    elif choice == 4:
        try:
            num_input = int(input("How many elements you want to pop: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        for i in range(num_input):
            try:
                index = int(input("Enter index to pop: "))
                popped = listko.pop(index)
                print(f"Popped element: {popped}")
            except IndexError:
                print("Invalid index.")
            except ValueError:
                print("Enter a whole number.")

        print(f"Current listko: {listko}")

    elif choice == 5:
        listko.clear()
        print("listko successfully cleared.")
        print(f"Current listko: {listko}")

    elif choice == 6:
        element = input("Enter element to find index: ")
        try:
            index = listko.index(eval(element))
            print(f"Index of '{element}': {index}")
        except ValueError:
            print(f"'{element}' not found in the list.")
        except:
            print("Invalid input.")

    elif choice == 7:
        element = input("Enter element to count: ")
        try:
            count = listko.count(eval(element))
            print(f"'{element}' occurs {count} time(s).")
        except:
            print("Invalid input.")

    elif choice == 8:
        try:
            listko.sort()
            print("List sorted.")
        except TypeError:
            print("Cannot sort list with mixed data types.")
        print(f"Current listko: {listko}")


    elif choice == 9:
        listko.reverse() 
        print("List reversed.")
        print(f"Current listko: {listko}")

    elif choice == 10:
        print(f"Current listko: {listko}")

    elif choice == 11:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose from 1-11.")
