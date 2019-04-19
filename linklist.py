# implementation of linked list
import time

class LinkList:
	start = None
	i = 1001 
	def __init__(self,data = None, next = None):
		self.data=data
		self.next=next
	@classmethod	
	def displayList(cls):
		if cls.start == None:
			print('List is empty. please create list first')
			return
		q = cls.start
		while(q.next != None):
			print('|'+str(q.data)+'|'+str(id(q.next))+'|---->',end = '')
			q = q.next
		# we have print the last node
		print('|'+str(q.data)+'|'+'X'+'|') 

	def createList(self, data):
		link = LinkList(data)
		LinkList.start = link
		link.next = None
		print('list created successfully')

	def insert(self, data, at = '', pos = 0):
		if at == '' and pos == 0:
			# default; insert in last
			if LinkList.start == None:
				print('list is empty')
				print('please wait while list is creating...')
				time.sleep(3)
				self.createList(data)
			else:
				#list is already created
				# iterate loop to last node
				q = LinkList.start
				while q.next != None:
					q = q.next
				link = LinkList(data)
				q.next = link
				print('data inserted successfully')
		elif at == 'start' or pos <= 0:
			#insert in begining
			if LinkList.start == None:
				print('list is empty')
				print('please wait while list is creating...')
				time.sleep(3)
				self.createList(data)
			else:
				#list is already created
				q = LinkList.start
				link = LinkList(data)
				link.next = q
				q = link
				LinkList.start = q
				print('data inserted successfully at 1st position')
		elif pos > 0 and pos <= LinkList.length():
			# at specified position
			if LinkList.start == None:
				print('list is empty')
				print('please wait while list is creating...')
				time.sleep(3)
				self.createList(data)
			else:
				#list is already created
				# iterate loop till entered position
				q = LinkList.start
				position = 1
				while position < pos-1:
					position += 1
					q = q.next
				link = LinkList(data)
				link.next = q.next
				q.next = link
				print('data inserted successfully at {} position'.format(pos))		
	def pop(self, _pos=None,item):
		l = LinkList.length()
		if l == 0:
			print('list empty')
			return
		if _pos != None:
			if _pos	== 1:
				# delete 1st node
				q = LinkList.start
				LinkList.start = q.next
				q.next = None
				del q
				print('item deleted from 1st position')
			elif _pos <= 0:
				print("index value can't be -ve")
			elif _pos > l:
				print('index out of range')
			else:
				q = LinkList.start
				i = 1
				while i < _pos-1:
					q = q.next
					i += 1
				t = q.next	
				q.next = t.next
				t.next = None
				del t
				print('{}rd position item has been deleted'.format(_pos))	
		elif item != None:
			q = LinkList.start
			t = q
			if l == 1:
				if q.data == item:
					# delete that node
					t = LinkList.start
					LinkList.start = node
					del t
			else:
				while True:
					if q.data == item and q == start:
						LinkList.start = q.next
						q.next = None
						del q
						break
					elif q.data == item:
						t.next = q.next
						q.next = None
						del q
						break
					t = q
					q = q.next
				print('item deleted')

	@staticmethod		
	def length():
		count = 0
		if LinkList.start == None:
			return count
		q = LinkList.start	
		while q.next != None:
			count += 1
			q = q.next
		count += 1
		return (count)	


while True:
	print('1. Insert')
	print('2. Show')
	print('3. Count')
	print('4. Delete')
	print('5. Exit')
	choice = int(input('Enter your choice'))
	if choice == 1:
		item = int(input('Enter element to insert'))
		at = input("Enter the position start/'' ?")
		pos = int(input('Enter position'))
		link = LinkList()
		link.insert(item,at,pos)
	elif choice == 2:
		LinkList.displayList()
	elif choice == 3:
		print(LinkList.length())
	elif choice == 4:
		position = int(input('Enter position'))
		item = ''
		if position == 0:
			item = int(input('Then Enter item'))
		LinkList().pop(position,item)	
			
	elif choice == 5:
		print('Thanks...')
		exit()
	else:
		print('no choice matched')
		exit()			