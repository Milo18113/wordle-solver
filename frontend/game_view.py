import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame

from backend.enums import GuessMethod

class MiApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wordle Solver")
        self.setMinimumSize(450, 725)           # w x h
        self.showMaximized()

        # Spacers
        spacer = QWidget()
        spacer.setFixedSize(0, 50) 

        smallspacer = QWidget()
        smallspacer.setFixedSize(0, 20)

        # Matrix to store square references 5x5
        self.squares = [[None for _ in range(5)] for _ in range(5)]

        #### Main vertical layout (wrapper)
        main_vertical_layout = QVBoxLayout()
        main_vertical_layout.addWidget(spacer)
        
        # Main Row 1
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch()
        
        
        ### Word Attempts Column
        column_layout = QVBoxLayout()
        column_layout.setSpacing(35)
        
        for row in range(5):
            row_layout = QHBoxLayout()
            row_layout.setSpacing(5)  # spacing between squares in row
            
            # Building char squares
            for col in range(5):
                square = QFrame()
                square.setFixedSize(60, 60)
                square.setStyleSheet("background-color: red; border: 1px solid black;")
                
                self.squares[row][col] = square
                row_layout.addWidget(square)

            column_layout.addLayout(row_layout)
        
        horizontal_layout.addLayout(column_layout)
        horizontal_layout.addStretch()

        main_vertical_layout.addLayout(horizontal_layout)
        main_vertical_layout.addWidget(smallspacer)


        ### Main Row 2
        horizontal_layout_2 = QHBoxLayout()
        horizontal_layout_2.addStretch()

        info_panel = QVBoxLayout()
        horizontal_layout_2.addLayout(info_panel)
        
        ## Info & Controls Panel
        reports_label = QLabel("Reports")
        info_panel.addWidget(reports_label, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        # Buttons Layout
        buttons_layout = QHBoxLayout()

        guess_method_combo = QComboBox()
        guess_method_combo.addItems([g.value for g in GuessMethod   ])
        buttons_layout.addWidget(guess_method_combo)
        
        guess_button = QPushButton("Guess")
        reset_button = QPushButton("Reset")
        buttons_layout.addWidget(guess_button)
        buttons_layout.addWidget(reset_button)

        info_panel.addLayout(buttons_layout)
        horizontal_layout_2.addStretch()

        main_vertical_layout.addLayout(horizontal_layout_2)
        main_vertical_layout.addWidget(spacer)
        

        self.setLayout(main_vertical_layout)
        self.load_styles()


    def load_styles(self):
        base_dir = os.path.dirname(__file__)  # carpeta del .py
        ruta = os.path.join(base_dir, "styles.qss")

        with open(ruta, "r") as f:
            self.setStyleSheet(f.read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiApp()
    sys.exit(app.exec())