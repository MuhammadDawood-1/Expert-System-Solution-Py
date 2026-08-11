import os
import time
 
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def pause_f():
    time.sleep(2)
    
    
    
def add_product(d):
    name=input("Enter the name of product:")
    quantity=int (input("Enter the quantity"))
    d[name]=quantity
    
    
    
def update_q(d):
    name=input("Enter the name of product:")
    quantity=int (input("Enter the quantity"))
    d[name]=quantity
    
def remove_p(d):
    name=input("Enter the name of product:")
    if name in d:
        d.remove(name)
    else:
        print("ja kam kr")

def search_p(d):
    name=input("Enter the name of product:") 
    if name in d:
        print(f"Name: {name} , Quantity: {d[name]}")
        
    else:
        print("BYEE")    

def display_i(d):
    if not d:
        print("Inventory is empty.")
    for name, quantity in d.items():
        print("Name: ",name," Quantity:")   
                
        
def print_menu():
    print("1:ADD PRODUCT")
    print("2:UPDATE QUANTITY")
    print("3:REMOVE PRODUCT")
    print("4:SEARCH PRODUCT")    
    print("5:DISPLAY INVENTORY")
    print("6:EXIT")
    
    
def main():
    david = True
    dd={} 
    while david:
        print_menu()
        user= int (input("Enter the number: "))
        match user:
            case 1:
                clear_screen()
                add_product(dd)
            case 2:
                clear_screen()
                update_q(dd)
            case 3:
                clear_screen()
                remove_p(dd)
            case 4:
                clear_screen()
                search_p(dd)
            case 5:
                 clear_screen()   
                 display_i(dd)
            case 6:
                clear_screen()
        pause_f()
main()
                    
                
                  
                            
                
            