import sys
import sqlite3
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Umbrella Reinsurance Company System Management')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QtWidgets.QLabel('Welcome to Umbrella Reinsurance Company System Management')
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Click Me')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label.setText('Button clicked!')
        self.add_data_to_database()

    def add_data_to_database(self):
        conn = sqlite3.connect('umbrella.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS policy (id INTEGER PRIMARY KEY, policy_number TEXT, policy_type TEXT, policy_holder TEXT)")
        c.execute("INSERT INTO policy VALUES (1, '123456', 'Auto', 'John Smith')")
        conn.commit()
        c.close()
        conn.close()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
