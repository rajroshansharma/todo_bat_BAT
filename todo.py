from datetime import date
import pyfiglet

def give_time():
    today = date.today()
    return today


def pending_completed_counter():
    count_1 = 0
    counter_2 = 0
    # opening todo_list.txt file
    pending = open('C:/Users/rajro/PycharmProjects/untitled/todo.txt', 'r')
    for line in pending:
        count_1 = count_1 + 1
    pending.close()
    # opening done_list.txt file
    completed = open('C:/Users/rajro/PycharmProjects/untitled/done.txt', 'r')
    for lines in completed:
        counter_2 = counter_2 + 1
    completed.close()
    return count_1, counter_2  # returning the pending and completed numbers of each file


def print_report():
    date_1 = give_time()
    pending_completed = pending_completed_counter()
    print(f'{date_1} Pending : {pending_completed[0]}  completed : {pending_completed[1]}')


def print_menu():
    print('$ Usage :-')
    print('$ ./todo add "todo item"    #Add a new todo')
    print('$ ./todo ls                 #Show remaining todos')
    print('$ ./todo del NUMBER         #Delete a todo')
    print('$ ./todo done NUMBER        #Complete a todo')
    print('$ ./todo help               #Show usage')
    print('$ ./todo report             #Statistics')


def add_el(str_var):
    temp = str_var
    f = open('C:/Users/rajro/PycharmProjects/untitled/todo.txt', 'a')
    f.write('\n' + temp)
    f.close()


def print_ls():  # prints all the valid lists present in the .txt file
    def rev():  # calculates the total number of lists
        f1 = open('C:/Users/rajro/PycharmProjects/untitled/todo.txt', 'r')
        count2 = 0
        for m in f1:
            count2 = count2 + 1
        f1.close()
        return count2
    f = open('C:/Users/rajro/PycharmProjects/untitled/todo.txt', 'r')
    gth = rev()
    count1 = gth  # iterating from reverse(reverse counting)
    for j in f:
        print(f"[{count1}] {j}", end="")
        count1 = count1 - 1  # iterating from reverse
    f.close()


def done_el(num):
    cd = []
    f1 = open('C:/Users/rajro/PycharmProjects/untitled/todo.txt', 'r')
    for line in f1:
        cd.append(line)
    f1.close()
    num_var = len(cd) - num
    # var = num - 1  # index to be deleted
    var2 = cd[num_var]  # storing the value to shift into done list
    cd.pop(num_var)  # item is now deleted
    f2 = open('C:/Users/rajro/PycharmProjects/untitled/todo.txt', 'w')  # writing operation is going to perform
    for ln in range(len(cd)):
        f2.write(cd[ln])
    f2.close()
    # storing the done list into the file
    f3 = open('C:/Users/rajro/PycharmProjects/untitled/done.txt', 'a')
    f3.write(var2)
    f3.close()


def del_it(num):
    lg = []
    f12 = open('C:/Users/rajro/PycharmProjects/untitled/todo.txt', 'r')
    for line in f12:
        lg.append(line)
    f12.close()
    num_var = len(lg) - num
    lg.pop(num_var)
    f13 = open('C:/Users/rajro/PycharmProjects/untitled/todo.txt', 'w')
    for ln in range(len(lg)):
        f13.write(lg[ln])
    f13.close()


if __name__ == '__main__':
    while 1:
        start = str(input("$ "))
        if start == './todo':  # starter
            result = pyfiglet.figlet_format("Welcome")
            result2 = pyfiglet.figlet_format("Mr RAZ")
            print(result + result2)
            print_menu()
            while 1:
                command = ['./todo add', './todo ls', './todo del ', './todo done', './todo help', './todo report']
                index = 0
                count = 0
                command_input = str(input("\n$ "))
                com1 = command_input[:11]
                c = len(command_input) - 1
                com2 = command_input[12:c]
                com3 = command_input[12:]
                com4 = command_input[10:]
                com5 = command_input[:13]


                # print(com1)
                # print(com2)
                for i in range(len(command)):  # confirming that command is valid
                    if command[i] == com1 or command[i] == com5:
                        index = i

                variable = index
                #print(variable)

                if variable == 0:
                    count = count + 1
                    add_el(str(com2))
                    print(f'Added todo: "{com2}"')
                if variable == 1:
                    print_ls()
                if variable == 2:
                    del_it(int(com4))
                    print(f"Deleted todo #{com4}")
                if variable == 3:
                    var1 = int(com3)
                    done_el(var1)
                    print(f"Marked todo #{var1} as done.")
                if variable == 4:
                    print_menu()
                if variable == 5:
                    print_report()




