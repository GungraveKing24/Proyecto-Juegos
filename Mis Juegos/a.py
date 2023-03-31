import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import openpyxl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabla ordenada")
        self.setGeometry(100, 100, 500, 500)
        
        # Leer datos del archivo Excel
        wb = openpyxl.load_workbook("Lista de Juegos.xlsx")
        sheet = wb.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(list(row))

        # Crear tabla y agregar datos
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 400, 300)
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[0])):
                item = QTableWidgetItem(str(data[i][j]))
                self.tableWidget.setItem(i, j, item)

        # Ordenar por columna 2
        self.tableWidget.sortItems(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())