# Using map() function and lambda and count() function create a list consisted of the number of occurence of both letters: A and a.   
# lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]   


def  get_occurrence_list(list_1):
    count_occurrence_A = lambda x: x.count('A')
    count_occurrence_a = lambda x: x.count('a')
    
    occurrence_A = sum(list(map(count_occurrence_A, list_1)))
    occurrence_a = sum(list(map(count_occurrence_a, list_1)))
    
    return {"A": occurrence_A, "a": occurrence_a}

if __name__ == "__main__":

    list_1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
    occurrence_list = get_occurrence_list(list_1)
    print(occurrence_list)
