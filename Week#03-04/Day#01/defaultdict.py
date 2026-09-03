from collections import defaultdict 
#list d me 
d = defaultdict(list) 
  
for i in range(5): 
    d[i].append(i) 
      
print("Dictionary with values as list:") 
print(d)

students = defaultdict(list)

students["CS"].append("Ali")
students["CS"].append("Ahmed")

students["SE"].append("Dawood")
students["SE"].append("Usman")

print(students)