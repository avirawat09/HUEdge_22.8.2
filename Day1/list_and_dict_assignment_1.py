# Return all the duplicate values from list of arraylist   
# Input:    
# [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]   
# Output:    
# 1 -> 2 	  
# 8 -> 2   
# 0 -> 3, 4 -> 2   


def check_duplicates_in_list(ele_list):
    """This function print duplicate entries present in a list

    Args:
        ele_list (list): input list
    """    
    duplicate_dict = {}
    for ele in ele_list:
        if ele in duplicate_dict:
            duplicate_dict[ele] +=1
        else:
            duplicate_dict[ele] = 1

    for ele, freq in duplicate_dict.items():
        if freq>1:
            print(f"{ele} -> {freq}", end = ' , ')
    print()


def process_duplicates(array_list):
    for ele_list in array_list:
        check_duplicates_in_list(ele_list)


if __name__ == "__main__":
    array_list = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
    process_duplicates(array_list)