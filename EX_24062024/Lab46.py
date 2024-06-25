#How to find value in dictonary and print it

my_dict = {
    "name": "Sid",
    "add": "Jalgaon",
    "State" : "Maharashtra"
}
for k, v in my_dict.items():
    print(k,v)

    if k == "add":
      print("Add is founnd")

    #Or we can use and it will give ans in boolen 
abc = 'add' in my_dict
print(abc)
