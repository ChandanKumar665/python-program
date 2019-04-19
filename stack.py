# implementing stack using array
stack = []
# we are declaring top but it's an unmutable object we can't perform
# re-assignment to the top variable. so we have to make it as mutable object
# thats why we are using global key word other wise we will get LocalUnboundError.
# after using global keyword we can able to perform re-assignment to the top variable
# and it will become mutable object.
top = -1
max_size = 5

def push(item):
	global top
	if not top == max_size-1:
		stack.append(item)
		top = top + 1
		print('{} item has been added into stack'.format(item))
	else:
		print('Stack is full.')	

def pop():
	global top
	if not isEmpty():
		print('Stack is empty. Deletion is not possible')
		return
	stack.pop(top)
	top -= 1
	print('item deleted successfully from stack')	

def isEmpty():
	# print(top)
	return False if top == -1 else True

def peek():
	if not isEmpty():
		print('Stack is empty.')
		return
	print(stack[top])	

def display():
	if not isEmpty():
		print('Stack is empty.')
		return
	print(stack)	


while True:
	print('1. Insert')
	print('2. Show')
	print('3. Peek')
	print('4. Delete')
	print('5. Exit')
	choice = int(input('Enter your choice'))
	if choice == 1:
		item = int(input('Enter element to insert'))
		push(item)
	elif choice == 2:
		display()
	elif choice == 3:
		peek() 
	elif choice == 4:
		pop()		
	elif choice == 5:
		print('Thanks...')
		exit()
	else:
		print('no choice matched')
		exit()						