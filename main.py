import random

#A function to Shuffle all the characters of a string
def shuffle(string):
 tempList = list(string)
 random.shuffle(tempList)
 return ''.join(tempList)

#Brain of the operation here
uppercaseLetter1 = chr(random.randint(64,90)) #Generates a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(64,90)) #Generates a random Uppercase letter (based on ASCII code)

lowercaseLetter1 = chr(random.randint(97,122)) #Generates a random Lowercase letter (based on ASCII code)
lowercaseLetter2 = chr(random.randint(97,122)) #Generates a random Lowercase letter (based on ASCII code)

digit1 = chr(random.randint(48, 57)) #Generates a random digit (0 - 9)
digit2 = chr(random.randint(48, 57)) #Generates a random digit (0 - 9)

punctuationSign1 = chr(random.randint(33, 152)) 
punctuationSign2 = chr(random.randint(33, 152)) 

#Generating password using all characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
password = shuffle(password)

#Output
print("This is your random paswword: ", password)