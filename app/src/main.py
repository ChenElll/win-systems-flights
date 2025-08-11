import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer
from services.api_client import get_health

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('FlySmart by AirIsrael')

    # Branding
    welcome = QLabel('Welcome to FlySmart by AirIsrael')
    assistant = QLabel('Assistant: Wingman AI')
    status_label = QLabel('Checking API')

    # Layout
    layout = QVBoxLayout()
    layout.addWidget(welcome)
    layout.addWidget(assistant)
    layout.addWidget(status_label)
    window.setLayout(layout)
    window.show()

    # Update API status after the window is loaded
    def update_status():
        status_label.setText(get_health())

    QTimer.singleShot(100, update_status)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
