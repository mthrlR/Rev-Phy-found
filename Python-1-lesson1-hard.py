print("Medical Profile")
name = input("What's your name? ")
surname = input("What's your surname? ")
age = int(input("How old are u?"))
weigh = int(input("How much do you weigh?"))
if 50 <= weigh < 120 and age < 30:
     print("Good health")
elif weigh < 50 or weigh > 120 and 40 > age > 30:
     print("Watch ur health")
elif weigh < 50 or weigh > 120 and age > 40:
     print("Visit a doctor!")



