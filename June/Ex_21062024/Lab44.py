#Dictionary

#there are 2 way to print and use dictionary
#1st way
Dictionary_1 ={ "name" : "sid", "age": 22, "address": "jalgaon"}

print(Dictionary_1)
#if I want to print one by one then
print(Dictionary_1 ["name"])
print(Dictionary_1["age"])
print(Dictionary_1["address"])

#2nd Way
Dictionary_2 = dict(name ="sid", age= 22, address="nashik")
print(Dictionary_2)
#if want to call single then
print(Dictionary_2["name"])

#another way to get or call value of dictionary
print(Dictionary_2.get("name"))

#I can change name also
Dictionary_2["name"] = "siddhesh"
print(Dictionary_2["name"])

