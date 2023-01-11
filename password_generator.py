#The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.
import secrets
# the string module is abstract from the secret libery file
import string
# here the letters means that it can include both upper and lower case of the letters i.e the lower be like a,b,c,... and upper be like A,B,C,..... and we have just 26 letters and  it can include 52 letters in password generators which is abstact from the string of secrets file so it can be taken by . from which we define by import in python 
letters= string.ascii_letters
# there are 10 digits in python which also can taken from string in python file
digit = string.digits
# the meaning of spacial keyword are present far than letter and digit in computer .and it can be defined as some name stored as variable and given by punctuation 
special_char = string.punctuation
# and now i add/concaninate  all this thing to make some strong password as it gives in terminal which is generated by computer
alphabets = letters+digit+special_char
# and now i made it empty which is stored some password in terminal to take

pw = ""
# and i made fixed to take some length of password which is gives to us by computer . we can made any of length to give .
pwd_length =100
# i made a range of password named as m within the length of which i made fixed above to it.
for  m in range(pwd_length):
#  password can join with its module and its gives us in choice because string is fixed in a length and for length we can only use as a choice function and i passed as a hole alphabets on it
   pw = pw+"".join(secrets.choice(alphabets))
# and finally i print my password in the terminal 😄.yahho!.
   print(pw)