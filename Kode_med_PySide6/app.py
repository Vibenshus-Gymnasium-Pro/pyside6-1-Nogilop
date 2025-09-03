import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget

def reelle_loesninger_til_andengradsligning(a, b, c, d):
    if d < 0:
        return "Der er ingen reelle løsninger"
    elif d == 0:
        x = -b / (2*a)
        return f"Denne ligning har kun en løsning: {x}"
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return f"Denne ligning har to løsninger: {x1} og {x2}"

class HovedVindue(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Andengradsligningsløser")
        self.opsaetning()

    def opsaetning(self):
        layout = QVBoxLayout()

        # Tre felter til a, b, c
        self.lineedit_a = QLineEdit()
        self.lineedit_a.setPlaceholderText("Indtast a")
        self.lineedit_b = QLineEdit()
        self.lineedit_b.setPlaceholderText("Indtast b")
        self.lineedit_c = QLineEdit()
        self.lineedit_c.setPlaceholderText("Indtast c")

        # Knap til beregning
        self.beregn_knap = QPushButton("Beregn")
        self.beregn_knap.clicked.connect(self.beregn)

        # Label til resultatet
        self.result_label = QLabel("Resultatet vises her")

        # Tilføj alle widgets til layout
        layout.addWidget(self.lineedit_a)
        layout.addWidget(self.lineedit_b)
        layout.addWidget(self.lineedit_c)
        layout.addWidget(self.beregn_knap)
        layout.addWidget(self.result_label)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def beregn(self):
        try:
            # Hent værdier fra felterne og konverter til float
            a = float(self.lineedit_a.text())
            b = float(self.lineedit_b.text())
            c = float(self.lineedit_c.text())
            d = b**2 - 4*a*c

            # Beregn løsninger
            resultat = reelle_loesninger_til_andengradsligning(a, b, c, d)
            self.result_label.setText(resultat)

        except ValueError:
            self.result_label.setText("Ugyldig indtastning! Indtast tal.")

# Start appen
app = QApplication(sys.argv)
vindue = HovedVindue()
vindue.show()
sys.exit(app.exec())