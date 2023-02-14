'''You are responsible for writing a program that will get a message and a specific letter from a
user and then count the number of occurrences of that letter in the given message. You
program should count “H” and “h” as an occurence of h. Your program will then display a
message to the user stating the occurrences of the given letter.'''


#Printing Welcome Statement
name=input("Enter Your Name: ").title().strip()
print("Hello {} , nice to meet you. I will count the number of times that a specific letter occurs in a message \n".format(name))
#Getting usr input
message=input("Enter a Message: ").strip().lower()
letter=input("Enter the letter to find and count: ").strip().lower()

letter_cnt=str(message.count(letter))
print("\n{} your message contains {}'s {}".format(name,letter_cnt,letter))
