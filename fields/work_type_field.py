from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class WorkTypeField(QComboBox):
    def __init__(self):
        super().__init__()

        self.addItems(['Private', 'Self-employed', 'Govt_job'])
