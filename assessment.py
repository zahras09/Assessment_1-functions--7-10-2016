# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).


#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 
def item_cost(tax, state, cost):
	tax = .07
	state = "" 
	cost = float()
	total = cost + (cost * tax)
print item_cost(tax, state, cost)
# need extra help on calling function when the argument is passed as variables.
	
#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".
def is_berry(fruit_name):
	# I'm not sure why this line did not work??
	# if fruit_name == "strawberry" or "cherry" or "blackberry":
	if fruit_name == "strawberry":
		return True
	if fruit_name ==   "cherry":
		return True
	if fruit_name == "blackberry":
		return
	else:
		return False
print is_berry(fruit_name)


#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def is_berry(fruit_name):
	# fruit_name == "strawberry"
	if fruit_name == "strawberry":
		return True
	if fruit_name ==   "cherry":
		return True
	if fruit_name == "blackberry":
		return
	else:
		return False
	return is_berry("apple")

	def shipping_cost():
		if is_berry == True:
			return 0
		if is_berry == False:
			return 5
	print shipping_cost()

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
def is_hometown():
	# while True:
	user_answer = raw_input("what is your hometown?")
	hometown = "berkeley"
	if user_answer == "berkeley":
		return True
	else:
		return False
print is_hometown()
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
def full_name(first, last):
	# when you take an argument and pass it as a variable whey do you
	# need to call it again when you call your function?
	first = raw_input("what is your first name?")
	last = raw_input("what is your last name?")
	entire_name = str(first + " " + last
	return entire_name
print full_name("zahra", "sadat")

#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.
def hometown_greeting(first_name, last_name, home_town,):
		first_name = first
		last_name = last
		home_town = hometown
		print "Hi" + entire_name + "where are you from?"

		def full_name(first, last):
				first = raw_input("what is your first name?")
				last = raw_input("what is your last name?")
				entire_name = first + " " + last
				return entire_name

		def is_hometown():
			user_answer = raw_input("what is your hometown?")
			hometown = "berkeley"
			if user_answer == "berkeley":
				print "we're from the same place!"
			else:
				print "I dont' know where that is."
hometown_greeting("zahra", "sadat", "berkeley")
# really stuck and confused on this one.


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.
def increment(x):
	x = int(1)

	def add(y):
		y = x + y
		return y
print (increment(1)) + (add(1))

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20. 
def increment(variable):
	for i in variable:
		x = 5
		addfive = x
	# ???

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.
def list_function(number,list_of_numbers):
	number = int()
	list_of_numbers = []
	for new_numbers in number:
		list_of_numbers.append(number)
	return list_of_numbers
value = list_function(number, list_of_numbers)
print value

#####################################################################