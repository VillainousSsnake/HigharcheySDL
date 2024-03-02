# App/main.py
# Holds main program code

# DISCLAIMER: When creating an app, move */App/main.py to */main.py

# Importing modules
from App.AppLib.app import App
from App.AppLib.index import Index

# Creating App variable
app = App()

# Mainloop
while app.returnStatement != "exit":

    # Menu System
    match app.returnStatement:

        case "main":  # Main Menu
            Index.main_menu(app)
