from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle('Multiple Widgets Example')

# Create widgets
label1 = QLabel('Label 1')
label2 = QLabel('Label 2')
button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')

# Create a layout to organize the widgets
layout = QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(label2)
layout.addWidget(button1)
layout.addWidget(button2)

# Set the layout on the window
window.setLayout(layout)

window.show()

app.exec_()
