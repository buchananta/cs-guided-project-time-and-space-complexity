def do_a_bunch_of_stuff(items):
    last_idx = len(items) -1 # gettinng the length is O(1)

    print(items[last_idx]) # accessing an array element via index is O(1)
                           # printing is also considered O(1)

    middle_idx = len(items) / 2 # arithmetic operations are O(1)
    idx = 0                     # initializing a variable O(1)

    while idx < middle_idx: # Only iterating over half? Doesn't matter! 0(n)
        print(items[idx])   # O(1)
        idx = idx + 1       # O(1)

    for num in range(2000): # O(1)
        print(num)

def removeDuplicateMine(arr):
    return list(set(arr))

def removeDuplciate(arr):
    # I guess this runs in O(n)
    # because the two O(n) times add together
    # They don't multiply becuase they aren't nested!
    differents = {} # initializing a variable - O(n)
    for i in arr: # O(n)
        if i not in differents: # O(1)
            differents[i] = []  # O(1)

        differents[i] += [i]    # 1. appending onto the end of the list - O(1)
                                # 2. accessing the key in the dictionary - O(1)
    return differents.keys()    # the `keys` method takes all the keys in the
                                # dictionary and returns them as a list O(n)
