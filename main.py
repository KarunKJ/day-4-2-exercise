# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)
print(len(names))
Payee = random.randint(0,len(names) - 1)
payee_name = names[Payee]
print(f"Today's bill is to be paid by {payee_name}")

