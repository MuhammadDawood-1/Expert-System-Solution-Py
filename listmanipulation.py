print("------------LIST WORKING------------")
ESS=['HR','Finance','IT','Engineering','Marketing']
ESS.insert(0,'Taxation')
ESS.append('Management')
print("List of Departments",ESS)

print("The Length of the List is Before",len(ESS))
ESS.pop(6)

print("The Length of the List is After",len(ESS))
print(ESS)