#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])


array = [5, 2, 3, 4, 1, 6, 7]

# Take sum as input from user
summ = 7

# print array
print("Array= ", array)

# call function find
find(array, len(array), summ)


# In[2]:


def reverseList(A, start, end):
  while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1
# Driver function to test above function
A = [10, 20, 30, 40, 50]
reverseList(A, 0, 4)
print(A)


# In[3]:


# Python3 program for the above approach


def checkString(s1, s2, indexFound, Size):
	for i in range(Size):

		# check whether the character is equal or not
		if(s1[i] != s2[(indexFound + i) % Size]):
			return False

		# %Size keeps (indexFound+i) in bounds,
		# since it ensures it's value is always less than Size
	return True


# driver code
s1 = "abcd"
s2 = "cdab"

if(len(s1) != len(s2)):
	print("s2 is not a rotation on s1")

else:

	indexes = [] # store occurrences of the first character of s1
	Size = len(s1)
	firstChar = s1[0]
	for i in range(Size):
		if(s2[i] == firstChar):
			indexes.append(i)

	isRotation = False

	# check if the strings are rotation of each other
	# for every occurrence of firstChar in s2
	for idx in indexes:

		isRotation = checkString(s1, s2, idx, Size)

		if(isRotation):
			break

	if(isRotation):
		print("Strings are rotations of each other")
	else:
		print("Strings are not rotations of each other")

# This code is contributed by shinjanpatra


# In[4]:


# Python program to print the first non-repeating character

string = "geeksforgeeks"
index = -1
fnc = ""
for i in string:
	if string.count(i) == 1:
		fnc += i
		break
	else:
		index += 1
if index == 1:
	print("Either all characters are repeating or string is empty")
else:
	print("First non-repeating character is", fnc)


# In[5]:


# Recursive Python function to solve tower of hanoi


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# Driver code
N = 3

# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

# Contributed By Harshit Agrawal


# In[6]:


# Python3 Program to convert postfix to prefix

# function to check if
# character is operator or not


def isOperator(x):

	if x == "+":
		return True

	if x == "-":
		return True

	if x == "/":
		return True

	if x == "*":
		return True

	return False

# Convert postfix to Prefix expression


def postToPre(post_exp):

	s = []

	# length of expression
	length = len(post_exp)

	# reading from right to left
	for i in range(length):

		# check if symbol is operator
		if (isOperator(post_exp[i])):

			# pop two operands from stack
			op1 = s[-1]
			s.pop()
			op2 = s[-1]
			s.pop()

			# concat the operands and operator
			temp = post_exp[i] + op2 + op1

			# Push string temp back to stack
			s.append(temp)

		# if symbol is an operand
		else:

			# push the operand to the stack
			s.append(post_exp[i])

	
	ans = ""
	for i in s:
		ans += i
	return ans


# Driver Code
if __name__ == "__main__":

	post_exp = "AB+CD-"
	
	# Function call
	print("Prefix : ", postToPre(post_exp))

# This code is contributed by AnkitRai01


# In[7]:


# Python Program to convert prefix to Infix
def prefixToInfix(prefix):
	stack = []
	
	# read prefix in reverse order
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			
			# symbol is operand
			stack.append(prefix[i])
			i -= 1
		else:
		
			# symbol is operator
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False

# Driver code
if __name__=="__main__":
	str = "*-A/BC-/AKL"
	print(prefixToInfix(str))
	
# This code is contributed by avishekarora


# In[8]:


# Python3 program to check for
# balanced brackets.

# function to check if
# brackets are balanced


def areBracketsBalanced(expr):
	stack = []

	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
			stack.append(char)
		else:

			# IF current character is not opening
			# bracket, then it must be closing.
			# So stack cannot be empty at this point.
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	# Check Empty Stack
	if stack:
		return False
	return True


# Driver Code
if __name__ == "__main__":
	expr = "{()}[]"

	# Function call
	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")

