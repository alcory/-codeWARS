def move_zeros(lst):
    new_lst = []
    for number in lst:
        if number != 0:
            new_lst.append(number)
    for number in lst:
        if number == 0:
            new_lst.append(number)
    return(new_lst)



lst = [1, 0, 1, 2, 0, 1, 3]

move_zeros(lst)
