import sys
import math
#from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QDoubleSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget
    # Tilføj eller fjern selv flere widgets, hvis I vil/ikke vil bruge dem. F.eks. forskellige layouts
)


"""def reelle_loesninger_til_andengradsligning(a, b, c, d):
    Denne funktion modtager a, b og c-koefficienterne til en andengradsligning sat op på standardform som argumenter og returnerer de reelle løsninger.
    if d < 0:
            print("Der er ingen reelle løsninger")
    elif d == 0: 
        x = ((-b+math.sqrt(d))/(2*a))
        print(f"Denne ligning har kun en løsning: {x}")
    else:
        x1 = ((-b+math.sqrt(d))/(2*a))
        x2 = ((-b-math.sqrt(d))/(2*a))
        print(f"Denne ligning har to løsninger: {x1} og {x2}")
    # Overvej hvad funktionen skal returnere, naar der er hhv 0, 1 eller 2 loesninger
    # Skal funktionen returnere faktiske vaerdier, eller bare en tekststreng?
    pass
"""

class HovedVindue(QMainWindow):
    def __init__(self):
        super().__init__()
        self.opsaetning()

    def opsaetning(self):
        self.setWindowTitle("Andengradsligningsløser")
        #layout = QVBoxLayout()
        """widgets = [
            QApplication,
            QMainWindow,
            QLabel,
            QPushButton,
            QLineEdit,
            QDoubleSpinBox,
            QVBoxLayout,
            QHBoxLayout,
            QGridLayout,
        ]
        for widget in widgets:
            layout.addWidget(widget)
          
        central_widget = QWidget()
        central_widget.setLayout(layout)
        
        self.setCentralWidget(central_widget)
        """
        self.lineedit = QLineEdit()
        self.lineedit_a = QLineEdit()
        self.lineedit_b = QLineEdit()
        self.lineedit_c = QLineEdit()
        beregn_knap = QPushButton("Beregn")
        beregn_knap.setCheckable(True)
        beregn_knap.clicked.connect(self.beregn)
        self.lineedit.setMaxLength(10)
        self.lineedit.setPlaceholderText("Indtast værdier for a, b og c her et af gangen")
        self.setCentralWidget(self.lineedit)
        # Herunder skal oprette de noedvendige widgets
        # og soerge for at saette dem op i et ordentligt layout.
        # Herunder skal I saette jeres signaler og slots op
        # Hvis man har en knap, som hedder self.beregn_knap kan det se nogenlunde
        # saaledes ud
        # self.beregn_knap.clicked.connect(self.beregn)

    # Herunder er det en god idé at skrive en metode(funktion), som
    # - gemmer værdierne for a, b og c
    # - sender værdierne til funktionen reelle_loesninger_til_andengradsligning
    # - modtager svaret fra reelle_loesninger_til_andengradsligning
    # - skriver svaret ud i et eller flere felter.
    # I kan jo kalde metoden for beregn
    def beregn(self):        
        a = input()
        b = input()
        c = input()
        d = b**2-4*a*c

#reelle_loesninger_til_andengradsligning(a, b, c, d)

andengradsligningsloeser = QApplication(sys.argv)
vindue = HovedVindue()
vindue.show()
andengradsligningsloeser.exec()