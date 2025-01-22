def take_mileage():
    while  True:
        try :
            number = float(input("please enter mileage : "))
            if (number >= 0):
                return number
            else :
                print("Error: Negative !? Try again.")
        except ValueError:
            print("Error : Not a number, Try again.")



def extract_values(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            parts = line.split("|")

            a = float(parts[0])
            b = float(parts[0])
            print(f"Value of theta0={a} and theta1={b}")
            return a,b
               
    except FileNotFoundError:
        print(f"Fichier '{filename}' introuvable.")
        return 0, 0
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return 0, 0
    

theta0 , theta1 = extract_values("values.psv")
mileage = take_mileage()

print(f"the prediction of this {mileage} is" , theta0 + (theta1 * mileage))




