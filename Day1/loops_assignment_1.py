# Write a program to input an integer N from user and print pascal triangle up to N rows.   
# input - 3   
# Output 1:   
# 1 0 0    
# 1 1 0    
# 1 2 1   

def pascal_triangle(num):
    """This function is used to print pascal triangle

    Args:
        num (int): number of rows of pascal triangle
    """    
    for row in range(1, num+1):
        ele = 1
        for col in range(1, row + 1):
            print(ele, end = ' ')
            ele = int(ele * (row-col) /col) 
        print()    

if __name__== "__main__":
    num = 7
    pascal_triangle(num)