# This code is contributed by AnkitRai01 and improved
# by Raju Pitta


# In[9]:


# create class for stack
class Stack:

	# create empty list
	def __init__(self):
		self.Elements = []
		
	# push() for insert an element
	def push(self, value):
		self.Elements.append(value)
	
	# pop() for remove an element
	def pop(self):
		return self.Elements.pop()
	
	# empty() check the stack is empty of not
	def empty(self):
		return self.Elements == []
	
	# show() display stack
	def show(self):
		for value in reversed(self.Elements):
			print(value)

# Insert_Bottom() insert value at bottom
def BottomInsert(s, value):

	# check the stack is empty or not
	if s.empty():
		
		# if stack is empty then call
		# push() method.
		s.push(value)
		
	# if stack is not empty then execute
	# else block
	else:
		popped = s.pop()
		BottomInsert(s, value)
		s.push(popped)

# Reverse() reverse the stack
def Reverse(s):
	if s.empty():
		pass
	else:
		popped = s.pop()
		Reverse(s)
		BottomInsert(s, popped)


# create object of stack class
stk = Stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

print("Original Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()


# In[11]:


# Class to make a Node
class Node:
	# Constructor which assign argument to nade's value
	def __init__(self, value):
		self.value = value
		self.next = None

	# This method returns the string representation of the object.
	def __str__(self):
		return "Node({})".format(self.value)

	# __repr__ is same as __str__
	__repr__ = __str__


class Stack:
	# Stack Constructor initialise top of stack and counter.
	def __init__(self):
		self.top = None
		self.count = 0
		self.minimum = None

	# This method returns the string representation of the object (stack).
	def __str__(self):
		temp = self.top
		out = []
		while temp:
			out.append(str(temp.value))
			temp = temp.next
		out = '\n'.join(out)
		return ('Top {} \n\nStack :\n{}'.format(self.top, out))

	# __repr__ is same as __str__
	__repr__ = __str__

	# This method is used to get minimum element of stack
	def getMin(self):
		if self.top is None:
			return "Stack is empty"
		else:
			print("Minimum Element in the stack is: {}" .format(self.minimum))

	# Method to check if Stack is Empty or not

	def isEmpty(self):
		# If top equals to None then stack is empty
		if self.top == None:
			return True
		else:
			# If top not equal to None then stack is empty
			return False

	# This method returns length of stack
	def __len__(self):
		self.count = 0
		tempNode = self.top
		while tempNode:
			tempNode = tempNode.next
			self.count += 1
		return self.count

	# This method returns top of stack
	def peek(self):
		if self.top is None:
			print("Stack is empty")
		else:
			if self.top.value < self.minimum:
				print("Top Most Element is: {}" .format(self.minimum))
			else:
				print("Top Most Element is: {}" .format(self.top.value))

	# This method is used to add node to stack
	def push(self, value):
		if self.top is None:
			self.top = Node(value)
			self.minimum = value

		elif value < self.minimum:
			temp = (2 * value) - self.minimum
			new_node = Node(temp)
			new_node.next = self.top
			self.top = new_node
			self.minimum = value
		else:
			new_node = Node(value)
			new_node.next = self.top
			self.top = new_node
		print("Number Inserted: {}" .format(value))

	# This method is used to pop top of stack
	def pop(self):
		if self.top is None:
			print("Stack is empty")
		else:
			removedNode = self.top.value
			self.top = self.top.next
			if removedNode < self.minimum:
				print("Top Most Element Removed :{} " .format(self.minimum))
				self.minimum = ((2 * self.minimum) - removedNode)
			else:
				print("Top Most Element Removed : {}" .format(removedNode))


# Driver program to test above class
if __name__ == '__main__':
	
    stack = Stack()
	
# Function calls
stack.push(3)
stack.push(5)
stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()
stack.pop()
stack.getMin()
stack.pop()
stack.peek()

# This code is contributed by Blinkii


# In[ ]:




