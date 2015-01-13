class ExitWindow(QMainWindow):
    """Exit Window Layout"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exit Window")
        #actions
        self.yes_exit = QAction("
