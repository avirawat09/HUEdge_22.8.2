# Problem 1 – Problem on Object Oriented Programming   

# create a class with name which should take string as an input from constructor. It should have method which should return the length of the string and a method to convert string to list  of characters. This method will take an argument as string to convert.    
# Create class PairsPossible which should inherit from StringClass and should have a method for storing list of all possible pairs formed. It should also have a method to print list of every possible pair in same line but with space between them. Pairs should be in list.   
# Create a class SearchCommonElements which should take up a string. Your task is to create a method to find common elements from string taken in StringClass and string taken in PairsPossible class and return the answer in list. Note- Please use dictionary logic to find common elements.   
# Create a class EqualSumPairs to get the count of total number of pairs formed in class PairsPossible which has sum which is not equal to sum of other pairs. Print the output for SearchCommonElements and EqualSumPairs classes.   
# NOTE: string taken should be in numbers representation. like string = '12314532'   



class StringClass:
    def __init__(self, input_string) -> None:
        self.input_string = input_string

    def get_length(self):
        return len(self.input_string)

    def get_character_list(self, name=None):
        if name is None:
            name = self.input_string
        return list(name)


class PairsPossible(StringClass):
    def __init__(self, input_string) -> None:
        super().__init__(input_string)

    def store_possible_pairs(self):
        string  = self.get_character_list()
        pair_list = []
        for i in range(len(string)):
            for j in range(i+1, len(string)):
                pair_list.append([string[i], string[j]])
        self.pair_list = pair_list
        
    def print_possible_pairs(self):
        return ', '.join([ ''.join(ele) for ele in self.pair_list])        



class SearchCommonElements:
    def __init__(self, string1, string2) -> None:
        self.string1 = string1
        self.string2 = string2

    def get_common_elements(self):
        temp = {}
        result = []
        for ele in self.string1:
            if ele in temp:
                temp[ele] += 1
            else:
                temp[ele] = 1
        
        for ele in self.string2:            
            if ele in temp:
                result.append(ele)
                temp[ele] -= 1
                if temp[ele]==0:
                    del temp[ele]
        
        return result

class EqualSumPairs(PairsPossible):
    def __init__(self, string) -> None:
        super().__init__( string)

    def count_number_of_pairs(self):
        self.store_possible_pairs()
        pair_list = self.pair_list
        count_dict = {}
        for pair in pair_list:
            pair = list(map(int,pair))
            pair_sum = sum(pair)
            if pair_sum in count_dict:
                count_dict[pair_sum] = False                
            else:
                count_dict[pair_sum] = True
        counter = 0
        for k,v in count_dict.items():
            if v is True:
                counter +=1

        return counter        

if __name__ == "__main__":
    s = SearchCommonElements('1221', '2312')
    r = s.get_common_elements()
    print(r)


    e = EqualSumPairs('1234')
    c = e.count_number_of_pairs()
    print(c)
