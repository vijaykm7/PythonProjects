
tasks=[]

def add_task(n):
    tasks.append(n)
    print("added task")

def del_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("task not found")    

def view_task():
    # for itoms in tasks
    if tasks:
        for id, itoms in enumerate(tasks,start=1):
            print(f"{id}.{itoms}")
    else:
        print("Tasks are empty")

def count():
    if tasks:
        n=0
        for i in tasks:
            n=n+1
        print(n)
    else:
        print("List is empty")

def main():
    while True:
        print("Slect the Below option")
        print("1. Add Tasks")
        print("2. Remove Tasks")
        print("3. View Tasks")
        print("4. quit")
        print("5. Could Elements")
        ch=input("Enter the option : ")


        if ch == '1':
            task=input("Enter the Task to add :")
            # print("adding task")
            add_task(task)
        elif ch == '2':
            task=input("Enter the task to remove : ")
            # print("removing task ..")
            print(task)
            while re.finditer("[a-zA-Z]","task"):
                print("These are string")
            else :
                print("its numbers ")
            # del_task(task)
        elif ch == '3':
            task=print("List of tasks")
            view_task()
        elif ch =='4':
            print("GogBye")
            break
        elif ch =='5':
            print("Total task number")
            count()
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()
