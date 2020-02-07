# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import tqdm
from PyQt5 import QtCore , QtWidgets, QtGui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 620)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setStyleSheet("background-image: url(\"dark_see.jpg\"); ")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        #self.tabWidget.setStyleSheet("border-style:none")
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 911, 621))
        self.tabWidget.setObjectName("tabWidget")
        #self.tab_4 = QtWidgets.QWidget()
        #self.tab_4.setObjectName("tab_4")
        #self.frame_3 = QtWidgets.QFrame(self.tab_4)
        #self.frame_3.setGeometry(QtCore.QRect(70, 40, 771, 491))
        #self.frame_3.setStyleSheet( "\n" " border-style:none;")
        #self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.frame_3.setObjectName("frame_3")
        #self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        #self.textEdit.setGeometry(QtCore.QRect(40, 80, 691, 341))
       # self.textEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
#"font: 25 16pt \"Calibri Light\";")
        #self.textEdit.setObjectName("textEdit")
       # self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        #self.pushButton_12.setGeometry(QtCore.QRect(290, 430, 161, 41))
        #self.pushButton_12.setStyleSheet("color: rgb(85, 170, 255);\n"
#"font: 75 16pt \"MS Shell Dlg 2\";")
       # self.pushButton_12.setObjectName("pushButton_12")
       # self.label_6 = QtWidgets.QLabel(self.frame_3)
       # self.label_6.setGeometry(QtCore.QRect(650, 439, 91, 31))
        #self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
        #self.label_6.setObjectName("label_6")
        #self.label_7 = QtWidgets.QLabel(self.frame_3)
        #self.label_7.setGeometry(QtCore.QRect(270, 10, 261, 51))
        #self.label_7.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
#"\n"
#"color: rgb(82, 186, 255);")
        #self.label_7.setObjectName("label_7")
        #self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(90, 40, 691, 421))
        #self.frame_2.setStyleSheet("background-color: rgb(245, 255, 242);")
        self.frame_2.setStyleSheet(" border-style: border-right-style: outset;" "\n"
  "border-right-color: coral;" "\n" "border-right-width: 7px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 361, 81))
        self.label_2.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
"color: rgb(116, 183, 255);")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(80, 160, 141, 71))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.fileName = QtWidgets.QTextEdit(self.frame_2)
        self.fileName.setGeometry(QtCore.QRect(230, 170, 211, 51))
        self.fileName.setObjectName("fileName")
        self.choose_file = QtWidgets.QPushButton(self.frame_2)
        self.choose_file.setGeometry(QtCore.QRect(470, 170, 91, 51))
        self.choose_file.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(116, 183, 255);")
        self.choose_file.setObjectName("choose_file")
        ###################################
        self.choose_file.clicked.connect(lambda:self.select_file())
        self.choose_file.setObjectName("Choose_file")


        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setGeometry(QtCore.QRect(290, 250, 101, 41))
        self.toolButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));")
        self.toolButton.setObjectName("toolButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        #self.tab_2.setEnabled(False)
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(20, 50, 791, 441))
        self.frame.setAccessibleName("")
