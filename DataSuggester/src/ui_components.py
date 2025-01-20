from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QMessageBox, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from src.logic import suggest_data_structure
from src.visualization import visualize_structure  # Ensure this line is at the top of ui_components.py


class DataStructureApp(QWidget):

    def __init__(self):
        super().__init__()
        self.is_dark_mode = False
        self.history = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Data Structure Suggestion Tool")
        self.setGeometry(300, 200, 950, 650)  # Adjusted dimensions for better spacing

        # Set a soft, modern font
        main_font = QFont("Segoe UI", 11)
        self.setFont(main_font)

        # Apply subtle drop shadows to the entire window for a modern, soft 3D effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(0, 0, 0, 120))
        self.setGraphicsEffect(shadow)

        # Apply initial light theme stylesheet for elegance and simplicity
        self.setStyleSheet("""
            QWidget {
                background-color: #F6F7FB;  /* Light, neutral background */
                color: #3E4A61;  /* Subtle dark text */
                font-size: 16px;
            }
            QPushButton {
                background-color: #6272A4;  /* Soft purple-blue */
                color: white;
                border-radius: 12px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #535D9C;  /* Slightly darker on hover */
            }
            QPushButton:pressed {
                background-color: #444D88;  /* Even darker on press */
            }
            QTextEdit {
                background-color: #FFFFFF;  /* Pure white background for clarity */
                color: #000000;  /* Set text color to black for light mode */
                border: 1px solid #D1D9E6;  /* Soft gray border */
                border-radius: 8px;
                padding: 12px;
                font-family: 'Courier New';
                font-size: 14px;
            }
            QLabel {
                color: #000000;  /* Set label color to black for light mode */
                font-weight: bold;
                font-size: 16px;
            }
        """)

        # Main layout with left and right sections
        main_layout = QHBoxLayout()

        # Left side layout for text input and control buttons
        input_layout = QVBoxLayout()
        
        # Text edit area for problem input
        self.textEdit = QTextEdit(self)
        self.textEdit.setPlaceholderText("📝 Describe your problem here (e.g., 'I need a data structure for fast sorting')...")
        input_layout.addWidget(self.textEdit)

        # Submit button
        self.submitButton = QPushButton("Submit", self)
        self.submitButton.clicked.connect(self.onSubmit)
        input_layout.addWidget(self.submitButton)

        # Clear button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.clicked.connect(self.onClear)
        input_layout.addWidget(self.clearButton)

        # Dark mode toggle button
        self.toggleButton = QPushButton("Toggle Dark/Light Mode", self)
        self.toggleButton.clicked.connect(self.toggleTheme)
        input_layout.addWidget(self.toggleButton)

        # Add the input layout to the main layout
        main_layout.addLayout(input_layout)

        # Right side layout for visualizations and history
        right_layout = QVBoxLayout()

        # Visualization area
        self.visualization_area = QLabel("Visualizations will appear here", self)
        self.visualization_area.setAlignment(Qt.AlignCenter)
        self.visualization_area.setStyleSheet("""
            border: 1px solid #D1D9E6;
            border-radius: 12px;
            padding: 20px;
            background-color: #FFFFFF;  /* Clean white background */
        """)
        right_layout.addWidget(self.visualization_area)

        # Problem history and suggestions sidebar
        self.sidebar = QTextEdit(self)
        self.sidebar.setReadOnly(True)
        self.sidebar.setPlaceholderText("Problem history and suggestions will appear here.")
        self.sidebar.setStyleSheet("""
            background-color: #F8F9FA; 
            color: #3E4A61;
            font-size: 14px; 
            border: 1px solid #D1D9E6; 
            border-radius: 12px; 
            padding: 12px;
        """)
        right_layout.addWidget(self.sidebar)

        # Add the right layout to the main layout
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

    def toggleTheme(self):
        if self.is_dark_mode:
            # Light mode
            self.setStyleSheet("""
                QWidget {
                    background-color: #F6F7FB;
                    color: #3E4A61;
                    font-size: 16px;
                }
                QPushButton {
                    background-color: #6272A4;
                    color: white;
                    border-radius: 12px;
                    padding: 10px 20px;
                    font-weight: bold;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #535D9C;
                }
                QPushButton:pressed {
                    background-color: #444D88;
                }
                QTextEdit {
                    background-color: #FFFFFF;
                    color: #000000;  /* Set text color to black for light mode */
                    border: 1px solid #D1D9E6;
                    border-radius: 8px;
                    padding: 12px;
                    font-family: 'Courier New';
                    font-size: 14px;
                }
                QLabel {
                    color: #000000;  /* Set label color to black for light mode */
                    font-weight: bold;
                    font-size: 16px;
                }
            """)
        else:
            # Dark mode
            self.setStyleSheet("""
                QWidget {
                    background-color: #2C2C2C;
                    color: #FFFFFF;
                    font-size: 16px;
                }
                QPushButton {
                    background-color: #444444;
                    color: #7DD1F2;  /* Soft cyan for dark mode buttons */
                    border-radius: 12px;
                    padding: 10px 20px;
                    font-weight: bold;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #393939;
                }
                QPushButton:pressed {
                    background-color: #333333;
                }
                QTextEdit {
                    background-color: #3E3E3E;
                    color: #FFFFFF;  /* Set text color to white for dark mode */
                    border: 1px solid #7DD1F2;
                    border-radius: 8px;
                    padding: 12px;
                    font-family: 'Courier New';
                    font-size: 14px;
                }
                QLabel {
                    color: #7DD1F2;
                    font-weight: bold;
                    font-size: 16px;
                }
            """)
        self.is_dark_mode = not self.is_dark_mode

    def onSubmit(self):
        problem_description = self.textEdit.toPlainText()
        if problem_description:
            suggestion = suggest_data_structure(problem_description)
            QMessageBox.information(self, "Suggestion", suggestion)
            self.sidebar.append(f"Problem: {problem_description}\nSuggestion: {suggestion}")
            if 'binary_tree' in suggestion:
                visualize_structure('binary_tree')
            elif 'graph' in suggestion:
                visualize_structure('graph')
            elif 'heap' in suggestion:
                visualize_structure('heap')
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a problem description.")

    def onClear(self):
        self.textEdit.clear()
        self.sidebar.clear()
        self.visualization_area.setText("📊 Visualizations will appear here")
