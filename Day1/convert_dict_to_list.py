# The original dictionary is : {‘HuEx: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}   
# The converted list is : [[‘HuEx, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]   

def convert_to_list(orignal_dict):
    converted_list = []
    for key, value in orignal_dict.items():
        value.insert(0, key)
        converted_list.append(value)
    return converted_list    

if __name__== "__main__":
    orignal_dict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
    converted_list = convert_to_list(orignal_dict) 
    print(converted_list)

