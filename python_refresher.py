# l1=[2,4,6]
# l2=[3,5,7]
# square=list(map(lambda i:i*2, l2))
# print(square)

# celsius = [20, 30, 40, 50]
# farh=list(map(lambda i:((9/5)*i)+32, celsius))
# print(farh)

# operations = {
#     'add': lambda x, y: x + y,
#     'subtract': lambda x, y: x - y,
#     'multiply': lambda x, y: x * y,
#     'divide': lambda x, y: x / y
# }

# print(operations['add'](5, 3))       
# print(operations['subtract'](10, 4))  
# print(operations['multiply'](2, 6))    
# print(operations['divide'](10, 2))

# operations = {
#     'double': lambda x: x*2,
#     'half': lambda x: x/2,
# }

# print(list(map(operations['double'], [2,4,6])))      
# print(list(map(operations['half'], [2,4,6])))

week = {"M":30, "T":32, "W":31}
dict1 = dict((map(lambda i:(i[0],((9/5)*i[1])+32), week.items())))
print(dict1)