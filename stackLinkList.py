# stack implementation using link list

import time

class StackLinkList:
	start = None
	last = None
	i = 1001 
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	@classmethod	
	def displayList(cls):
		if cls.start == None:
			print('Stack is empty.')
			return
		q = cls.start
		while(q.next != None):
			print('|'+str(q.data)+'|'+str(id(q.next))+'|---->',end = '')
			q = q.next
		# we have print the last node
		print('|'+str(q.data)+'|'+'X'+'|') 

	def createList(self, data):
		link = StackLinkList(data)
		StackLinkList.start = link
		StackLinkList.last = link
		print('{} has been inserted successfully.'.format(data))

	# insert	
	def insert(self, data):
		if StackLinkList.start == None:
			print('Stack is empty')
			print('please wait while data is inserting...')
			time.sleep(2)
			self.createList(data)
		else:
			#list is already created
			# iterate loop to last node
			q = StackLinkList.start
			while q.next != None:
				q = q.next
			link = StackLinkList(data)
			q.next = link
			StackLinkList.last = link
			print('one item has been added into stack.')	

	def pop(self):
		l = StackLinkList.length()
		if l == 0:
			print('Stack is empty')
			return
		elif l == 1:
			StackLinkList.start = None
			print('one item has been deleted from stack.')
			return	
		q = StackLinkList.start
		t = q
		#iterate loop to last node 
		while q.next != None :
			t = q
			q = q.next 
		t.next = None
		StackLinkList.last = t
		del q
		print('one item has been deleted from stack.')	
	
	def peek(self):
		if StackLinkList.length() == 0:
			print('Stack is empty.')
			return
		print(str(StackLinkList.last.data))	

	@staticmethod		
	def length():
		count = 0
		if StackLinkList.start == None:
			return count
		q = StackLinkList.start	
		while q.next != None:
			count += 1
			q = q.next
		count += 1
		return (count)	
					
while True:
	print('1. Push')
	print('2. Show')
	print('3. peek')
	print('4. Pop')
	print('5. Exit')
	choice = int(input('Enter your choice'))
	if choice == 1:
		item = int(input('Enter element to insert'))
		link = StackLinkList()
		link.insert(item)
	elif choice == 2:
		StackLinkList.displayList()
	elif choice == 3:
		StackLinkList().peek()
	elif choice == 4:
		StackLinkList().pop()	
	elif choice == 5:
		print('Thanks...')
		exit()
	else:
		print('no choice matched')
		exit()		