"function is a block of code of reusuable code that is used to perform a specific task "

"it helps you avoid repetition , makes code modular and improve test automation frameworks"

"Types of functions in python"
"1. Built-in functions"
"2. User-defined functions"

"Built in functions"
"created by python and are readily available for use"
"examples : print(), input(), len(), type(), int(), str(), float(), list(), dict(), set(), tuple(), strip(), range() etc"
"refer : https://docs.python.org/3/library/functions.html"

"how the function are created ?"
"syntax :"
"~ define/ declare"
"~ call "

#steps to create a function
"define / declare a function"
"syntax : def name_of_function(parameters):"
 # block of code to be executed
  # return if something needs to be returned"

#step 2
"call the function"
"syntax : name_of_function(parameters)"

#example 1 : lets create a function which will greet you or say hello to user
def greet_user():
    print("Hello User! Welcome to Python Functions")

# step 2 : call the function
greet_user()
greet_user()


# types of functions based on parameters
"1. functions without parameters and without return type"
"2. functions with parameters and without return type"
"3. functions with parameters and with return type"
"4. functions without parameters and with return type"

# why we use return type in function ?
" after performing some operations inside the function if we want to get some result back we use return type"
" return statement is used to exit a function and go back to the place from where it was called"
" it can also return a value to the caller function"
" if no return statement is used the function will return None by default"

# why function are important for QA/ SDET automation engineers ?
" reusable code"
" easier maintenance"
" less code"
" easy to read and understand"
" modular code"
" better collaboration"
" improved test automation frameworks"
" better debugging and testing"
