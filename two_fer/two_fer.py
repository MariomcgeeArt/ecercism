def two_fer(name=None):
    if name:
        return f'One for {name}, one for me.'
    else:
        return 'One for you, one for me.'

print(two_fer("Bean"))
print(two_fer())



#good inputs
print(two_fer("Bean"))
print(two_fer('ann'))
print(two_fer('mark'))




#bad inputs
print(two_fer("hello, mark"))
print(two_fer([1,2,3]))
print(two_fer(3))


#edgecases inputs
print(two_fer('3'))
var = 'matt'
print(two_fer(var))













