import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("WELCOME TO THE PROGRAME")
    print("DATABASE LIBRARY")
    print("=========================")

    # check database exist / no
    CRUD.init_console()

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("WELCOME TO THE PROGRAME")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Enter Option: ")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        is_done = input("Are You (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print("Programe Done, Thank You!!")