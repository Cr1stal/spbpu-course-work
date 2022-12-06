from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class WorkTypeField(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.label = QLabel('Work Type')
        self.layout.addWidget(self.label)

        self.field = QComboBox()
        self.field.addItems(['Private', 'Self-employed', 'Govt_job'])
        self.layout.addWidget(self.field)

        self.setLayout(self.layout)
