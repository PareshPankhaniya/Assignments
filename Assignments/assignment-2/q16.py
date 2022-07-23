max = 0

def max_len_from_list_element(list):
    global max
    for x in list:
        if max < len(x):
            max = x
            return max

print(f"Maximun length of an element from passed list : {max_len_from_list_element(['asfdsdf','sdfsdf','sdfsdf','aswetr','fgbafe','trawe'])}")