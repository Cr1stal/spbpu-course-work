from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QCheckBox

from fields.gender_field import GenderField
from fields.age_field import AgeField
from fields.hypertension_field import HypertensionField
from fields.heart_disease_field import HeartDiseaseField
from fields.ever_married_field import EverMarriedField
from fields.work_type_field import WorkTypeField
from fields.residence_type_field import ResidenceTypeField
from fields.average_glucose_level_field import AverageGlucoseLevelField
from fields.body_mass_index_field import BodyMassIndexField
from fields.smoking_status_field import SmokingStatusField

from client import Client

from grpc._channel import _InactiveRpcError

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        form = QFormLayout()

        # Gender field
        self.gender = GenderField()
        form.addRow(QLabel('Gender'), self.gender)

        # Age field
        self.age = AgeField()
        form.addRow(QLabel('Age'), self.age)

        # Hypertension field
        self.hypertension = HypertensionField()
        form.addRow(QLabel('Hypertension'), self.hypertension)

        # Heart Disease field
        self.heart_disease = HeartDiseaseField()
        form.addRow(QLabel('Heart Disease'), self.heart_disease)

        # Ever married field
        self.ever_married = EverMarriedField()
        form.addRow(QLabel('Ever married'), self.ever_married)

        # Work Type field
        self.work_type = WorkTypeField()
        form.addRow(QLabel('Work Type'), self.work_type)

        # Residence Type field
        self.residence_type = ResidenceTypeField()
        form.addRow(QLabel('Residence Type'), self.residence_type)

        # Average Glucose Level field
        self.average_glucose_level = AverageGlucoseLevelField()
        form.addRow(QLabel('Average Glucose Level'), self.average_glucose_level)

        # Body Mass Index field
        self.body_mass_index = BodyMassIndexField()
        form.addRow(QLabel('Body Mass Index'), self.body_mass_index)

        # Smoking Status field
        self.smoking_status = SmokingStatusField()
        form.addRow(QLabel('Smoking Status'), self.smoking_status)

        # Submit button
        submit_btn = QPushButton('Predict')
        submit_btn.clicked.connect(self.submit_button_clicked)
        form.addWidget(submit_btn)

        self.setMinimumSize(QSize(400, 400))
        self.setWindowTitle('Stroke prediction app')

        widget = QWidget()
        widget.setLayout(form)
        self.setCentralWidget(widget)

    def submit_button_clicked(self):
        gender_value = self.gender.currentReturnValue()
        age_value = int(self.age.value())
        hypertension_value = self.hypertension.isChecked()
        heart_disease_value = self.heart_disease.isChecked()
        ever_married_value = self.ever_married.currentReturnValue()
        work_type_value = self.work_type.currentReturnValue()
        residence_type_value = self.residence_type.currentReturnValue()
        average_glucose_level_value = int(self.average_glucose_level.value() * 100)
        body_mass_index_value = int(self.body_mass_index.value() * 100)
        smoking_status_value = self.smoking_status.currentReturnValue()

        client = Client()
        try:
          response = client.run(
                gender_arg=gender_value,
                age_arg=age_value,
                hypertension_arg=hypertension_value,
                heart_disease_arg=heart_disease_value,
                ever_married_arg=ever_married_value,
                work_type_arg=work_type_value,
                residence_type_arg=residence_type_value,
                average_glucose_level_arg=average_glucose_level_value,
                body_mass_index_arg=body_mass_index_value,
                smoking_status_arg=smoking_status_value
                )

          dlg = QMessageBox(self)
          dlg.setWindowTitle('Result of work')

          if response.result == 1:
            dlg.setIcon(QMessageBox.Warning)
            dlg.setText('You have a high probability of stroke. You need to see a doctor ASAP')
          else:
            dlg.setIcon(QMessageBox.Information)
            dlg.setText('You have a low probability of stroke. Do some regular check-ups and everything will be fine')

          dlg.setStandardButtons(QMessageBox.Close)

          dlg.exec()
        except _InactiveRpcError:
          dlg = QMessageBox(self)
          dlg.setWindowTitle('Error is happened')
          dlg.setText('Server is unavailable')
          dlg.setIcon(QMessageBox.Critical)
          dlg.setStandardButtons(QMessageBox.Close)
          dlg.exec()
