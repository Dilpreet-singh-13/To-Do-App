class ToDoList:
    def __init__(self):
        self.list = []

    def listAdd(self):

        value = input("Enter the task you want to add: ")
        self.list.append(["x", value])
        print("Task added successfully\n")

    def listDisplay(self):

        if not self.list:
            print("No items in the list\n")
        else:
            i = 0
            print("Index\tStatus\tTask")
            for item in self.list:
                print(f"{i}\t{item[0]}\t {item[1]}")
                i+=1

    def listElementDelete(self):
        
        index = int(input("Enter the index of the task you want to delete: "))

        if 0 <= index < len(self.list):
            item = self.list[index][1]
            self.list.pop(index)
            print(f"{item} - task deleted successfully\n")
        else:
            print("Invalid index")

    def markAsDone(self):

        index = int(input("Enter the index of the task you want to mark as done: "))

        if 0 <= index < len(self.list):
            if self.list[index][0] !="Y":
                self.list[index][0] = "Y"
                print(f"{self.list[index]}")
            else:
                print("Task already marked as done!\n")
        
class user(ToDoList):

    def __init__(self, name = "user1"):
        self.username = name
        self.ToDoList = ToDoList()



def main():
    users = {}

    choice = "Y"
    while choice == "y" or choice == "Y":

        print(
        '''
        OPTIONS
        1 - Open user
        2 - Add user
        3 - Delete user
        4 - List users
        '''
            )

        num = int(input("Enter you option: "))

        if num == 1:
            if not users:
                print("No users exist, add a user first.\n")
            else:
                name = input("Enter your username: ")
                if name not in users:
                    print("No such user exists!\n")
                else:    
                    choice2 = "y"
                    while choice2 == "y" or choice2 == "Y":
                        print(
                        '''
                        OPTIONS
                        1 - Display the list
                        2 - Add an task
                        3 - Mark task as done
                        4 - Delete task
                        ''' 
                            )

                        option = int(input("Enter your option: "))
                        match option:
                            case 1:
                                users[name].ToDoList.listDisplay()
                            case 2:
                                users[name].ToDoList.listAdd()
                            case 3:
                                users[name].ToDoList.markAsDone()
                            case 4:
                                users[name].ToDoList.listElementDelete()
                            case _:
                                print("Incorrect option!")
                        choice2 = input(f"Do you want to continue in user {name}? y = yes, n = no : ")
        elif num == 2:
            name = input("Enter you username: ")
            if name in users:
                print("This username already exists.\n")
            else:
                users[name] = user(name)
                print(f"User {name} added successfully.\n")
        elif num == 3:
            if not users:
                print("No users to delete.\n")
            else:
                name = input("Enter the user whom you wish to delete: ")
                if name in users:
                    del users[name]
                    print(f"User {name} deleted successfully")
                else:
                    print("No such user to delete.\n")
        elif num == 4:
            if not users:
                print("No user to list")
            else:
                i = 0
                for key in users:
                    print(f"{i}. {key}")
                    i += 1
        else:
            print("Invalid option\n")
        choice = input('''\nDo you want to continue? y = yes, n = no : ''')


if __name__ == "__main__":
    main()