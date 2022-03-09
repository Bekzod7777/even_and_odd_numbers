#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
a=4444
b=((a%10)%2)+((a//10)%10)%2+(((a//100)%10)%2)+(a//1000)%2
print(4-b,'ta juft son')
