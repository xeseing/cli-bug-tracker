from bug import Bug
from storage import load_bugs, save_bugs

def add_bug():
    title = input("Enter bug title: ")
    description = input("Enter bug description: ")
    priority = input("Enter priority (Low/Medium/High): ")

    bug = Bug(title, description, priority)
    bugs = load_bugs()
    bugs.append(bug.to_dict())
    save_bugs(bugs)

    print("Bug added successfully.\n")


def view_bugs():
    bugs = load_bugs()
    if not bugs:
        print("No bugs found.\n")
        return

    for bug in bugs:
        print(f"ID: {bug['id']}")
        print(f"Title: {bug['title']}")
        print(f"Priority: {bug['priority']}")
        print(f"Status: {bug['status']}")
        print("-" * 40)


def update_bug():
    bug_id = input("Enter Bug ID to update: ")
    bugs = load_bugs()

    for bug in bugs:
        if bug["id"] == bug_id:
            print("Current Status:", bug["status"])
            new_status = input("Enter new status (Open/In Progress/Closed): ")
            bug["status"] = new_status
            save_bugs(bugs)
            print("Bug updated successfully.\n")
            return

    print("Bug not found.\n")



def delete_bug():
    bug_id = input("Enter Bug ID to delete: ")
    bugs = load_bugs()

    updated_bugs = [bug for bug in bugs if bug["id"] != bug_id]

    if len(updated_bugs) == len(bugs):
        print("Bug not found.\n")
    else:
        save_bugs(updated_bugs)
        print("Bug deleted successfully.\n")

def filter_bugs():
    status = input("Enter status to filter by (Open/In Progress/Closed): ")
    bugs = load_bugs()
    filtered_bugs = [bug for bug in bugs if bug["status"]== status]

    if not filtered_bugs:
        print("No bugs found with that status.\n")
        return

    for bug in filtered_bugs:
        print(f"ID: {bug['id']}")
        print(f"Title: {bug['title']}")
        print(f"Priority: {bug['priority']}")
        print(f"Status: {bug['status']}")
        print("-" * 40)


def main():
    while True:
        print("==== Bug Tracker ====")
        print("1. Add Bug")
        print("2. View Bugs")
        print("3. Update Bug")
        print("4. Delete Bug")
        print("5. Exit")
        print("6. Filter Bugs by Status")

        choice = input("Choose an option: ")

        if choice == "1":
            add_bug()
        elif choice == "2":
            view_bugs()
        elif choice == "3":
            update_bug()
        elif choice == "4":
            delete_bug()
        elif choice == "5":
            print("Exiting...")
            break
        elif choice == "6":
            filter_bugs()
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()