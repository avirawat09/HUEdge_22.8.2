# Create a generator to return the fibonnaci sequence starting from the first element   
# up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,  89, . . .   


def fibonacci_gen(limit):
    a, b = 0, 1  
    while a < limit:
        yield a
        a, b = b, a + b
  
if __name__ == "__main__":
    for i in fibonacci_gen(5): 
        print(i)