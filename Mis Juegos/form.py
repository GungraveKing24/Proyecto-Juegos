# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerJxqYXe.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(798, 480)
        self.table = QTableWidget(Dialog)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 80, 761, 361))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 10, 113, 21))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(80, 40, 111, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 49, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 20, 81, 20))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 40, 41, 20))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(310, 10, 271, 61))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(630, 30, 75, 24))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 450, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Juegos", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Estado", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Datos adicionales", None));
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Completado", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Algun dia", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Nuevo", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Jugando", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Pendiente", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Juego", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Datos extra", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Estado", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cargar Lista", None))
    # retranslateUi

