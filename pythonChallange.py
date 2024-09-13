name = input("What is your name? ")
monthSales = float(input("How much did you make in sales this month? "))
commission = (float(monthSales) * 0.13)
print("Welcome, " + name + ". You've made a total of " + str(round(commission)) + " dollars! ")