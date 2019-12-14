college = 'Extraordinary'
clas = 'course'
print(college)
print(college[1:4])
print(college[:3]) #Starts from 0 position
print(college[1:]) #Goes till the end of the string
print(college[0::2]) # [Start_pos : End_pos : Step_distance]
print(college[-2:-12:-1])
print(college[::-1]) #reversing a string in this step

#Starting position is always included and end position is always excluded.

print(college + clas) #To add two strings
print(college * 2) #It prints the string 2 times consicutively

for ch in college:   #loop to print every character in a string
    print(ch, end=' ')
print('\n')

x = "abCDeFGhi" 
n = x.isalpha()
'''to check that every character is a alphabet or not.
Always returns bool value either true or false'''
print(n)
n = x.isdigit()
'''to check that every character of string is a digit or not.
Always returns bool value i.e. True or False'''
print(n)
n = x.islower()
print(n)

y = x.upper() #to convert lowercase to uppercase letters
print(y)
y = x.lower() #to convert uppercase to lowercase letters
print(y)

z = '    abcd  '
print(z.lstrip()) #To remove spaces from left
print(z.rstrip()) #To remove spaces form right

print(ord('A')) #prints order/ASCII value of given character
print(ord('a'))

print(chr(65)) #prints character relative to ASCII value mentioned
print(chr(102))
print(chr(87))

