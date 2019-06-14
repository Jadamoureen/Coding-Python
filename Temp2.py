def main():
   fahr = input("Enter the temperature in F: ")
   fah = int(fahr)
   cel = (fah - 32)* 5.0/9.0
   return(cel)
temp = main()
print('The temperature in C is:', temp)
