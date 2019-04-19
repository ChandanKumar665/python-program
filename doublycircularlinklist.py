# Circular link list

# implementation of linked list
import time

class DoublyCircularLinkList:
	start = None
	# i = 1001 
	def __init__(self, data = None, prev = None, next = None):
		self.data = data
		self.prev = prev
		self.next = next
	@classmethod	
	def displayList(cls):
		if cls.start == None:
			print('List is empty. please create list first')
			return
		q = cls.start
		while(q.next != cls.start):
			print('|'+str(id(q.prev))+'|'+str(q.data)+'|'+str(id(q.next))+'|<---->',end = '')
			q = q.next
		# we have to print the last node
		print('|'+str(id(q.prev))+'|'+str(q.data)+'|'+str(id(q.next))+'|') 

	def createList(self, data):
		link = DoublyCircularLinkList(data)
		DoublyCircularLinkList.start = link
		link.next = DoublyCircularLinkList.start
		link.prev = DoublyCircularLinkList.start
		print('list created successfully')

	def insert(self, data, at = '', pos = 0):
		if at == '' and pos == 0:
			# default; insert in last
			if DoublyCircularLinkList.start == None:
				print('list is empty')
				print('please wait while list is creating...')
				time.sleep(3)
				self.createList(data)
			else:
				#list is already created
				# iterate loop to last node
				q = DoublyCircularLinkList.start
				t = q
				while q.next != DoublyCircularLinkList.start:
					q = q.next
				link = DoublyCircularLinkList(data)
				link.next = DoublyCircularLinkList.start
				q.next = link
				link.prev = q
				t.prev = link
				print('data inserted successfully')
		elif at == 'start' or pos <= 0:
			#insert in begining
			if DoublyCircularLinkList.start == None:
				print('list is empty')
				print('please wait while list is creating...')
				time.sleep(3)
				self.createList(data)
			else:
				#list is already created
				q = DoublyCircularLinkList.start
				t = q
				link = DoublyCircularLinkList(data)
				# iterate till last node to update the last.next = link
				while q.next != DoublyCircularLinkList.start:
					q = q.next
				q.next = link	
				DoublyCircularLinkList.start = link
				link.prev = q
				link.next = t
				t.prev = link
				print('data inserted successfully at 1st position')
		elif pos > 1 and pos <= DoublyCircularLinkList.length():
			# at specified position
			if DoublyCircularLinkList.start == None:
				print('list is empty')
				print('please wait while list is creating...')
				time.sleep(3)
				self.createList(data)
			else:
				#list is already created
				# iterate loop till entered position
				q = DoublyCircularLinkList.start
				position = 1
				while position < pos-1:
					position += 1
					q = q.next
				link = DoublyCircularLinkList(data)
				link.next = q.next
				q.next = link
				print('data inserted successfully at {} position'.format(pos))		
	
	def pop(self, _pos=None,item=None):
		l = DoublyCircularLinkList.length()
		if l == 0:
			print('list empty')
			return
		if _pos != 0:
			if _pos	== 1:
				# delete 1st node
				q = DoublyCircularLinkList.start
				t = q
				while q.next != DoublyCircularLinkList.start:
					q = q.next
				DoublyCircularLinkList.start = t.next	
				q.next = DoublyCircularLinkList.start
				t.next.prev = q	
				t.next = None
				del t
				print('item deleted from 1st position')
			elif _pos <= 0:
				print("index value can't be -ve")
			elif _pos > l:
				print('index out of range')
			else:
				q = DoublyCircularLinkList.start
				i = 1
				while i < _pos-1:
					q = q.next
					i += 1
				t = q.next
				q.next = t.next
				if t.next == DoublyCircularLinkList.start:
					t.next = None
					DoublyCircularLinkList.start.prev = q
					del t
					return
				t.next.prev = q
				t.next = None
				del t
				print('{}rd position item has been deleted'.format(_pos))	
		elif item != None:
			q = DoublyCircularLinkList.start
			t = q
			if l == 1:
				if q.data == item:
					# delete that node
					
					DoublyCircularLinkList.start = None	
					del q
					del t
			else:
				while True:
					if q.data != item and q.next == DoublyCircularLinkList.start:
						print('item not found')
						return
					if q.data == item and q.next == DoublyCircularLinkList.start:
						# while q.next != DoublyCircularLinkList.start:
						# 	q = q.next
						# DoublyCircularLinkList.start = t.next	
						# q.next = DoublyCircularLinkList.start	
						t.next = q.next
						q.next = None
						DoublyCircularLinkList.start.prev = t
						del q
						break
					elif q.data == item:
						t.next = q.next
						q.next.prev = t 
						del q
						break
					t = q
					q = q.next
				print('item deleted')	



					

	@staticmethod		
	def length():
		count = 0
		if DoublyCircularLinkList.start == None:
			return count
		q = DoublyCircularLinkList.start	
		while q.next != DoublyCircularLinkList.start:
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
		link = DoublyCircularLinkList()
		link.insert(item,at,pos)
	elif choice == 2:
		DoublyCircularLinkList.displayList()
	elif choice == 3:
		print(DoublyCircularLinkList.length())
	elif choice == 4:
		position = int(input('Enter position'))
		item = ''
		if position == 0:
			item = int(input('Then Enter item'))
		DoublyCircularLinkList().pop(position,item)	
			
	elif choice == 5:
		print('Thanks...')
		exit()
	else:
		print('no choice matched')
		exit()			