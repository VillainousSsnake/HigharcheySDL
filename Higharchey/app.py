# Higharchey/app.py
# Contains App class

# Importing Modules
from Higharchey.config import Config


# App class
class App:
    def __init__(self):
        self.returnStatement = "main"
        self.romfs_location = Config.get_setting("romfs_location")
        self.settings = {
            "buttons_pop": Config.get_setting("buttons_pop"),
            "buttons_highlight": Config.get_setting("buttons_highlight"),
            "verbose_output": Config.get_setting("verbose_output"),
            "current_theme": Config.get_setting("current_theme"),
        }
        match self.settings["current_theme"]:

            case "Purple":
                self.theme_colors = ["#8b41bf", "#ba75eb", "#131642", "#ba75eb", "#8b41bf"]

            case "Dark":
                self.theme_colors = ["#464A52", "#575757", "#171717", "#757575", "#464A52"]

            case "Light":
                self.theme_colors = ["#E6E6F2", "#D3D3DB", "#FBFBFB", "#D3D3DB", "#E6E6F2"]
