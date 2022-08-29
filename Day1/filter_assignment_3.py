# Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.   
# lst1=["Netflix", "Hulu", "Sling", "Hbo"]
# lst2=[198, 166, 237, 125]


if __name__ == "__main__":
    lst1 = ["Netflix", "Hulu", "Sling", "Hbo"]
    lst2 = [198, 166, 237, 125]


    print(dict(zip(lst1, lst2)))

