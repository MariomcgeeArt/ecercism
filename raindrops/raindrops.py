def check_num(number):
    #checdk if int  or float
    if isinstance(number, int) or isinstance(number, float):
        #return if ture
        return True
        #creturn if false
    else:
        return False

def convert(number):
    #set results to empty string
    result = ""
    #if reviosu function return == TRUE
    #itterate thoguth the following code 

    if check_num(number)==True:
        if number%3==0:
            result += "Pling"
        if number%5==0:
            result += "Plang"
        if number%7==0:
            result += "Plong"
        if result == "":
            return str(number)
#return the resutl 
        return result
        #error message for some edge cases 
    else:
        raise Exception("Please enter a valid integer.")

# "Tests Cases:"

# good input
# print(check_num(50))
# print(convert(82))
# print(convert(20))
# print(convert(8300))
  print(convert(2))

# bad input
# print(check_num("s"))
# print(convert("a"));
# print(convert('345tg5'))


# edge-case input
# print(check_num(.7))
# print(convert(6.1))


