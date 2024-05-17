#Q1) Python string methods
str="My name is Avinash"
str2="I am from Bihar"
str3=("Hi", "This", "Is", "King")


print(len(str))
print(str.count("i"))
print(str + str2)
print(str.upper())
print(str2.lower())
print(str.startswith("My"))
print(str2.endswith("from"))
print(str2.find("a"))
print(str.split())
print(str.strip())

x=str2.lstrip()
print(x,"Nawada")

x=str2.rstrip()
print("Nawada",x)

x = str.index("Avinash")
print(x)

x=" ".join(str3)
print(x)
