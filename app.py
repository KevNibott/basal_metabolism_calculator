n = 0

def intro():
    global n
    if n == 0:
        print("Hi! This is a basal metabolic rate calculator")
        print("We are going to ask you some question to collect the data needed (type 'exit' any time to finish). Let's begin:")
    else:
        print("Ok, let's start over agian")
    n += 1

def data():
    global sexo
    global peso
    global altura
    global edad
    while True:
        sexo = input("Tell me your biological sex: M (for Male), F (for Female)\n > ")
        if sexo.lower() == "exit":
            exit()
        elif sexo.lower() == "m" or sexo.lower() == "f":
            break
        else:
            print("Sorry, that's not a valid answer. Try again")
            continue
    while True:
        peso = input("Tell me your weight in kg\n > ")
        if peso.lower() == "exit":
            exit()
        elif "," in peso:
            print("That's an incorrect value, use '.' to separate decimals instead of ','")
        elif "." in peso:
            peso = float(peso)
            break
        else:
            peso = int(peso)
            break
    while True:
        altura = input("Tell me your height\n > ")
        if altura.lower() == "exit":
            exit()
        elif " " in altura:
            print("You used feet and inches for your height, right? Anyway, let's continue...")
            altura = conversor_feet_inches(altura)
            break
        elif "." in altura:
            if float(altura) > 10:
                print("You used centimeters for your height, right? Anyway, let's continue...")
                altura = float(altura)
                break
            elif float(altura) > 2.4:
                print("You used feet for your height, right? Anyway, let's continue...")
                altura = conversor_feet(altura)
                break
            else:
                print("You used meters for your height, right? Anyway, let's continue...")
                altura = float(altura) * 100
                break
        elif "," in altura:
            print("That's an incorrect value, use '.' to separate decimals instead of ','")
            continue
        else:
            altura = int(altura)
            print("You used centimeters for your height, right? Anyway, let's continue...")
            break
    edad = input("Ok and last but not least, how old are you?\n > ")
    if edad.lower() == "exit":
        exit()
    else:
        edad = int(edad)

def calculator(sex):
    if sex.lower() == "m":
        tmb = int((10*peso) + (6.25*altura) - (5*edad) + 5)
        print(f"For {altura}cm of height, {peso}kg of weight and a {edad} years old male, your basal metabolism rate is: {tmb}kcal")
    else:
        tmb = int((10*peso) + (6.25*altura) - (5*edad) - 161)
        print(f"For {altura}cm of height, {peso}kg of weight and a {edad} years old female, your basal metabolism rate is: {tmb}kcal")
    return tmb

def conversor_feet_inches(height):
    global altura
    feet, inches = height.split(" ")
    decimal_feet = int(inches) * 0.083
    total_height_in_feet = int(feet) + decimal_feet
    altura = total_height_in_feet * 30.48
    return altura

def conversor_feet(height):
    global altura
    altura = float(height)*30.48
    return altura

def loop():
    decision = input("Enter 'exit' to finish or 'any key' for more calculations\n > ")
    if decision.lower() == "exit":
        exit()
    else:
        app()

def app():
    intro()
    data()
    calculator(sexo)
    loop()

app()