#         self.frame.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
# "color: rgb(116, 183, 255);\n"
# "font: 75 20pt \"MS Shell Dlg 2\";\n"
# "background-color: rgb(245, 255, 242);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(100, 110, 631, 211))

        self.groupBox.setStyleSheet("color: rgb(116, 183, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 30, 161, 71))
        self.pushButton.setStyleSheet("background-color: rgb(184, 231, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        #self.pushButton_2.setGeometry(QtCore.QRect(80, 120, 161, 61))
        self.pushButton_2.setGeometry(QtCore.QRect(230, 130, 161, 61));
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(184, 231, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 30, 181, 71))
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(184, 231, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        #self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        #self.pushButton_4.setGeometry(QtCore.QRect(380, 120, 181, 61))
        #self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);\n"
#"background-color: rgb(184, 231, 255);")
        #self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 40, 301, 51))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 75 20pt " "MS Shell Dlg 2; ""\n" "color: rgb(184, 231, 255);")
        #self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        #self.pushButton_5.setGeometry(QtCore.QRect(340, 330, 111, 61))
#         self.pushButton_5.setStyleSheet("color: rgb(184, 231, 255);\n"
# "font: 14pt \"MS Shell Dlg 2\";\n"
# "font: 12pt \"MS Shell Dlg 2\";\n"
# "font: 8pt \"MS Shell Dlg 2\";\n"
# "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
# "font: 12pt \"MS Shell Dlg 2\";")
#         self.pushButton_5.setObjectName("pushButton_5")
        self.progressBar = QtWidgets.QProgressBar(self.frame);
        self.progressBar.setObjectName("progressBar");
        self.progressBar.setGeometry(QtCore.QRect(100, 360, 621, 41));
        self.progressBar.setValue(0);

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 881, 581))
        #self.tabWidget_2.setStyleSheet("background-color: rgb(245, 255, 242);")
        #"background-color: rgb(245, 255, 242); \n"
        self.tabWidget_2.setStyleSheet( "\n" " border-style:none;")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        '''
        self.scrollArea = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea.setGeometry(QtCore.QRect(40, 60, 611, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 269))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        '''
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setGeometry(QtCore.QRect(150, 20, 261, 31))
        self.label_4.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(116, 183, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 460, 131, 71))
        self.pushButton_6.setStyleSheet("background-color: rgb(184, 231, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 460, 131, 71))
        self.pushButton_7.setStyleSheet("background-color: rgb(184, 231, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_8.setGeometry(QtCore.QRect(600, 460, 131, 71))
        self.pushButton_8.setStyleSheet("background-color: rgb(184, 231, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_5)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 821, 441))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.plainTextEdit.setStyleSheet("selection-background-color: rgb(255, 255, 255);\n"
                                                "font: italic 12pt \"Calibri\";\n"
                                                "\n" "selection-color: rgb(116, 183, 255);")

        self.graphic_view = QtWidgets.QWidget()
        self.graphic_view.setObjectName("graphic_view")
        self.graphicsView = QtWidgets.QGraphicsView(self.graphic_view)
        self.graphicsView.setGeometry(QtCore.QRect(10, 60, 821, 441))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("selection-background-color: rgb(255, 255, 255);\n"
                                                  "font: italic 12pt \"Calibri\";");

        self.label_8=QtWidgets.QLabel(self.graphic_view)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 821, 4411))
        self.label_8.setObjectName("image")

        self.label_5 = QtWidgets.QLabel(self.graphic_view)
        self.label_5.setGeometry(QtCore.QRect(340, 10, 131, 41))
        self.label_5.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(116, 183, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.graphic_view)
        #self.pushButton_9.setGeometry(QtCore.QRect(70, 510, 101, 41))
        self.pushButton_9.setGeometry(QtCore.QRect(710, 100, 131, 41));
        self.pushButton_9.setStyleSheet("background-color: rgb(184, 231, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.graphic_view)
        #self.pushButton_10.setGeometry(QtCore.QRect(260, 510, 101, 41))
        self.pushButton_10.setGeometry(QtCore.QRect(710, 160, 131, 41));
        self.pushButton_10.setStyleSheet("background-color: rgb(184, 231, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.graphic_view)
        #self.pushButton_11.setGeometry(QtCore.QRect(450, 510, 81, 41))
        self.pushButton_11.setGeometry(QtCore.QRect(710, 220, 131, 41));
        self.pushButton_11.setStyleSheet("background-color: rgb(184, 231, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget_2.addTab(self.graphic_view, "")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)  #start the program on the first tab
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def select_file(self):

            filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '*.csv')

            self.fileName.setText(str(filename[0]))
            print(filename)
            return filename

    button_number=0;
    def displayResults(self, button_number):

            filename=self.fileName.toPlainText()

            self.button_number=button_number
            print(self.button_number)
            if button_number==4:
                    QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 2)
                    from Svm import Svm_predict

                    self.plainTextEdit.insertPlainText(Svm_predict.forecast)

                    pic=QtGui.QPixmap("Svm_plot.png")
                    self.label_8.setPixmap(pic)
            elif button_number==1:
                    QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 2)
                    from RNN_LSTM import Rnn_predict

                    ###############################
                    obj = Rnn_predict()

                    train_set, test_set = obj.preprocess(filename)
                    x_train, y_train, x_test, y_test = obj.cross_validation(train_set, test_set)
                    # obj.testModel()
                    model = obj.trainModel()
                    true_values_inversed = obj.testModel(model)[1]
                    predictions_inversed = obj.testModel(model)[0]

                    output = obj.testModel(model)[2]
                    # print(predictions)
                    obj.plotAndSave(true_values_inversed, predictions_inversed)

                    ##############################
                    self.plainTextEdit.clear()  # first clear whatever we find
                    self.plainTextEdit.insertPlainText(output)

                    pic = QtGui.QPixmap("RNN_Lstm_plot.png")
                    self.label_8.setPixmap(pic)
                    pic = pic.scaled(1000, 441, QtCore.Qt.KeepAspectRatio)
                    self.label_8.setPixmap(pic)

                    # 10, 60, 821, 441
                    self.label_8.setGeometry(120, 57, 821, 441)
                    print("rnn")
                    return button_number
            elif button_number==2:
                    QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 2)

                    ##################################################
                    from Encoder_Decoder_LSTM import EncoderDecoder_predict

                    obj = EncoderDecoder_predict()

                    trainset, testset = obj.preprocess(filename)
                    # obj.testModel()

                    X, y, X_test, y_test = obj.cross_validation(trainset, testset)
                    model = obj.trainModel()
                    true_values_inversed = obj.testModel(model)[1]
                    predictions_inversed = obj.testModel(model)[0]

                    output = obj.testModel(model)[2]
                    # print(predictions)
                    obj.plotAndSave(true_values_inversed, predictions_inversed)
                    ##################################################
                    self.plainTextEdit.clear()  # first clear whatever we find
                    self.plainTextEdit.insertPlainText(output)

                    pic = QtGui.QPixmap("Encoder-decoder_plot.png")
                    pic = pic.scaled(1000, 441, QtCore.Qt.KeepAspectRatio)
                    self.label_8.setPixmap(pic)

                    #10, 60, 821, 441
                    self.label_8.setGeometry(120,57,821, 441)
                    print("Encoder-decoder")
            else:
                    QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 2)
                    from Cnn_Model import Cnn_predict

                    ##############################################

                    obj = Cnn_predict()
                    # obj.testModel()

                    trainset, testset = obj.preprocess(filename)
                    # obj.testModel()

                    X, y, X_test, y_test = obj.cross_validation(trainset, testset)

                    model = obj.trainModel()
                    true_values_inversed = obj.testModel(model)[1]
                    predictions_inversed = obj.testModel(model)[0]

                    output = obj.testModel(model)[2]
                    # print(predictions)
                    obj.plotAndSave(true_values_inversed, predictions_inversed)

                    #############################################
                    self.plainTextEdit.clear()# first clear whatever we find
                    self.plainTextEdit.insertPlainText(output)
                    pic = QtGui.QPixmap("Cnn_plot.png")

                    #pic.
                    #pic = pic.scaled(1000, 1000, QtCore.Qt.KeepAspectRatio)
                    pic = pic.scaled(1500, 451, QtCore.Qt.KeepAspectRatio)
                    self.label_8.setPixmap(pic)

                    #10, 60, 821, 441
                    self.label_8.setGeometry(120,57,850, 441)

                    #self.label_8.resize(pic.width(), pic.height())
                    #self.label_8.resize(int(pic.width(), pic.height()))

                    print("Cnn")
                    return button_number,1

    def rerun(self, button_number):
        self.displayResults(button_number)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'Calibri Light\'; font-size:16pt; font-weight:24; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\">This Application ueses deep learning models to  Predict stock prices given a  correct datasets.</span></p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\">The dataset my be in a csv format.</span></p>\n"
