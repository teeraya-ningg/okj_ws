from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont


Home_ui = "src/ui/Main.ui"
CustomSaladStep_1_ui = "src/ui/customSaladStepWindow1.ui"
Payment_ui = "src/ui/paymentScreen.ui"

class homeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi( Home_ui , self)  # Load the first page UI file
        self.customSaladButton.clicked.connect(self.go_to_customSaladStep1)  # Connect button click to go to the second page
        
    def go_to_customSaladStep1(self):
        self.customSaladStep1 = customSaladStep1Screen()
        self.close()
        self.customSaladStep1.show()


class customSaladStep1Screen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi( CustomSaladStep_1_ui, self)  # Load the second page UI file
        self.homeButton.clicked.connect(self.go_to_homeScreen)  # Connect button click to go back to the first page
       
    def go_to_homeScreen(self):
        self.home = homeScreen()
        self.close()
        self.home.show()


if __name__ == '__main__':
    app = QApplication([])
    window = homeScreen()
    window.show()
    app.exec_()
    
    
