from PySide6.QtWidgets import QLabel, QWidget, QComboBox, QHBoxLayout

class GenderField(QComboBox):
    def __init__(self):
        super().__init__()

        self.displayable_values = ['Male', 'Female']
        self.returnable_values = ['male', 'female']

        self.addItems(self.displayable_values)

    def currentReturnValue(self):
        return self.returnable_values[self.currentIndex()]
