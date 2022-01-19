# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = name1.lower() + name2.lower()

true_count = int(combined_name.count('r') + combined_name.count('t') + combined_name.count('u') + combined_name.count('e')) 

love_count = int(combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e'))

total_char = int(str(true_count) + str(love_count))

if total_char < 10 or total_char > 90:
    print(f"Your score is {total_char}, you go together like coke and mentos.")
elif total_char >= 40 and total_char <=50:
    print(f"Your score is {total_char}, you are alright together.") 
else:
    print(f"Your score is {total_char}.") 
