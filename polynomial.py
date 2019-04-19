import time
class LinkList1:
	start = None
	i = 1001 
	def __init__(self, coeff = None, exp = None, next = None):
		self.coeff = coeff
		self.exp = exp
		self.next = next

	def insert(self, coeff, exp):
	# default; insert in last
		if LinkList1.start == None:
				print('list is empty')
				print('please wait while list is creating...')
				time.sleep(2)
				# create a new list
				link = LinkList1(coeff,exp)
				LinkList1.start = link
				# print(str(id(LinkList1.start)))
				print('list created successfully')
		else:
			#list is already created
			# iterate loop to last node
			q = LinkList1.start
			while q.next != None:
				q = q.next
			link = LinkList1(coeff,exp)	
			q.next = link
			print('data inserted successfully')
	

	@classmethod	
	def displayList(cls):
		if cls.start == None:
			print('List is empty. please create list first')
			return
		q = cls.start
		print('list1---',id(q))
		while(q.next != None):
			print(str(q.coeff)+'x'+str(q.exp)+' ', end=' ')
			q = q.next
		# we have to print the last node also
		print(str(q.coeff)+'x'+str(q.exp)+' ') 	

class LinkList2:
	start = None
	i = 1001 
	def __init__(self, coeff = None, exp = None, next = None):
		self.coeff = coeff
		self.exp = exp
		self.next = next

	def insert(self, coeff, exp):
	# default; insert in last
		if LinkList2.start == None:
				print('list is empty')
				print('please wait while list is creating...')
				time.sleep(2)
				# create a new list
				link = LinkList2(coeff,exp)
				LinkList2.start = link
				# print(str(id(LinkList2.start)))
				print('list created successfully')
		else:
			#list is already created
			# iterate loop to last node
			q = LinkList2.start
			while q.next != None:
				q = q.next
			link = LinkList2(coeff,exp)	
			q.next = link
			print('data inserted successfully')	

	@classmethod		
	def displayList(cls):
		if cls.start == None:
			print('List is empty. please create list first')
			return
		q = cls.start
		print('list2---',id(q))
		while(q.next != None):
			print(str(q.coeff)+'x'+str(q.exp)+' ',end=' ')
			q = q.next
		# we have to print the last node also
		print(str(q.coeff)+'x'+str(q.exp)+' ') 
			

class LinkList3:
	start = None
	i = 1001 
	def __init__(self, coeff = None, exp = None, next = None):
		self.coeff = coeff
		self.exp = exp
		self.next = next

	def insert(self, coeff, exp):
	# default; insert in last
		if LinkList3.start == None:
				print('list is empty')
				print('please wait while list is creating...')
				time.sleep(2)
				# create a new list
				link = LinkList3(coeff,exp)
				LinkList3.start = link
				# print(str(id(LinkList2.start)))
				print('list created successfully')
		else:
			#list is already created
			# iterate loop to last node
			q = LinkList3.start
			while q.next != None:
				q = q.next
			link = LinkList3(coeff,exp)	
			q.next = link
			print('data inserted successfully')	

	@classmethod		
	def displayList(cls):
		if cls.start == None:
			print('List is empty. please create list first')
			return
		q = cls.start
		# print('list2---',id(q))
		while(q.next != None):
			print(str(q.coeff)+'x'+str(q.exp)+' ',end=' ')
			q = q.next
		# we have to print the last node also
		print(str(q.coeff)+'x'+str(q.exp)+' ') 
			



def add(list1, list2):
	if list1 == None and list2 == None:
		print("addition is can't possible bcz both list are empty.")
		return
	if list1 != None and list2 == None:
		# means list2 is empty
		link = LinkList1()
		link.displayList()
		return
	elif list1 == None and list2 != None:
		link = LinkList2()
		link.displayList()
		return
	else:
		q1 = list1
		q2 = list2
		while q1 != None and q2 != None:
			# if exponentials are equal
			if q1.exp == q2.exp:
				coeff = q1.coeff + q2.coeff
				exp = q1.exp
				link = LinkList3()
				link.insert(coeff,exp)
				q1 = q1.next
				q2 = q2.next
			elif q1.exp > q2.exp:
				# q1 > q2
				coeff = q1.coeff
				exp = q1.exp
				link = LinkList3()
				link.insert(coeff, exp)
				q1 = q1.next 
			else:
				# q2 > q1
				coeff = q2.coeff
				exp = q2.exp
				link = LinkList3()
				link.insert(coeff, exp)
				q2 = q2.next

		# inserting the remaining node of q1 in list 3
		while q1 != None:
			coeff = q1.coeff
			exp = q1.exp
			link = LinkList3()
			link.insert(coeff, exp)
			q1 = q1.next

		# inserting the remaining node of q1 in list 3
		while q2 != None:
			coeff = q1.coeff
			exp = q1.exp
			link = LinkList3()
			link.insert(coeff, exp)
			q1 = q1.next		
	# printing the resultant list
	LinkList3.displayList()		
				

# def length(LinkList):
# 	count = 0
# 	if LinkList == None:
# 		return count
# 	q = LinkList.start	
# 	while q.next != None:
# 		count += 1
# 		q = q.next
# 	count += 1
# 	return (count)			


while True:
	print('1. Insert in 1st list')
	print('2. Show')
	print('3. Count')
	print('4. Insert in 2nd list')
	print('5. Add both polynomial list')
	print('6. Exit')
	choice = int(input('Enter your choice'))
	if choice == 1:
		coeff = int(input('Enter coefficient'))
		exp = int(input('Enter exponential'))
		link = LinkList1()
		link.insert(coeff,exp)
	elif choice == 4:
		coeff = int(input('Enter coefficient'))
		exp = int(input('Enter exponential'))
		link = LinkList2()
		link.insert(coeff,exp)	
	elif choice == 2:
		x = int(input('Enter list no 1/2?'))
		if x==1:
			LinkList1.displayList()
		elif x==2:
			LinkList2.displayList()
	elif choice == 3:
		x = int(input('Enter list no 1/2?'))
		if x==1:
			print(length(LinkList1.start))
		elif x==2:
			print(length(LinkList2.start))
	elif choice == 5:
		# print(id(LinkList1.start),id(LinkList2.start))
		add(LinkList1.start, LinkList2.start)		
	elif choice == 6:
		print('Thanks...')
		exit()
	else:
		print('no choice matched')
		exit()				