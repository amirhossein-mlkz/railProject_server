from uiUtils import GUIComponents

class commonUI:

    def __init__(self):
        pass

    def show_confirmbox(self, title:str, text:str, buttons:list[str]):
        confirmbox = GUIComponents.confirmMessageBox(title, text, buttons)
        return confirmbox.render()