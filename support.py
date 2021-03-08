def print_func(name):
    return print ("Hello,  ", name)    

def add_func(a,b):
    return a + b

def sub_func(a,b):
    return a - b

# print('call it from support.py')
# print_func("Nick")

if __name__ == '__main__':
    print('call it from support.py')
    print_func("Nick")