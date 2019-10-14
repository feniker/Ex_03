import math
lst = [1,5,7,1,4,5,7,8,9,5,4]
lst2 = [2,4,1]
print(sum(range(1,2**25)))
print(math.factorial(1000))
print([i+1 if i%2 else i for i in lst])
print([i for i in lst if lst2.count(i) == 0])
print([j + str(i) for i in range(1,11) for j in ['a','b','c','d','e','f','g','h']])
print(len([i for i in range(1,10**6+1) if (i % 2 == 0) and (i % 7 != 0) and (str(i)[:3] == "793")]))
print("".join(reversed(input("Enter string: "))))
with open('untitled.txt', encoding='UTF8') as a: print(a.read().count("z"))