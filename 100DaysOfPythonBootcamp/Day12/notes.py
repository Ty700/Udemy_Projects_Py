#Scope - usual. Py just doesn't have a block scope like C/C++
#Modifying global vars in python is a tad bit different

#Modifying Global Var example:

global_var = 5

def example_func():
	global global_var #Without this, we can't modify the global scope variable
	#Since we usually don't want to modify global vars, it is an extra step to change it.
	global_var += 1
	print(global_var) #6

	#If we want to increase any global_var without modifying it. Just return it as an output
	#Example: return (global_var + 1)

example_func()

print(global_var) #6


#Python Constants

#All caps as usual. No "const" pre text before.
#We can still change all cap variables, no true const var in Python which is weird
PI = 3.14159