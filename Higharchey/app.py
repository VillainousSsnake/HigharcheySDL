# Higharchey/app.py
# Contains App class

# Importing Modules
from App.Higharchey.config import Config


# App class
class App:
    def __init__(self):
        self.returnStatement = "main"
        self.settings = {
            "current_theme": Config.get_setting("current_theme"),
            "romfs_location": Config.get_setting("romfs_location")
        }
        match self.settings["current_theme"]:

            case "Purple":
                self.theme_colors = ["#8b41bf", "#ba75eb", "#131642", "#ba75eb", "#8b41bf"]

            case "Dark":
                self.theme_colors = ["#464A52", "#575757", "#171717", "#757575", "#464A52"]

            case "Light":
                self.theme_colors = ["#E6E6F2", "#D3D3DB", "#FBFBFB", "#D3D3DB", "#E6E6F2"]
