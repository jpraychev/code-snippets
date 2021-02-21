def decorator_function(func):
    print('A decorator function was called')
    
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

# # Simple function
@decorator_function
def simple_function(name):
    return f'Hi, {name}'

if __name__ == '__main__':

    # simple_function = decorator_function(simple_function('Jordan'))
    # simple_function()
    print(simple_function('Jordan'))