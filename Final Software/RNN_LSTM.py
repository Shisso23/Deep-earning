
# Recurrent Neural Network
# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import array
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import sys

class Rnn_predict:

    X_train = []
    y_train = []
    X_test=[]
    y_test=[]
    sc=None

    def split_sequence(self,sequence, n_steps):
        X, y = list(), list()
        for i in range(len(sequence)):
            # find the end of this pattern
            end_ix = i + n_steps
            # check if we are beyond the sequence
            if end_ix > len(sequence) - 1:
                break
            # gather input and output parts of the pattern
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
            X.append(seq_x)
            y.append(seq_y)
        return array(X), array(y)

    def preprocess(self, dataset):
        # dataset_train=""
        # Importing the training set
         dataset_train = pd.read_csv(dataset)
         self.sc = MinMaxScaler(feature_range=(0, 1))
         training_set = dataset_train.iloc[:, 1:2].values  # using the open values. column 2

        # Feature Scaling

         training_set_scaled = self.sc.fit_transform(training_set)

         test_set_size = int((len(training_set_scaled) * 15) / 100)# 15% split

         test_set_scaled = training_set_scaled[len(training_set_scaled) - test_set_size:]  # the last 90 are used for testing. # 90 is the test set size



        # real_stock_price = dataset_test.iloc[:, 1:2].values

        # Getting the predicted stock price of 2017
        # dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis = 0)
        # inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
         test_set_scaled = test_set_scaled.reshape(-1, 1)
         #test_set_scaled = sc.fit_transform(test_set_scaled)

         training_set_scaled = training_set_scaled[ :len(training_set_scaled)-test_set_size]  # 90 is the test set size

         return training_set_scaled,test_set_scaled


        # Creating a data structure with 60 timesteps and 1 output


    def cross_validation(self,trainset,testset):
        self.X_train, self.y_train = self.split_sequence(trainset, 60)  # using 60 time steps

        # Reshaping
        self.X_train = np.reshape(self.X_train, (self.X_train.shape[0], self.X_train.shape[1], 1))
        self.X_test, y_test = self.split_sequence(testset, 60)
        # print(X_test.shape)
        # sys.exit()
        self.X_test = np.reshape(self.X_test, (self.X_test.shape[0], self.X_test.shape[1], 1))
        self.y_test = np.reshape(y_test, (y_test.shape[0], y_test.shape[1], 1))

        return self.X_train,self.X_test,self.y_train,y_test

    def trainModel(self):

        # Part 2 - Building the RNN

        # Initialising the RNN
        regressor = Sequential()

        # Adding the first LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = 40, return_sequences = True, input_shape = (self.X_train.shape[1], 1)))
        regressor.add(Dropout(0.2))

        # Adding a second LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(0.2))

        # Adding a third LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(0.2))

        # Adding a fourth LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = 50))
        regressor.add(Dropout(0.2))

        # Adding the output layer
        regressor.add(Dense(units = 1))

        # Compiling the RNN
        regressor.compile(optimizer = 'Adam', loss = 'mean_squared_error')

        # Fitting the RNN to the Training set
        regressor.fit(self.X_train, self.y_train, epochs = 100, batch_size = 50)
        return regressor


    # Part 3 - Making the predictions and visualising the results
    #3900
    # Getting the real stock price of 2017

    #print(inputs.__sizeof__())
    #sys.exit()


    def testModel(self, regressor):

        predicted_stock_price = regressor.predict(self.X_test)


        #predictions_inversed = []  # will be used for plotting
        true_values_inversed = []
        Y_preds = predicted_stock_price
        Y_true = self.y_test

       # sys.exit()
        output = ""
        for i in range(len(predicted_stock_price)):
            output += "Expected output-------: " + str(self.y_test[i][0][0]) + "  predicted-------: " + str(
                predicted_stock_price[i][0]) + "\n"

            # unscaling the features

            #predictions_inversed.append(predictions[i][j])  # here because the inverse method accepts an array of dimension less than 3
            for j in range(len(predicted_stock_price[i])):

                true_values_inversed.append(self.y_test[i][j])

            mse = mean_squared_error(Y_true[i], Y_preds[i])  # Calculation of Mean Squared Error (MSE)
            output += "=========>Mean squared error: " + str(mse) + "\n\n\n"
        print(output)

        output += "The overall Mse is: " + str(mean_squared_error(true_values_inversed, predicted_stock_price))
        ########################q
        #print(predicted_stock_price)
        #print(true_values_inversed)
        #sys.exit()
        predicted_stock_price = self.sc.inverse_transform(predicted_stock_price)
        true_values_inversed=self.sc.inverse_transform(true_values_inversed)

        print("end of testModel")
        return predicted_stock_price,true_values_inversed, output

    def plotAndSave(self, real_stock_price,predicted_stock_price):
        # Visualising the results
        print("beginning of plot")
        plt.title('RNN_LSTM prediction')
        plt.plot(real_stock_price, color = 'red', label = 'Real  Stock Price')
        plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted  Stock Price')
        #plt.title('Google Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Google Stock Price')
        plt.legend()

        plt.gcf() #get current figure. before saving it
        plt.savefig('RNN_Lstm_plot.png',dpi=100) # save the figure as Cnn_plot.png in the current working directory

        plt.show()
    #sys.exit()
'''obj=Rnn_predict()

train_set, test_set= obj.preprocess('Google_Stock_Price_Train.csv')
x_train, y_train, x_test,y_test=obj.cross_validation(train_set, test_set)
#obj.testModel()
model=obj.trainModel()
true_values_inversed=obj.testModel(model)[1]
predictions_inversed=obj.testModel(model)[0]

output=obj.testModel(model)[2]
#print(predictions)
obj.plotAndSave(true_values_inversed, predictions_inversed)'''
