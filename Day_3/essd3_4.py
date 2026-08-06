print("Now Dictionaries")

info = {
    "Name": "David",
    "Roll no": "F2024SE037",
    "University": "Nastp Niit",
    "Department": "Software Engineering"
}

print(info)

print(info["Name"])
print(info["University"])

info["CGPA"] = 2.42

print(info)

print(info["CGPA"])

# get() function
print(info.get("Department"))
print(info.get("University"))

# keys()
print(info.keys())
#values
print(info.values())
#items
print(info.items())
#update()
info.update({
    "Nationality":"Pakistani",
    "Cast":"Homo Sapiens"

})
print(info)
#copy 
info2=info.copy()
print(info2)
#length
print(len(info))
print(len(info2))


