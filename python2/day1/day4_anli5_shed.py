#!/usr/bin/env python3
stack=[]
def push_it():
    item = input('item to push:').strip()
    if item:
        stack.append(item)
def pop_it():
    if stack:
        print('From stack,pop: %s' % stack.pop())
def view_if():
    print('%s' % stack)
def show_menu():
    #把函数保存到一个名为cmds的字典中
    cmds = {'0':push_it,'1':pop_it,'2':view_if}
    prompt = """(0) push it
(1) pop it
(2) view it
(3) quit
Please input your choice(0/1/2/3):"""
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid input; Try again!')
            continue
        if choice == '3':
            break
        cmds[choice]()     #根据用户输入，在字典中取中函数，调出
        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # else:
        #     view_if()

if __name__=='__main__':
    show_menu()