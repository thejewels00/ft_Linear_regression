import sys
import os
import csv
import matplotlib.pyplot as plt

class linear_regression :

    def __init__(self) :
        if len(sys.argv) == 1:
            self.data_file = input("Enter file name : ")
        else :
            self.data_file = sys.argv[1]

        if len(self.data_file) < 1 :
            sys.exit("Error : File name is too short")

        self.extract_data()
        self.theta0 = 0.0
        self.theta1 = 0.0
        self.temp_theta_0 = 1.0
        self.temp_theta_1 = 1.0
        self.prev_mse = 0.0
        self.curent_mse = self.mean_square_error()
        self.delta_mse = self.curent_mse


    
    def extract_data(self):
        self.value = []

        if not os.path.isfile(self.data_file):
            sys.exit(f"Error: File {self.data_file} doesn't exist")
        if not os.access(self.data_file, os.R_OK):
            sys.exit(f"Error: Access denied for {self.data_file}")

        with open(self.data_file, 'r') as csv_file:
            try:
                dict_val = csv.reader(csv_file, delimiter=',')
                for row in dict_val:
                    self.value.append(row)
                # print(self.value)
            except:
                sys.exit("Error: File {:} cannot be read")
    
    def estimatePrice(self, mileage):
        return ((self.temp_theta_0 + (self.temp_theta_1 * float(mileage))))
    

    

    def standarize_data(self):
        i = 0
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')

        #this part used to extcract the min and max values of x and y
        for line in self.value:
            if(i > 0):
                if (float(line[0]) < self.min_x):
                    self.min_x = float(line[0])
                if (float(line[0]) > self.max_x):
                    self.max_x = float(line[0])
                if (float(line[1]) < self.min_y):
                    self.min_y = float(line[1])
                if (float(line[1]) > self.max_y):
                    self.max_y = float(line[1])
            else:
                i = 1

        #this part used to standarize the data
        for line in self.value :
            if(i > 0):
                line[0] = (float(line[0]) - self.min_x) / (self.max_x - self.min_x)
                line[1] = (float(line[1]) - self.min_y) / (self.max_y - self.min_y)
            else:
                i = 1

    def gradient0(self) :
        i = 0
        tmp_summ = 0.0

        for line in self.value :
            if (i > 0) :
                tmp_summ += (self.estimatePrice(line[0]) - float(line[1]))
            i += 1
        
        return (self.learning_rate * (tmp_summ / (i - 1)))


    def gradient1(self) :
        i = 0
        tmp_summ = 0.0

        for line in self.value :
            if (i > 0) :
                tmp_summ += (self.estimatePrice(line[0]) - float(line[1])) \
                    * float(line[0])
            i += 1
        
        return (self.learning_rate * (tmp_summ / (i - 1)))

    def mean_square_error(self) :

        i = 0
        tmp_summ = 0

        for line in self.value :
            if (i > 0) :
                tmp_diff = self.estimatePrice(line[0]) - float(line[1])
                tmp_diff *= tmp_diff
                tmp_summ += tmp_diff
            i += 1

        return (tmp_summ / (i - 1))

    def save_theta(self):
        with open("values.psv", 'w') as file:
            file.write(f"{self.theta0}|{self.theta1}")

    def train_model(self, learning_rate, print_error):
        self.learning_rate = learning_rate

        self.standarize_data()
        while self.delta_mse > 0.0000001 or self.delta_mse < -0.0000001:
            self.theta0 = self.temp_theta_0
            self.theta1 = self.temp_theta_1
            self.temp_theta_0 -= self.gradient0()
            self.temp_theta_1 -= self.gradient1()
            self.prev_mse = self.curent_mse
            self.curent_mse = self.mean_square_error()
            self.delta_mse = self.curent_mse - self.prev_mse


            self.theta_1 = (self.max_y - self.min_y) * self.theta_1 / \
                (self.max_x - self.min_x)
            self.theta_0 = self.min_y + ((self.max_y - self.min_y) * \
                self.theta_0) + self.theta_1 * (1 - self.min_x)
        
            if(print_error ==  1):
                print(f"theta0 = {self.temp_theta_0} theta1 = {self.temp_theta_1} MSE = {self.curent_mse}")
            
            self.save_theta()

    def plot_value(self):
        tmp_val = self.value
        tmp_val.pop(0)

        tmp_theta0 = self.temp_theta_0
        tmp_theta1 = self.temp_theta_1
        self.temp_theta_0 = self.theta0
        self.temp_theta_1 = self.theta1

        print(self.min_y, self.max_y)
        tmp = list(zip(*tmp_val))
        tmp = [list(tmp[0]), list(tmp[1])]
        plot_val = [[], []]
        for i in tmp[0] :
            i = self.min_x + (self.max_x - self.min_x) * i
            plot_val[0].append(i)
        for i in tmp[1] :
            i = self.min_y + (self.max_y - self.min_y) * i
            plot_val[1].append(i)
        plt.title('Real values')
        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.plot(plot_val[0], plot_val[1], 'bo')
        plt.plot([self.min_x, self.max_x], [self.estimatePrice(self.min_x), \
            self.estimatePrice(self.max_x)])
        plt.axis([self.min_x - abs(self.max_x * 0.1), self.max_x + \
            abs(self.max_x * 0.1), self.min_y - abs(self.max_y * 0.1), \
            self.max_y + abs(self.max_y * 0.1)])
        plt.show()
        self.tmp_theta_0 = tmp_theta0
        self.tmp_theta_1 = tmp_theta1



        




model = linear_regression()
model.train_model(0.1, 1)




