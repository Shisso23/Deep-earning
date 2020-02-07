
# univariate multi-step encoder-decoder lstm example
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import RepeatVector
from keras.layers import TimeDistributed
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from sklearn.preprocessing import MinMaxScaler

class EncoderDecoder_predict:


    # Importing the training set
    #dataset_train = pd.read_csv('Google_Stock_Price_Train.csv')
    #training_set = dataset_train.iloc[:, 1:2].values  # using the open values. column 2

    sc=None
    # choose a number of time steps
    n_steps_in, n_steps_out = 60, 1  # predict the next 5 prices given the last 30 prices in the trainingset
    n_features = 1  # output

    X=[]
    y=[]
    X_test=[]
    y_test=[]

    # split a univariate sequence into samples

    def split_sequence(self,sequence, n_steps_in, n_steps_out):
        X, y = list(), list()
        for i in range(len(sequence)):
            # find the end of this pattern
            end_ix = i + n_steps_in
            out_end_ix = end_ix + n_steps_out
            # check if we are beyond the sequence
            if out_end_ix > len(sequence):
                break
            # gather input and output parts of the pattern
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix:out_end_ix]
            X.append(seq_x)
            y.append(seq_y)
        return array(X), array(y)

    def preprocess(self , dataset):
        # define input sequence
        dataset_train=pd.read_csv(dataset)
        training_set= dataset_train.iloc[:, 1:2].values  # using the open values. column 2
        # Feature Scaling
        test_set_size = int((len(training_set) * 15) / 100)
        #print(test_set_size)
        #sys.exit()
        self.sc = MinMaxScaler(feature_range=(0, 1))
        training_set = self.sc.fit_transform(training_set)

        test_set = training_set[len(training_set) - test_set_size:]  # the last 90 are used for testing. # 90 is the test set size

        training_set = training_set[:len(training_set) - test_set_size]  # 90 is the test set size

        return training_set, test_set

    def cross_validation(self, trainset, testset):
        # split into samples
        self.X, self.y = self.split_sequence(trainset, self.n_steps_in, self.n_steps_out)
        # reshape from [samples, timesteps] into [samples, timesteps, features]

        self.X = self.X.reshape((self.X.shape[0], self.X.shape[1], self.n_features))
        self.y = self.y.reshape((self.y.shape[0], self.y.shape[1], self.n_features))

        self.X_test, self.y_test = self.split_sequence(testset, self.n_steps_in, self.n_steps_out)

        self.X_test = self.X_test.reshape((int(self.X_test.size / self.n_steps_in), self.n_steps_in,
                                 self.n_features))  # for each n_steps_in rows in the test set it will output the next n_steps_out predictions
        return self.X,self.y, self.X_test,self.y_test

    def trainModel(self):
        # define model
        model = Sequential()
        model.add(LSTM(100, activation='relu', input_shape=(self.n_steps_in, self.n_features)))
        #model.add(Dropout(0.2))
        model.add(RepeatVector(self.n_steps_out))
        model.add(LSTM(100, activation='relu', return_sequences=True))
        model.add(LSTM(100, activation='relu', return_sequences=True))
        model.add(LSTM(100, activation='relu', return_sequences=True))
        model.add(TimeDistributed(Dense(1)))
        model.compile(optimizer='adam', loss='mse')
        # fit model
        model.fit(self.X, self.y, epochs=100, verbose=1)
        print("end of training")
        return model


    def testModel(self,model):

        output=""
        predictions = model.predict(self.X_test, verbose=0)

    #calculate mean squared errors using arrays of y_test and arrays of predictions

    #taking each 5 arrays of  arrays of values and put them in an array so it can be an array of values then calculate the mse for each n_out_steps

        predictions_inversed=[]   # will be used for plotting
        true_values_inversed=[]
        for i in range(len(predictions)) :
            Y_preds=[]
            Y_true=[]
            for j in range(self.n_steps_out):  #for each 5 preds
                t_value=self.y_test[i][j][0]
                Y_true.append(t_value)
                p_value=predictions[i][j][0]
                Y_preds.append(p_value)
                output+="Expected output-------: "+str(t_value)+ "  predicted-------: "+str(p_value)+"\n"

                # unscaling the features
                predictions_inversed.append( predictions[i][j])  # here because the inverse method accepts an array of dimension less than 3
                true_values_inversed.append(self.y_test[i][j])
            mse=mean_squared_error(Y_true,Y_preds)# Calculation of Mean Squared Error (MSE)

            output+="=========>Mean squared error: "+ str(mse)+"\n\n\n"
        print(output)
        print()


        predictions_inversed = np.array(predictions_inversed)
        true_values_inversed = np.array(true_values_inversed)
        predictions_inversed = predictions_inversed.reshape(-1, 1)
        true_values_inversed = true_values_inversed.reshape(-1, 1)
        output += "The overall Mse is: " + str(mean_squared_error(true_values_inversed, predictions_inversed))
        predictions_inversed=self.sc.inverse_transform(predictions_inversed)
        true_values_inversed=self.sc.inverse_transform(true_values_inversed)





        print("end of testing")

        return predictions_inversed, true_values_inversed,output
   # print ("the overall Mse is: ",mse)
    #print(predictions)
    def plotAndSave(self,true_values, predicted_values ):

        plt.plot(true_values, color = 'red', label = 'Real Stock Price')
        plt.plot(predicted_values, color = 'blue', label = 'Predicted  Stock Price')
        plt.title('Encoder-decoder prediction')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.legend()

        plt.gcf() #get current figure. before saving it
        plt.savefig('Encoder-decoder_plot.png',dpi=100) # save the figure as Cnn_plot.png in the current working directory
        plt.show()
        print("end of plotting")
        #sys.exit()

'''obj=EncoderDecoder_predict()

trainset,testset=obj.preprocess('Google_Stock_Price_Train.csv')
#obj.testModel()

X,y,X_test, y_test=obj.cross_validation(trainset, testset)
model=obj.trainModel()
true_values_inversed=obj.testModel(model)[1]
predictions_inversed=obj.testModel(model)[0]


output=obj.testModel(model)[2]
#print(predictions)
obj.plotAndSave(true_values_inversed, predictions_inversed)'''

#sys.exit()
