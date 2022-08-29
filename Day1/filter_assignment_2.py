# Take the first two values, run the function on them. Then take the result and the next value and have a multiplication between them. etc. When no more values are left, return the last result.   
#  Note: use reduce function for this

from functools import reduce

if __name__ == "__main__":
    list_1 = [3,5,6,4]
    print(reduce(lambda a, b: a*b, list_1))