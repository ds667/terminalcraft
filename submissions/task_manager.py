import os

tasks = []

def show_tasks():
    if not tasks:
        print("\n✅ No tasks yet!\n")
    else:
        print("\n📋 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print()

def add_task():
    task = input("\nEnter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Task '{task}' added!\n")

def remove_task():
    show_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"❌ Removed task '{removed_task}'!\n")
        else:
            print("⚠️ Invalid task number!\n")
    except ValueError:
        print("⚠️ Please enter a valid number!\n")

def save_and_exit():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("\n💾 Tasks saved to 'tasks.txt'. Goodbye!\n")
    exit()

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())

def main():
    load_tasks()
    while True:
        print("1️⃣ Show Tasks\n2️⃣ Add Task\n3️⃣ Remove Task\n4️⃣ Exit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            save_and_exit()
        else:
            print("⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
