name = input("enter your name : ")
age = input("enter your age: ")
print("your age is "+age)

boy_name =input("enter the boye name: ")
boy_age  = int(input("enter the boy age: "))
girl_name = input("enter the girl name: ")
girl_age = int(input("enter the girl age: "))
age_diff = abs(boy_age - girl_age)

print(boy_name + " loves " + girl_name + " .and there age diffrence is "+ str(age_diff))
print(f"{boy_name} loves {girl_name}. and there age diffrence is {age_diff}") # formated string