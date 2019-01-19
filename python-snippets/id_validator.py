
factor_arr = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2] # consts for validating China's 18-digit ID

generateX(id):
    # assuming the input id is a string, first we need to convert it into an array 
    # we also assume the input has 17 digits -- all in numbers
    id_arr = [int(x) for x in id]
    sumvalue = sum([x * y for x, y in zip(id_arr, factor_arr)])
    modvalue = sumvalue % 11
    mod_str = str(modvalue) if modvalue < 10 else 'X'
    return mod_str
