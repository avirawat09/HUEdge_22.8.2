# Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list   
# Given List:   
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]   
# Sub List to be added = ["h", "i", "j"]   
# Expected output:  
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']    

def extend_list(list1,extend_flag = False):
    for ele in list1:
        if isinstance(ele,list):
            extend_list(ele)
            extend_flag = True
            break
    if not extend_flag:    
        list1.extend(["h", "i", "j"])




if __name__== "__main__":
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
    extend_list(list1)
    print(list1) 