# Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c  

if __name__ == "__main__":
    equation = lambda a,b,c,x: a*(x**2) + b*x + c 
    result = equation(3,5,6,4)
    print(result)