# "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\"><br /></p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\">The models used are :RNN_LSTM,Encoder-Decoder_LSTM, CNN and  SVM</span></p></body></html>"))
        #self.pushButton_12.setText(_translate("MainWindow", "Start The App"))
        #self.label_6.setText(_translate("MainWindow", "Hyacinthe Ebula"))
       # self.label_7.setText(_translate("MainWindow", "Stock Price Prediction"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Main"))
        self.label_2.setText(_translate("MainWindow", "Stock price prediction"))
        self.label_3.setText(_translate("MainWindow", "Choose a Dataset"))
        self.choose_file.setText(_translate("MainWindow", "chose file"))
        self.toolButton.setText(_translate("MainWindow", "Next"))
        ####################################
        self.toolButton.clicked.connect(lambda: QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home"))
        self.groupBox.setTitle(_translate("MainWindow", "SELECT A MODEL"))
        self.pushButton.setText(_translate("MainWindow", "RNN(with LSTM)"))
        ###################################

        self.pushButton.clicked.connect(
                lambda: self.displayResults(1))  # the button number is given to know which model to use

        self.pushButton_2.setText(_translate("MainWindow", "CNN"))
        ###################################
        self.pushButton_2.clicked.connect(
                lambda: self.displayResults(3))  # the button number is given to know which model to use
        self.pushButton_3.setText(_translate("MainWindow", "Encoder-Decoder LSTM"))
        ###################################
        self.pushButton_3.clicked.connect(
                lambda: self.displayResults(2))  # the button number is given to know which model to use

        #self.pushButton_4.setText(_translate("MainWindow", "SVM"))
        ##########################################################
        #self.pushButton_4.clicked.connect(lambda: self.displayResults(4))# the button number is given to know which model to use
        self.label.setText(_translate("MainWindow", "Stock Price Prediction"))
        #self.pushButton_5.setText(_translate("MainWindow", "BACK"))
        ##########################################################
        #self.pushButton_5.clicked.connect(lambda: QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget,1))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Select Model"))
        self.label_4.setText(_translate("MainWindow", "Selected Model Predictions"))
        self.pushButton_6.setText(_translate("MainWindow", "Choose Algorithm"))
        #########################################
        self.pushButton_6.clicked.connect(lambda: QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 1))
        self.pushButton_7.setText(_translate("MainWindow", "Re- Run"))


        self.pushButton_7.clicked.connect(
                lambda: self.rerun(self.button_number))
        self.pushButton_8.setText(_translate("MainWindow", "EXIT"))
        ##################################################
        self.pushButton_8.clicked.connect(lambda: sys.exit())
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Normal view"))
        self.label_5.setText(_translate("MainWindow", "Graphic view"))
        self.pushButton_9.setText(_translate("MainWindow", "Choose algorithm"))
        #################################################
        self.pushButton_9.clicked.connect(lambda: QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 1))
        self.pushButton_10.setText(_translate("MainWindow", "Re-Run"))
        self.pushButton_10.clicked.connect(
                lambda: self.rerun(self.button_number))
        self.pushButton_11.setText(_translate("MainWindow", "EXIT"))
        #############################################
        self.pushButton_11.clicked.connect(lambda: sys.exit())
        #self.pushButton_12.clicked.connect(lambda:QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.graphic_view), _translate("MainWindow", "Graphic view"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Prediction Results"))


        ##########################################SVM###############
        #svm_predObj= Svm_predict()

        #self.pushButton_4.click.connect()

if __name__ == "__main__":
    import sys

   # from RNN_LSTM import Rnn_predict
   # from Cnn_Model import Cnn_predict
    #from Encoder_Decoder_LSTM import EncoderDecoder_predict

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

