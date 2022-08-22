#Python-Primer-100
print(5 + 5)

sum = 5 + (10 /10)
print(sum)

# Python-Primer-101
abu_bakr = "First Caliph"
print(abu_bakr)

# To write multiple line of strings use single quotes three times
umer = '''Second Caliph 
A companion of Holy Prophet peace and blessings be upon him
righteous 


strong
brave'''
print(umer)

# STRING PROBLEM HANDLING

# silly_string = "He said,"Aren't can't shoudn't woudn't"

# If you are multiple quotes of single and double strings than this causes an error. There are two ways to solve this error 

# 1). You can use triple quotes and use multiple single double quotes inside the string
silly_string = '''He said, "Aren't can't shoudn't wouldn't" '''
print(silly_string)

# 2). "\" or excaping asks python to ignore the quotes inside the string, this would not pop the error.
another_silly_string = 'He said, "Aren\'t can\'t shoudn\'t woudn\'t"'
print(another_silly_string)

# EMBEDDING VALUES IN THE STRING

myscore = 1000
message = "I scored %s points"
print(message % myscore)