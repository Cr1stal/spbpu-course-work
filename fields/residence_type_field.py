from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class ResidenceTypeField(QComboBox):
    def __init__(self):
        super().__init__()

        self.displayable_values = ['Urban', 'Rural']
        self.returnable_values = ['urban', 'rural']

        self.addItems(self.displayable_values)

    def currentReturnValue(self):
        return self.returnable_values[self.currentIndex()]
