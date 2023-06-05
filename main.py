import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QWidget
from PyQt5.QtCore import pyqtSlot

from QRpayment import generateQR
Main_UI_FILE = "src/ui/Main.ui"
CustomSaladStep_1_UI_FILE = "src/ui/customSaladStepWindow1.ui"
Payment_UI_FILE = "src/ui/paymentScreen.ui"

class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen,self).__init__()
        self.ui = loadUi(Main_UI_FILE,self)
    
        #goto next page
        self.customSaladButton.clicked.connect(self.gotoCustomSaladStep1)
    
    def gotoNextScreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        screen2 = PaymentScreen()
        widget.setCurrentIndex(Widget.currentIndex()+1) 
    
    def gotoCustomSaladStep1(self):
        customSaladStep1Screen = customSaladStep1Screen()
        self.close()
        customSaladStep1Screen.widget.show()
        print('button click')
        
class PaymentScreen(QDialog):
    def __init__(self):
        super(PaymentScreen,self).__init__()
        self.ui = loadUi(Payment_UI_FILE,self)
        self.Finish_Button.clicked.connect(self.on_click)
        
   
        
    def on_click(self):
        print('button click')
        
class customSaladStep1Screen(QWidget):
    def __init__(self):
        super(customSaladStep1Screen,self).__init__()
        self.ui = loadUi( CustomSaladStep_1_UI_FILE, self )


    # def go_to_first_widget(self):
    #     first_widget = FirstWidget()
    #     self.close()
    #     first_widget.show()
#main
if __name__== '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    Main_window = MainScreen()
    Payment_window = PaymentScreen()
    CustomSaladStep1_window = customSaladStep1Screen()
    widget.addWidget(Main_window)
    widget.addWidget(Payment_window)
    widget.addWidget(CustomSaladStep1_window)
    widget.setFixedHeight(834)
    widget.setFixedWidth(1121)
    widget.show()
    



    try:
        sys.exit(app.exec())
    except:
        print("Exiting")