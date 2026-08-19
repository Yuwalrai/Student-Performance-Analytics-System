from reports import (
    line_width,
    build_dashboard
)

from students_report import (
    display_student_report
)

from ranking import (
    build_leaderboard
)
def display_menu() :
    section = "=" * line_width + "\n"
    section += "STUDENT PERFORMANCE ANALYTICS SYSTEM".center(line_width) + "\n"
    section += "=" * line_width + "\n"
    section += "1. Search Student Report\n"
    section += "2. View Leaderboard\n"
    section += "3. View Dashboard\n"
    section += "4. Exit\n"
    section += "=" * line_width + "\n"
    section += "Enter your choice: \n"

    return section

def get_menu_choice() : 
    while True :
        try :
            choice = int(input("Please enter a number between 1 and 4: "))
            if  1 <= choice <= 4 :
                return choice
            else:
                print("Incorrect! That number is not between 1 and 4.")
        except ValueError :
            print("Invalid input!. Please enter a number between 1 and 4.")

def handle_search(df) :
    while True :
        try :
            search_roll = int(input("Please enter the roll number of students: "))
            if search_roll in df["roll no."].values :
                detail_option = ["short","detailed"]
                while True :
                    detail_level = input("please input the detail level 'short' or 'detailed'")
                    if detail_level not in detail_option :
                        print("⚠️ Warning: Invalid choice detected.")
                    else :
                        section = display_student_report(df, search_roll, detail_level)
                        return section      
            else :
                print(f"The student does not exist with the roll number of {search_roll}")
        except ValueError :
            print("Invalid input!. Please enter a valid roll number.")


def handle_leaderboard(df) :
    while True :
        try :
            max_rank = int(input("Please enter the total rank you want to see: "))
            if 0 < max_rank <= len(df) :
                section = build_leaderboard(df,max_rank)
                return section
            else :
                print("Invalid rank!. Please enter a valid rank.")

        except ValueError :
            print("Invalid input!. Please enter a valid rank you want to see.")

def handle_dashboard(df) :
    section =  build_dashboard(df)
    return section

def handle_exit() :
    section = "=" * line_width + "\n"
    section += "Thank you for using the Student Performance\n".center(line_width) + "\n"
    section += "Analytics System!".center(line_width) + "\n"
    section += "=" * line_width + "\n"
    return section


def run_menu(df) :
    while True :
        show_menu = display_menu()
        print(show_menu)
        choice = get_menu_choice()
        print(choice)

        if choice == 1 :
            search_report = handle_search(df)
            print(search_report)
        elif choice == 2 :
            show_leaderboard = handle_leaderboard(df)
            print(show_leaderboard)
        elif choice == 3 :
            show_dashboard = handle_dashboard(df)
            print(show_dashboard)
        elif choice == 4 :
            exit = handle_exit()
            print(exit)
            break

