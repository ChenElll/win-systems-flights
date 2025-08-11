import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer
from services.api_client import get_health

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Flight Advisor')

    # Label for displaying the API status
    status_label = QLabel('Checking API…')
    # Welcome label
    welcome = QLabel('Welcome to the Flight Advisor')

    # Layout configuration
    layout = QVBoxLayout()
    layout.addWidget(welcome)
    layout.addWidget(status_label)
    window.setLayout(layout)
    window.show()

    # Update the API status after the window is loaded
    def update_status():
        status_label.setText(get_health())

    QTimer.singleShot(100, update_status)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
