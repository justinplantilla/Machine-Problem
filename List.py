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
                    break

        print(f"Current listko: {listko}")
        continue
    
    elif choice == 2:
        while True:
            num_input = int(input("How many elements you want to insert: "))
            print("=========================================================")

            try:
                while True:
                    num_input = int(num_input)

                    for i in range(num_input):
                        data_type = input("What data type you want to insert: ").upper()

                        if data_type == "STRING":
                            try:
                                data_store = input("Enter the element you want to insert: ")
                                data_index = int(input("Enter the index you want to position youe element: "))
                                listko.insert(data_index, data_store)
                                break
                            except ValueError:
                                print("Invalid input. Please Enter whole number for index. ")
                        
                        elif data_type == "INT":
                            try:
                                data_store = int(input("Enter the element you want to insert: "))
                                data_index = int(input("Enter the index you want to position youe element: "))
                                listko.insert(data_index, data_store)
                                break
                            except ValueError:
                                print("Invalid input. Please Enter whole number for index. ")
                        
                        elif data_type == "FLOAT":
                            try:
                                data_store = float(input("Enter the element you want to insert: "))
                                data_index = int(input("Enter the index you want to position youe element: "))
                                listko.insert(data_index, data_store)
                                break
                            except ValueError:
                                print("Invalid input. Please Enter whole number for index. ")

                        elif data_type == "BOOLEAN":
                            try:
                                data_store = input("Enter the element you want to insert (True/False): ").capitalize()
                                if data_store in ["True", "False"]:
                                    data_store = (data_store == "True")
                                data_index = int(input("Enter the index you want to position youe element: "))
                                listko.insert(data_index, data_store)
                                break
                            except ValueError:
                                print("Invalid input. Please Enter whole number for index. ")

                    print(f"Current list: {listko}")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
            continue 
                

    elif choice == 3:
        while True:
            num_input = int(input("How many elements you want to remove: "))
            print("=========================================================")

            try:
                while True:
                    num_input = int(num_input)

                    for i in range(num_input):
                        data_type = input("What data type you want to remove: ").upper()

                        if data_type == "STRING":
                            try:
                                data_remove = input("Enter the element you want to remove: ")
                                if data_remove not in listko:
                                    print(f" '{data_remove}' is not found in the listko. ")
                                    break
                                else:
                                    listko.remove(data_remove)
                                    print(f"'{data_remove}' has been removed to the listko. ")
                                break
                            except ValueError:
                                print("Invalid input. Please enter string")
                        
                        elif data_type == "INT":
                            try:
                                data_remove = int(input("Enter the element you want to remove: "))
                                if data_remove not in listko:
                                    print(f" '{data_remove}' is not found in the listko. ")
                                    break
                                else:
                                    listko.remove(data_remove)
                                    print(f"'{data_remove}' has been removed to the listko. ")
                                break
                            except ValueError:
                                print("Invalid input. Please enter whole number.")
                        
                        elif data_type == "FLOAT":
                            try:
                                data_remove = float(input("Enter the element you want to remove: "))
                                if data_remove not in listko:
                                    print(f" '{data_remove}' is not found in the listko. ")
                                    break
                                else:
                                    listko.remove(data_remove)
                                    print(f"'{data_remove}' has been removed to the listko. ")
                                break
                            except ValueError:
                                print("Invalid input. Please enter number with decimal.")

                        elif data_type == "BOOLEAN":
                            try:
                                data_remove = input("Enter the element you want to remove (True/False): ").capitalize()
                                if data_remove in ["True", "False"]:
                                    data_remove = (data_remove == "True")
                                if data_remove not in listko:
                                    print(f" '{data_remove}' is not found in the listko. ")
                                    break
                                else:
                                    listko.remove(data_remove)
                                    print(f"'{data_remove}' has been removed to the listko. ")
                                break
                            except ValueError:
                                print("Invalid input. Please enter TRUE or False")

                    print(f"Current list: {listko}")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            continue 

    elif choice == 4:
        while True:
            num_input = int(input("How many elements you want to pop: "))
            print("=========================================================")

            try:
                num_input  = int(num_input)
                
                for i in range(num_input):
                    while True:
                        try:
                            data_pop = int(input("Enter the index number of element you want to pop: "))
                            popped_element = listko.pop(data_pop)
                            print(f"'{popped_element}' has been popped.")
                            break
                        except IndexError:
                            print("Enter valid Index.")
                        except ValueError:
                            print("Enter whole number.")
           
            except ValueError:
                print("Enter element that in the list.")
            print(f"Current list: {listko}")
            continue
        

    elif choice == 5:
        while True:
            listko.clear()
            print("List successfully cleared.")
            break
        print(f"Current list: {listko}")
        continue
    
    elif choice == 6:
        element = input("Enter element to find index: ")
        try:
            index = listko.index(eval(element))
            print(f"Index of '{element}': {index}")
        except ValueError:
            print(f"'{element}' not found in the list.")
        except:
            print("Invalid input.")
        continue

    
    elif choice == 7:
        element = input("Enter element to count: ")
        try:
            count = listko.count(eval(element))
            print(f"'{element}' occurs {count} time(s).")
        except:
            print("Invalid input.")
        continue

    
    elif choice == 8:
        try:
            listko.sort()
            print("List sorted.")
        except TypeError:
            print("Cannot sort list with mixed data types.")
        print(f"Current listko: {listko}")
        continue

    
    elif choice == 9:
        listko.reverse()  
        print("List reversed.")
        print(f"Current listko: {listko}")
        continue

    
    elif choice == 10:
        print(f"Current listko: {listko}")
        continue

    
    elif choice == 11:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose from 1-11.")
        continue
