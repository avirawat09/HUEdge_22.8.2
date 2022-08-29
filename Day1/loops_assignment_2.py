# Write a program to print the following pattern    
#       *   
#      ***     
#     *****   
#    *******   
#   *********   
#    *******   
#     *****   
#      ***   
#       *   


def print_diamond(num):
    for row in range(num):
        print(" "*(num-row), "*"*(row*2+1))
    for row in range(num-2, -1, -1):
        print(" "*(num-row), "*"*(row*2+1))

if __name__ == "__main__":
    num = 5
    print_diamond(num)