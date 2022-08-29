# write a decorator which will take a function and execute it twice.   
# Function is -   
# def multiply(num1, num2):   
#     print(num1 * num2)   


def my_decor(func):
    def my_wrap(*args, **kwargs):
        print("Decorator Function")
        func(*args, **kwargs)
        func(*args, **kwargs)
        
    return my_wrap


@my_decor
def multiply(num1, num2):
    print(num1 * num2)


if __name__ == "__main__":
    multiply(3,5)