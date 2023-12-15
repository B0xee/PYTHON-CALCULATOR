import sys
#? sys lets us termination through exit()

from PyQt6.QtWidgets import (
    QApplication, 
    QLabel, 
    QWidget, 
    QPushButton, 
    QFormLayout, 
    QLineEdit
    
)
#! Include the widgets you want in the import

#^ init app
myApp = QApplication([])


#^init GUI
window = QWidget()                      # passing a class through to window
window.setWindowTitle("My App")         # method for title
helloMsg = QLabel("<h1>Hewwo World!<h1>", parent = window) # widget to display in HTML

#? Lets make a button
button = QPushButton("My Button", parent = window)

#? Now lets format it a bit
'''
Dialogue windows (compared to Main Windows) are stand-alones for short interactions with users
'''
layout = QFormLayout()
layout.addRow(helloMsg) # There's like a massive gap under here and I don't know why haha
layout.addRow("Name: ", QLineEdit())
layout.addRow("Age: ", QLineEdit())
layout.addRow("Gender: ", QLineEdit())
layout.addRow("Teeth: ", QLineEdit())
layout.addRow(button)
window.setLayout(layout) # rmb to set this layout to the window object

'''
can use a widget as a top level window if it doesn't have a parent/isnt a main window
parent (main window) -> children(elements and shit)
'''
#! All QWidgets should have a parent unless they're a top window

#^ show GUI

window.show()
'''
exec method is wrapped in exit for clean exit and release resources upon termination
'''
sys.exit(myApp.exec())
