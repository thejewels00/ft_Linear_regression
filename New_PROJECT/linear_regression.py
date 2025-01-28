import sys
import os
import csv
import matplotlib.pyplot as plt



class linear_regression :

    def __init__(self) :
        print("constructor hello")
        self.theta0 = 0.0
        self.theta1 = 0.0   
        self.learning_rate = 0.001
        self.mae = 0.0
        self.mae_old = 0.0
        self.extract_data()



    def extract_data(self):
        if len(sys.argv) == 1:
            self.data_file = input("Enter file name : ")
        else :
            self.data_file = sys.argv[1]

        if len(self.data_file) < 1 :
            sys.exit("Error : try next time incha allah !")   

        self.value = []

        if not os.path.isfile(self.data_file):
            sys.exit(f"Error: File {self.data_file} doesn't exist")
        if not os.access(self.data_file, os.R_OK):
            sys.exit(f"Error: Acess denied for {self.data_file}")


        with open(self.data_file, 'r') as file :
            value_obj = csv.reader(file)
            # print(type(value))
            for row in value_obj:
                # print(row) #to remove
                self.value.append(row)


            # print("all value : ", self.value) #to remove
            #print(type(self.value))
            del(self.value[0])
            # self.mae = self.mean_absolute_error()


    def mean_absolute_error(self):
        i = 1
        sum = 0
        for line in self.value:
            sum += abs(self.estimatePrice(line[0]) - float(line[1]))
            i += 1


        print("MAE, ", (sum / i))

        return (sum / i)            
        

    def normalisation_data(self):
        i = 0
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')

        for line in self.value:
            if (float(line[0]) < self.min_x):
                self.min_x = float(line[0])
            if (float(line[0]) > self.max_x):
                self.max_x = float(line[0])
            if (float(line[1]) < self.min_y):
                self.min_y = float(line[1])
            if (float(line[1]) > self.max_y):
                self.max_y = float(line[1])

        tmp_x = self.max_x - self.min_x
        tmp_y = self.max_y - self.min_y 
        for line in self.value:
            line[0] = (float(line[0]) - self.min_x) / tmp_x
            line[1] = (float(line[1]) - self.min_y) / tmp_y

        print("donnees normalisee" ,self.value)




    def estimatePrice(self, km):
        return (self.theta0 + (self.theta1 * float(km)))

    def print_val(self):
        # print(self.value)
        print(f"theta0 = {self.theta0} theta1 = {self.theta1} MAE = {self.mae}")
        

    def gradient_theta0(self):
        sum = 0.0
        i = 1

        for line in self.value:
            sum += (self.estimatePrice(line[0]) - float(line[1])) 
            i += 1
        return (self.learning_rate * (sum / i))




    def gradient_theta1(self):
        sum = 0.0
        i = 1

        for line in self.value:
            sum += (self.estimatePrice(line[0]) - float(line[1])) * float(line[0])
            i += 1
        return (self.learning_rate * (sum / i))

    def training_model(self):
        self.mae = self.mean_absolute_error()

        mae_delta = self.mae
        while mae_delta > 0.0000001 or mae_delta < -0.0000001:
            theta0_slop = self.gradient_theta0()
            theta1_slop = self.gradient_theta1()


            self.theta0 -= theta0_slop
            self.theta1 -= theta1_slop


            self.mae_old = self.mae
            self.mae = self.mean_absolute_error()
            mae_delta = self.mae - self.mae_old

        self.theta1 = (self.max_y - self.min_y) * self.theta1 / \
                (self.max_x - self.min_x)
        self.theta0 = self.min_y + ((self.max_y - self.min_y) * \
                self.theta0) + self.theta1 * (1 - self.min_x)
        self.save_thetas()
        print("delta: ", mae_delta)


    def save_thetas(self):
        with open("values.psv", 'w') as file:
            file.write(f"{self.theta0}|{self.theta1}")

    def plot_value(self):
        tmp_val = self.value.copy()  # Copie pour ne pas modifier self.value


        # Conversion des données normalisées en valeurs réelles
        tmp = list(zip(*tmp_val))
        tmp = [list(tmp[0]), list(tmp[1])]
        plot_val = [[], []]
        for i in tmp[0]:
            real_x = self.min_x + (self.max_x - self.min_x) * float(i)
            plot_val[0].append(real_x)
        for i in tmp[1]:
            real_y = self.min_y + (self.max_y - self.min_y) * float(i)
            plot_val[1].append(real_y)

        # Tracé des points de données réelles
        plt.title('Real Values and Regression Line')
        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.plot(plot_val[0], plot_val[1], 'bo', label='Data Points')

        # Tracé de la ligne de régression
        x_line = [self.min_x, self.max_x]
        y_line = [self.estimatePrice(self.min_x), self.estimatePrice(self.max_x)]
        plt.plot(x_line, y_line, 'r-', label='Regression Line')

        # Ajustement des axes pour plus de visibilité
        plt.axis([
            self.min_x - abs(self.max_x * 0.1), 
            self.max_x + abs(self.max_x * 0.1), 
            self.min_y - abs(self.max_y * 0.1), 
            self.max_y + abs(self.max_y * 0.1)
        ])
        plt.legend()
        plt.show()


    # def print_acurancy(self):
    #     print("the mean absolute error is : ", self.mean_absolute_error())
        
        




if __name__ == "__main__":

    model = linear_regression()
    model.normalisation_data() #linear scaling method :) done
    model.training_model()
    #next ploting data  - bonus
    # model.print_val()

    model.print_acurancy() #fixing this shit 

    model.plot_value()
    

