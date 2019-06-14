def temp():

    fahr = input('enter fahr temp:')

    fahr = int(fahr)

    cel = (((fahr-32)*5.0)/9.0)

    return cel

bg = temp()

print(bg)