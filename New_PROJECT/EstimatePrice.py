

def input_mileage():

    while True:
        try :
            mileage = float(input("Enter the mileage of the car: "))
            if(mileage >= 0):
                return mileage
            else:
                print("Error: Please try again.") 
        except ValueError:
            print("Error: Please try again. Use a number.")



def extract_values(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            parts = line.split("|")
            theta0 = float(parts[0])
            theta1 = float(parts[1])
            print(f"Value of theta0={theta0} and theta1={theta1}")
            return theta0, theta1
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0
    


if __name__ == "__main__":
    mileage = input_mileage()
    theta0 , theta1 = extract_values("values.psv")

    print(f"the prediction of this {mileage} is" , theta0 + (theta1 * mileage))

