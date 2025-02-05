# decorator - @ followed by the function name is used to define a decorator
# decorator must be placed one step above the function that is to be sent in decorator
# using decorator is alternative for called a function like [function(arko_function)]
# def Program(functions):
#    print("Inside Program function")
#    functions()
#    print("Execution completed.")

# # @function_name
# @Program
# def Hello():
#    print("Hello World")
#    print("Hello World")
#    print("Hello World")
#    print("Hello World")

# Program(Hello)
# Hello()


# use decorator to solve this problem,even if numearator is smaller than denomenator, print out positive interger should not be decimal 
def divide(a,b):
   print(a/b)

divide(2,10)