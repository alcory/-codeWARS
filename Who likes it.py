def likes(names):
    if (len(names)) == 0:
        return 'no one likes this'
    elif (len(names)) == 1:
        return names[0] + ' likes this'
    elif (len(names)) == 2:
        return ' and '.join(names[0:2]) + ' like this'
    elif (len(names)) == 3:
        return ', '.join(names[0:2])+ ' and ' + names[2] + ' like this'
    elif (len(names)) > 3:
        return ', '.join(names[0:2])+ ' and '+ str(len(names[1:-1]))+ ' others like this'

zero_names = []
one_names = ["Peter"]
two_names =["Jacob", "Alex"]
three_names =["Max", "John", "Mark"]
four_names =["Alex", "Jacob", "Mark", "Max"]


print(likes(three_names))
