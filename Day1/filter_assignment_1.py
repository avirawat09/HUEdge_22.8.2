# Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.   
# Note: map() function is inside filter() function.   
# lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]   


if __name__ == "__main__":
    list_1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
    filtered_list  = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, list_1)))
    print(filtered_list)


