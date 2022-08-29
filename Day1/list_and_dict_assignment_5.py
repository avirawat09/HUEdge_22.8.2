# Merge following two Python dictionaries into one   
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}   
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


def merge_dict(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict 



if __name__== "__main__":
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30 }
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50 }
    merged_dict = merge_dict(dict1, dict2)
    print(merged_dict)
