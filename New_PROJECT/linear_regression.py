import sys
import os
import csv



class linear_regression :

    def __init__(self) :
        print("constructor hello")
        self.theta0_old = 0.0
        self.theta1_old = 0.0   
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
                print(row) #to remove
                self.value.append(row)


            print("all value : ", self.value) #to remove
            #print(type(self.value))
            del(self.value[0])


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
        return (self.theta0_old + (self.theta1_old * float(km)))

    def print_val(self):
        print(self.value)

    def gradient_theta0(self):
        sum = 0.0

        for line in self.value:
            sum +=  #u are working here
    

    def training_model(self, learning_rate, print_error):

        

    

        

            






if __name__ == "__main__":

    model = linear_regression()
    model.normalisation_data() #linear scaling method :) done
    #next step training model :D
    # model.print_val()
    

