print("Hello, Python!")

'''
1. Python apart from other programming languages run on Identation.
for eg Below is a simple for loop:

something = [1,1,1,1,1]
for i in something:
    print i 

Now lets start with Basics i.e. Variables
'''
counter = 100  # An integer assignment
miles = 1000.0  # A floating point
name = "John"  # A string
print("Here, 100, 1000.0 and John are the values assigned to counter, miles, and name variables, respectively. This "
      "produces the following result −")
print(counter)
print(miles)
print(name)

'''We can also do multuple Assingment in a single go i.e.'''
a = b = c = 1
print(a, b, c)

'''Standard Data Types
    Python has five standard data types −
           1. Numbers
           2. String
           3. List
           4. Tuple
           5. Dictionary'''

'''Python Numbers
Number data types store numeric values. Number objects are created when you assign a value to them. For example −'''
var1 = 1
var2 = 10

'''Python Strings Strings in Python are identified as a contiguous set of characters represented in the quotation 
marks. Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the slice 
operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at 
the end. 

The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator. For example −'''

hello_str = 'Hello World!'

print(hello_str)  # Prints complete string
print(hello_str[0])  # Prints first character of the string i.e. H
print(hello_str[2:5])  # Prints characters starting from 3rd to 5th i.e. llo
print(hello_str[2:])  # Prints string starting from 3rd character i.e. llo World!
print(hello_str * 2)  # Prints string two times i.e. Hello World!Hello World!
print(hello_str + "TEST")  # Prints concatenated string i.e. Hello World!TEST

print('''Python Lists Lists are the most versatile of Python's compound data types. A list contains items separated by 
commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference 
between them is that all the items belonging to a list can be of different data type. 

The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the 
beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, 
and the asterisk (*) is the repetition operator. For example − ''')

test_list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(test_list)  # Prints complete list
print(test_list[0])  # Prints first element of the list
print(test_list[1:3])  # Prints elements starting from 2nd till 3rd
print(test_list[2:])  # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(test_list + tinylist)  # Prints concatenated lists
