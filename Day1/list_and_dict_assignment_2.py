# Merge two lists as shown below   
# Given I/P   
# list1 = ["Hello ", "take "]   
# list2 = ["Dear", "Sir"]   
# E/O   
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']  


def merge_lists(list1, list2) -> list:
    """This function is used to merge two lists

    Args:
        list1 (list): first list
        list2 (list): second list

    Returns:
        merge_list (list): merged list 
    """    
    merge_list = [first+' '+second for first in list1 for second in list2]
    return merge_list



if __name__ == "__main__":
    list1 = ["Hello", "take"]
    list2 = ["Dear","Sir"]
    merged_list = merge_lists(list1,list2)
    print(merged_list)