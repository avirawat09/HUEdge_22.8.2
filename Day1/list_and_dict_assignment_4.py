# Map the dictionary in the following manner   
# Keys = [‘Ten’, ‘Twenty’, ‘Thirty’]   
# Value = [10,20,30]   
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}   


def dict_mapper(Keys, Value):
    return dict(zip(Keys, Value))

if __name__ == "__main__":
    Keys = ['Ten', 'Twenty', 'Thirty'] 
    Value = [10,20,30]
    mapped_dict = dict_mapper(Keys, Value)
    print(mapped_dict)