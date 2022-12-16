from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class WorkTypeField(QComboBox):
    def __init__(self):
        super().__init__()

        self.displayable_values = ['Government Job', 'Never worked', 'Private', 'Self-employed', 'Children']
        self.returnable_values = ['govt_job', 'never', 'private', 'self-employed', 'children']

        self.addItems(self.displayable_values)

    def currentReturnValue(self):
        return self.returnable_values[self.currentIndex()]
