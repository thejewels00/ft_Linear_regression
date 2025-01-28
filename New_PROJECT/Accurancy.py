
import sys
import os
import csv



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
    
def extract_data():
       
        data_file = "data.csv"
        value = []

        if not os.path.isfile(data_file):
            sys.exit(f"Error: File {data_file} doesn't exist")
        if not os.access(data_file, os.R_OK):
            sys.exit(f"Error: Acess denied for {data_file}")


        with open(data_file, 'r') as file :
            value_obj = csv.reader(file)
            # print(type(value))
            for row in value_obj:
                # print(row) #to remove
                value.append(row)


            # print("all value : ", value) #to remove
            #print(type(value))
            del(value[0])
            # self.mae = self.mean_absolute_error()

        return value
    
def estimatePrice(theta0,theta1 ,km):
    return (theta0 + (theta1 * float(km)))


def r2_score(value, theta0, theta1):
    actual_values = [float(line[1]) for line in value]
    predicted_values = [estimatePrice(theta0, theta1,float(line[0])) for line in value]
    mean_y = sum(actual_values) / len(actual_values)

    # Calculate the total sum of squares (TSS) and residual sum of squares (RSS)
    tss = sum((y - mean_y) ** 2 for y in actual_values)
    rss = sum((y - y_pred) ** 2 for y, y_pred in zip(actual_values, predicted_values))

    # Compute R²
    r2 = 1 - (rss / tss)
    return r2


if __name__ == "__main__":
    theta0 , theta1 = extract_values("values.psv")


    data = extract_data()
    # print (data)


    print(f"The R² score is: {r2_score(data, theta0, theta1):.4f}")  # Calculate and display R² score
    





