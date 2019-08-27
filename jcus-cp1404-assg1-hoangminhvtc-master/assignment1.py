
"""
Replace the contents of this module docstring with your own details
Name:Dam Hoang Minh
Date started: 15/08/2019
Program: Travel tracker
GitHub URL:https://github.com/hoangminhvtc/CP1404
"""

# The program will load the places from places.csv
# A menu is displayed so that user can make choices: listing all Destination, add a destination or visited destination
# The program then saves user's changes, then edits the original csv file
# Open the places.csv file  then assign it to a variable(FILES) for the 4 functions of menu(),list(),add(),and visited()

input_file = open("places.csv","r")
FILES = input_file.readlines()
TOTAL = [0]
REMAINDER = [1]
EXPORT_LIST = []

'''main() function serves the purpose of only displaying the intial message,and then moving forward directly to the menu() function'''
def main():
    print("Travel Tracker - by <Dam Hoang Minh>")
    first = menu()

    '''menu() function display the three main options of the program for user to access the three main functions(L - List, A - Add, C - visted, and Q - Quit)
    The Q - Quit option allows the user to save all the changes or input in the place list to the csv file itself, overwrite the place list '''
def menu():
    print("A - Destination List")
    print("S - Add a new destination")
    print("D - Destination visited")
    print("Q - Quit")
    option = input("Please select ").upper()

    while option not in ['A', 'S', 'D', 'Q']:
        option = input("Invalid choice, please make another option").upper()
    if option == "A":
        list()
    elif option == "S":
        add()
    elif option == "D":
        visited()
    else:
        confirm = input("Are you sure you want to quit? - (Y) Yes, (N) No ").upper()
        while confirm not in ['Y','N']:
            confirm = input("Invalid choice, please choose Y or N").upper()
        if confirm == "Y":
            print("-- Have a nice day  --")
        else:
            menu()

'''list functions displays all the values from the places.csv files (all stored in the FILES variable created above instead of having to directly access the csv file itself) in a neatly organized format at any point within the program, whether its before or after more data is inputed into the places.csv file'''
def list():
    list = []
    count = 0
    count_2 = 0
    for lines in FILES:
        count += 1
        new_lines = lines.split(",")
        place_name = new_lines[0]
        country_name = new_lines[1]
        priority = new_lines[2]
        status = new_lines[3].replace("v", "*").replace("n", "").replace("\n", "")
        list.append(count)
        final_place_list = ("{:>2}. {:<1} {:<35} - {:<35} ({})".format(count, status, place_name, country_name, priority))
        print(final_place_list)
        if "*" in status:
            count_2 += 2
    print("-" * 86)
    print("Total number of places:", max(list))
    TOTAL.append(max(list))
    print("Number of places visited:", max(list) - count_2)
    print("Number of places left to visit:", count_2)
    REMAINDER.append(count_2)
    print("-" * 86)
    menu()

'''add function serves the purpose of allowing the user to add data to the FILES varible which would be printed and formatted appropriately in the list() function'''
def add():
    remove_status ="v\n"
    place_name2 = input("Enter a destination:")
    while place_name2 in ["", " ", "  ", "   "]:
        print("Destination is blank, Please type a destination ")
        place_name2 = input("Enter a destination:")
    country_name2 = input("Enter destination's country:")
    while country_name2 in ["", " ", "  ", "   "]:
        print("Country is blank, Please type destination's country")
        country_name2 = input("Enter a country:")
    flag=True
    while (flag==True):
        try:
            priority_2 = int(input("Enter priority: "))
            flag = False
        except ValueError:
            print("Invalid input, please enter a number")
    if REMAINDER[-1] == 0:
        REMAINDER.remove(REMAINDER[-1])
    result_1 = ("{},{},{},{}".format(place_name2, country_name2, priority_2, remove_status))
    FILES.append(result_1)
    EXPORT_LIST.append(result_1)
    print("{} from {} with priority ({}) added to Destination list".format(place_name2, country_name2, priority_2))
    print("-" * 86)
    menu()

'''the visited() function serves the purpose of allowing the user to mark the places within the list as visited but user is required to list the destination before mark them as "visted"'''
def visited():
 flag=True
    while (flag==True):
        try:
            number = int(input("Enter the number of a destination to be marked as visited"))
            flag = False
        except ValueError:
            print("Invalid input, please enter a number")
    if max(TOTAL) == 0:
        print("Please load the destination list ")
        menu()
    while number > max(TOTAL):
        print("Invalid input")
        number = int(input("To mark the visited destination , please type the order number of destination"))
    rows = FILES[number - 1]
    new_rows = rows.split(",")
    place_name3 = new_rows[0]
    country_name3 = new_rows[1]
    priority_3 = new_rows[2]
    result_3 = ("{},{},{},{}".format(place_name3, country_name3, priority_3, remove_status))
    result_4 = ("=> '{} from {} with priority {}' visited".format(place_name3, country_name3, priority_3))
    FILES.append(result_3)
    FILES.remove(FILES[number - 1])
    print(result_4)
    print("-" * 86)
    menu()
main()


