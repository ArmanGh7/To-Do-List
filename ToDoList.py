import sys
import csv


class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
        }


class ToDoList:
    def __init__(self):
        self.task_list = []

    def add_task(self, name, description, priority):
        task = Task(name, description, priority)
        self.task_list.append(task.to_dict())

    def show_tasks(self):
        number = 1
        for task in self.task_list:
            print(
                f"({number})\nname: {task["name"]}\ndescription: {task["description"]}\npriority: {task["priority"]}"
            )
            number += 1

    def delete_task(self, number):
        if number > len(self.task_list) or number < 1:
            print("Task not found!")
        else:
            del self.task_list[number - 1]

    def export_csv(self):
        with open("export_tasks.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["name", "description", "priority"]
            )
            writer.writeheader()
            writer.writerows(self.task_list)

    def import_csv(self):
        filename = input("Enter the CSV filename: ")

        try:
            with open(filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.task_list.append(row)

        except FileNotFoundError:
            print("File not found!")


print("==========")
print("To-Do List")
print("==========")

todo = ToDoList()

while True:

    print(
        "\n1. Add task\n2. Delete task\n3. Show all tasks\n4. Save all tasks as CSV\n5. Import tasks from CSV\n"
    )
    check = False
    while check is False:
        try:
            answer = int(input("Enter option(Enter 0 to exit): "))
        except ValueError:
            print("Please enter valid number!")
        else:
            if answer > 5 or answer < 0:
                print("Please enter valid number!")
            else:
                check = True

    if answer == 0:
        sys.exit()

    elif answer == 1:
        name = input("Task name: ")
        description = input("Add description: ")
        priority = input("Set priority: ")

        todo.add_task(name, description, priority)

    elif answer == 2:
        number = int(input("Enter task number to delete: "))
        todo.delete_task(number)

    elif answer == 3:
        todo.show_tasks()

    elif answer == 4:
        todo.export_csv()

    elif answer == 5:
        todo.import_csv()
