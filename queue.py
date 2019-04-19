# array implementation of queue
queue = [-1 for x in range(5)]
print(queue)
front = -1 
rear = -1
max_size = 5

def isEmpty():
	return True if front == -1 and rear == -1 else False

def isFull():
	if front == 0 and rear == max_size-1:
		return True
	elif rear == front-1:
		return True
	else:
		return False		

def enqueue(item):
	global front,rear			
	# print(item)
	if not isFull():
		if front == -1 and rear == -1:
			front = 0
			rear += 1
			queue[rear] = item
		else:
			rear = (rear + 1) % (max_size)
			print('rear is: ',rear)
			print('queue[rear] is :',queue[rear])
			queue[rear]	= item
		print('{} enqueued to queue'.format(item))
		return 
	print('Queue is overflow.')
	
def dequeue():
	global front,rear
	if not isEmpty():
		if front == rear:
			queue[front] = -1
			front = (front + 1) % max_size
			front = rear = -1
		else:
			queue[front] = -1
			front = (front + 1) % max_size	
		print('{} dequeued to queue'.format(queue[front-1]))
		return 
	print('Queue is underflow.')	

def show():
	if not isEmpty():
		print(queue)
		return			
	print('Queue is underflow.')

def peek():
	if not isEmpty():
		print('front: ',front)
		print('rear: ',rear)
		return			
	print('Queue is underflow.')		

while True:
	print('1. Enqueue')
	print('2. Show')
	print('3. Peek')
	print('4. Dequeue')
	print('5. Exit')
	choice = int(input('Enter your choice'))
	if choice == 1:
		item = int(input('Enter element to insert'))
		enqueue(item)
	elif choice == 2:
		show()
	elif choice == 3:
		peek() 
	elif choice == 4:
		dequeue()		
	elif choice == 5:
		print('Thanks...')
		exit()
	else:
		print('no choice matched')
		exit()						
