from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class SmokingStatusField(QComboBox):
    def __init__(self):
        super().__init__()

        self.displayable_values = ['Formerly Smoked', 'Never Smoked', 'Smokes']
        self.returnable_values = ['formerly_smoked', 'never_smoked', 'smokes']

        self.addItems(self.displayable_values)

    def currentReturnValue(self):
        return self.returnable_values[self.currentIndex()]
