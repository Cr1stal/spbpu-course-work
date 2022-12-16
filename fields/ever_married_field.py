from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class EverMarriedField(QComboBox):
    def __init__(self):
        super().__init__()

        self.displayable_values = ['Yes', 'No']
        self.returnable_values = ['yes', 'no']

        self.addItems(self.displayable_values)

    def currentReturnValue(self):
        return self.returnable_values[self.currentIndex()]
