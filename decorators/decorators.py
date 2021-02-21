# Simple function with arguments
def simple_func_args(name):
    print(f'Hello {name}')

    def inner_func():
        print('A call from inner function')

    inner_func()


def wrong_sentance():
    return "A senTancE That HavE to be ReworKeD"

def fix_sentance(func):

    print("Calling a function to fix our sentance")

    sentance = func()
    return sentance.capitalize()





def decorator_function(func):
    print('A decorator function was called')
    
    def wrapper():
        print(func)

    return wrapper

# # Simple function
# @decorator_function
def simple_function(name):
    return f'Hi, {name}'

if __name__ == '__main__':

    simple_function = decorator_function(simple_function('Jordan'))
    simple_function()

    
    

    

