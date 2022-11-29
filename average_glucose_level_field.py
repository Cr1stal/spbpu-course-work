from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QDoubleSpinBox

class AverageGlucoseLevelField(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.label = QLabel('Average Glucose Level')
        self.layout.addWidget(self.label)

        self.field = QDoubleSpinBox()
        self.field.setRange(0, 500)
        self.field.setSingleStep(0.01)
        self.layout.addWidget(self.field)

        self.setLayout(self.layout)
