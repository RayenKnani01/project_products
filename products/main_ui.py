# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1980, 1080)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 41, 255);")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei UI"])
        font.setPointSize(22)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"\n"
"background-color: rgb(200,200, 200);")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 80, 1771, 891))
        self.tabWidget.setStyleSheet(u"/* Fond du QTabWidget */\n"
"QTabWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 144, 255, 255), stop:1 rgba(0, 70, 128, 255));\n"
"}\n"
"\n"
"/* Style des onglets */\n"
"QTabBar::tab {\n"
"    background-color: #dddddd; /* Bleu primaire du th\u00e8me de sport nautique */\n"
"    color: #000000; /* Texte blanc */\n"
"    border: 2px solid #000000; /* Bordure bleu fonc\u00e9 */\n"
"    padding: 12px 20px; /* Espacement interne - ajustez selon vos besoins */\n"
"    text-align: center; /* Centrer le texte */\n"
"}\n"
"\n"
"/* Style des onglets lorsqu'ils sont survol\u00e9s */\n"
"QTabBar::tab:hover {\n"
"    background-color: #ffffff; /* Bleu plus fonc\u00e9 au survol */\n"
"}\n"
"\n"
"/* Style des onglets actifs */\n"
"QTabBar::tab:selected {\n"
"    background-color: #aaaaaa; /* Fond blanc pour l'onglet actif */\n"
"    color: #000000; /* Texte bleu primaire pour l'onglet actif */\n"
"    border-bottom: 2px solid #000000; /* Bordure bleu primaire en bas de l'ong"
                        "let actif */\n"
"}\n"
"\n"
"/* Style du contenu des onglets */\n"
"QTabWidget::pane {\n"
"    border: 2px solid #000000; /* Bordure bleu fonc\u00e9 pour le contenu des onglets */\n"
"    border-top: 0; /* Supprimer la bordure sup\u00e9rieure */\n"
"}\n"
"\n"
"/* Style des boutons de fermeture des onglets */\n"
"QTabBar::close-button {\n"
"    image: url(close.png); /* Remplacez par le chemin de votre ic\u00f4ne de fermeture */\n"
"    subcontrol-position: right; /* Position \u00e0 droite du texte de l'onglet */\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"    image: url(close-hover.png); /* Ic\u00f4ne de fermeture au survol */\n"
"}\n"
"\n"
"/* Ajustement de la police */\n"
"QTabBar {\n"
"    font-size: 16px; /* Taille de la police pour les onglets */\n"
"    qproperty-drawBase: 0; /* D\u00e9sactiver le dessin de la base (fond) de l'onglet */\n"
"}\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 90, 1121, 51))
        self.lineEdit_3.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4 = QLineEdit(self.tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(1180, 90, 541, 51))
        self.lineEdit_4.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 20, 1471, 51))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(22)
        font1.setBold(False)
        font1.setItalic(False)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"font: 75 22pt \"Nirmala UI\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setReadOnly(True)
        self.nouveauButton = QPushButton(self.tab)
        self.nouveauButton.setObjectName(u"nouveauButton")
        self.nouveauButton.setGeometry(QRect(1190, 100, 161, 31))
        self.nouveauButton.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: #5bb450;\n"
"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(1520, 20, 201, 51))
        self.lineEdit_2.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_2.setReadOnly(True)
        self.supprimerButton = QPushButton(self.tab)
        self.supprimerButton.setObjectName(u"supprimerButton")
        self.supprimerButton.setGeometry(QRect(1550, 100, 161, 31))
        self.supprimerButton.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: #ff2800")
        self.fermerButton = QPushButton(self.tab)
        self.fermerButton.setObjectName(u"fermerButton")
        self.fermerButton.setGeometry(QRect(1550, 30, 141, 31))
        self.fermerButton.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: #ff2800")
        self.modifierButton = QPushButton(self.tab)
        self.modifierButton.setObjectName(u"modifierButton")
        self.modifierButton.setGeometry(QRect(1370, 100, 161, 31))
        self.modifierButton.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: #0075ff")
        self.live_search_bar = QLineEdit(self.tab)
        self.live_search_bar.setObjectName(u"live_search_bar")
        self.live_search_bar.setGeometry(QRect(40, 99, 1091, 31))
        self.live_search_bar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.productTableView = QTableView(self.tab)
        self.productTableView.setObjectName(u"productTableView")
        self.productTableView.setGeometry(QRect(30, 160, 1691, 671))
        font2 = QFont()
        font2.setPointSize(13)
        self.productTableView.setFont(font2)
        self.productTableView.setStyleSheet(u"/* style.css */\n"
"\n"
"/* Table View */\n"
"QTableView {\n"
"    border: 1px solid #2c3e50; /* Border around the table view */\n"
"    selection-background-color: #3498db; /* Background color of selected rows */\n"
"    color: #000000; /* Text color of selected rows */\n"
"\n"
"}\n"
"\n"
"/* Table Header */\n"
"QHeaderView::section {\n"
"    background-color: #2c3e50; /* Header background color */\n"
"    color: white; /* Header text color */\n"
"    padding: 4px; /* Padding around header text */\n"
"    border: 1px solid #34495e; /* Border around header */\n"
"    border-style: outset; /* Border style */\n"
"    border-radius: 3px; /* Border radius */\n"
"}\n"
"\n"
"/* Table Rows */\n"
"QTableView QScrollBar:vertical {\n"
"    border: 1px solid #ccc; /* Vertical scrollbar border */\n"
"    background: #f0f0f0; /* Vertical scrollbar background color */\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background: #95a5a6; /* Vertical scrollbar handle background color */\n"
"}\n"
"\n"
"QTableVie"
                        "w QScrollBar::add-line:vertical,\n"
"QTableView QScrollBar::sub-line:vertical {\n"
"    background: #ecf0f1; /* Vertical scrollbar line background color */\n"
"    subcontrol-position: top; /* Position of the lines */\n"
"    subcontrol-origin: margin; /* Origin of the lines */\n"
"}\n"
"")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.cibleInput = QLineEdit(self.tab_2)
        self.cibleInput.setObjectName(u"cibleInput")
        self.cibleInput.setGeometry(QRect(550, 360, 471, 51))
        font3 = QFont()
        font3.setPointSize(14)
        self.cibleInput.setFont(font3)
        self.cibleInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cibleInput.setAlignment(Qt.AlignCenter)
        self.produitInput = QLineEdit(self.tab_2)
        self.produitInput.setObjectName(u"produitInput")
        self.produitInput.setGeometry(QRect(550, 240, 471, 51))
        self.produitInput.setFont(font3)
        self.produitInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.produitInput.setAlignment(Qt.AlignCenter)
        self.minInput = QLineEdit(self.tab_2)
        self.minInput.setObjectName(u"minInput")
        self.minInput.setGeometry(QRect(550, 300, 471, 51))
        self.minInput.setFont(font3)
        self.minInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.minInput.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 370, 191, 31))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.codeInput = QLineEdit(self.tab_2)
        self.codeInput.setObjectName(u"codeInput")
        self.codeInput.setGeometry(QRect(550, 180, 471, 51))
        self.codeInput.setFont(font3)
        self.codeInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.codeInput.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 250, 131, 31))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 310, 131, 31))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 190, 131, 31))
        self.label.setStyleSheet(u"\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;\n"
"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)
        self.addProductButton = QPushButton(self.tab_2)
        self.addProductButton.setObjectName(u"addProductButton")
        self.addProductButton.setGeometry(QRect(700, 700, 171, 51))
        self.addProductButton.setStyleSheet(u"/* Style de base pour le QPushButton */\n"
"\n"
"QPushButton {\n"
"    background-color: #5bb450;\n"
"font: 75 15pt \"Nirmala UI\"; /* Bleu l\u00e9g\u00e8rement plus fonc\u00e9 que l'arri\u00e8re-plan global */\n"
"    color: #ffffff; /* Texte blanc */\n"
"    border: 5px; /* Bordure bleue */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 5px 10px; /* Espacement interne */\n"
"\n"
"}\n"
"\n"
"/* Style du QPushButton lorsqu'il est survol\u00e9 */\n"
"QPushButton:hover {\n"
"    background-color: #1b6488; /* Bleu plus fonc\u00e9 au survol */\n"
"}\n"
"\n"
"/* Style du QPushButton lorsqu'il est press\u00e9 (clic) */\n"
"QPushButton:pressed {\n"
"    background-color: #1a5c7a; /* Bleu encore plus fonc\u00e9 au clic */\n"
"}\n"
"\n"
"/* Style du QPushButton lorsqu'il est en focus (tabulation) */\n"
"QPushButton:focus {\n"
"    outline: none; /* Supprimer le contour par d\u00e9faut */\n"
"    border: 2px solid #1a5c7a; /* Bordure plus fonc\u00e9e lorsqu'en focus */\n"
"}\n"
"\n"
"/* Style du QPus"
                        "hButton lorsqu'il est d\u00e9sactiv\u00e9 */\n"
"QPushButton:disabled {\n"
"    background-color: #b0b0b0; /* Fond gris clair pour les boutons d\u00e9sactiv\u00e9s */\n"
"    color: #707070; /* Couleur du texte grise pour les boutons d\u00e9sactiv\u00e9s */\n"
"    border: 2px solid #b0b0b0; /* Bordure grise pour les boutons d\u00e9sactiv\u00e9s */\n"
"}\n"
"\n"
"/* Style g\u00e9n\u00e9ral pour les widgets lorsqu'ils sont d\u00e9sactiv\u00e9s */\n"
"QWidget:disabled {\n"
"    background-color: #f0f0f0; /* Fond gris clair pour les widgets d\u00e9sactiv\u00e9s */\n"
"    color: #a0a0a0; /* Couleur du texte grise pour les widgets d\u00e9sactiv\u00e9s */\n"
"}\n"
"")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(320, 430, 191, 31))
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.maxInput = QLineEdit(self.tab_2)
        self.maxInput.setObjectName(u"maxInput")
        self.maxInput.setGeometry(QRect(550, 420, 471, 51))
        self.maxInput.setFont(font3)
        self.maxInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.maxInput.setAlignment(Qt.AlignCenter)
        self.lineEdit_5 = QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 90, 1471, 561))
        self.lineEdit_5.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_7 = QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(30, 20, 1471, 51))
        self.lineEdit_7.setFont(font1)
        self.lineEdit_7.setStyleSheet(u"font: 75 22pt \"Nirmala UI\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_7.setReadOnly(True)
        self.fermerButton_2 = QPushButton(self.tab_2)
        self.fermerButton_2.setObjectName(u"fermerButton_2")
        self.fermerButton_2.setGeometry(QRect(1550, 30, 141, 31))
        self.fermerButton_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: #ff2800")
        self.lineEdit_8 = QLineEdit(self.tab_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(1520, 20, 201, 51))
        self.lineEdit_8.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_8.setReadOnly(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.lineEdit_5.raise_()
        self.cibleInput.raise_()
        self.produitInput.raise_()
        self.minInput.raise_()
        self.label_6.raise_()
        self.codeInput.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.addProductButton.raise_()
        self.label_7.raise_()
        self.maxInput.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_8.raise_()
        self.fermerButton_2.raise_()
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.modifyMinInput = QLineEdit(self.tab_3)
        self.modifyMinInput.setObjectName(u"modifyMinInput")
        self.modifyMinInput.setGeometry(QRect(380, 280, 471, 51))
        self.modifyMinInput.setFont(font3)
        self.modifyMinInput.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.modifyMinInput.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(150, 350, 191, 31))
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.saveModificationsButton = QPushButton(self.tab_3)
        self.saveModificationsButton.setObjectName(u"saveModificationsButton")
        self.saveModificationsButton.setGeometry(QRect(700, 700, 171, 51))
        self.saveModificationsButton.setStyleSheet(u"/* Style de base pour le QPushButton */\n"
"\n"
"QPushButton {\n"
"    background-color: #5bb450;\n"
"font: 75 15pt \"Nirmala UI\"; /* Bleu l\u00e9g\u00e8rement plus fonc\u00e9 que l'arri\u00e8re-plan global */\n"
"    color: #ffffff; /* Texte blanc */\n"
"    border: 5px; /* Bordure bleue */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 5px 10px; /* Espacement interne */\n"
"\n"
"}\n"
"\n"
"/* Style du QPushButton lorsqu'il est survol\u00e9 */\n"
"QPushButton:hover {\n"
"    background-color: #1b6488; /* Bleu plus fonc\u00e9 au survol */\n"
"}\n"
"\n"
"/* Style du QPushButton lorsqu'il est press\u00e9 (clic) */\n"
"QPushButton:pressed {\n"
"    background-color: #1a5c7a; /* Bleu encore plus fonc\u00e9 au clic */\n"
"}\n"
"\n"
"/* Style du QPushButton lorsqu'il est en focus (tabulation) */\n"
"QPushButton:focus {\n"
"    outline: none; /* Supprimer le contour par d\u00e9faut */\n"
"    border: 2px solid #1a5c7a; /* Bordure plus fonc\u00e9e lorsqu'en focus */\n"
"}\n"
"\n"
"/* Style du QPus"
                        "hButton lorsqu'il est d\u00e9sactiv\u00e9 */\n"
"QPushButton:disabled {\n"
"    background-color: #b0b0b0; /* Fond gris clair pour les boutons d\u00e9sactiv\u00e9s */\n"
"    color: #707070; /* Couleur du texte grise pour les boutons d\u00e9sactiv\u00e9s */\n"
"    border: 2px solid #b0b0b0; /* Bordure grise pour les boutons d\u00e9sactiv\u00e9s */\n"
"}\n"
"\n"
"/* Style g\u00e9n\u00e9ral pour les widgets lorsqu'ils sont d\u00e9sactiv\u00e9s */\n"
"QWidget:disabled {\n"
"    background-color: #f0f0f0; /* Fond gris clair pour les widgets d\u00e9sactiv\u00e9s */\n"
"    color: #a0a0a0; /* Couleur du texte grise pour les widgets d\u00e9sactiv\u00e9s */\n"
"}\n"
"")
        self.modifyProduitInput = QLineEdit(self.tab_3)
        self.modifyProduitInput.setObjectName(u"modifyProduitInput")
        self.modifyProduitInput.setGeometry(QRect(380, 220, 471, 51))
        self.modifyProduitInput.setFont(font3)
        self.modifyProduitInput.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.modifyProduitInput.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(150, 410, 191, 31))
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 170, 131, 31))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.modifyCibleInput = QLineEdit(self.tab_3)
        self.modifyCibleInput.setObjectName(u"modifyCibleInput")
        self.modifyCibleInput.setGeometry(QRect(380, 340, 471, 51))
        self.modifyCibleInput.setFont(font3)
        self.modifyCibleInput.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.modifyCibleInput.setAlignment(Qt.AlignCenter)
        self.modifyCodeInput = QLineEdit(self.tab_3)
        self.modifyCodeInput.setObjectName(u"modifyCodeInput")
        self.modifyCodeInput.setGeometry(QRect(380, 160, 471, 51))
        self.modifyCodeInput.setFont(font3)
        self.modifyCodeInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.modifyCodeInput.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 230, 131, 31))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 290, 131, 31))
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.modifyMaxInput = QLineEdit(self.tab_3)
        self.modifyMaxInput.setObjectName(u"modifyMaxInput")
        self.modifyMaxInput.setGeometry(QRect(380, 400, 471, 51))
        self.modifyMaxInput.setFont(font3)
        self.modifyMaxInput.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.modifyMaxInput.setAlignment(Qt.AlignCenter)
        self.lineEdit_17 = QLineEdit(self.tab_3)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(30, 20, 1471, 51))
        self.lineEdit_17.setFont(font1)
        self.lineEdit_17.setStyleSheet(u"font: 75 22pt \"Nirmala UI\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_18 = QLineEdit(self.tab_3)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(30, 90, 1191, 511))
        self.lineEdit_18.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_19 = QLineEdit(self.tab_3)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(1250, 90, 471, 511))
        self.lineEdit_19.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_23 = QLineEdit(self.tab_3)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(QRect(1520, 20, 201, 51))
        self.lineEdit_23.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_23.setReadOnly(True)
        self.fermerButton_3 = QPushButton(self.tab_3)
        self.fermerButton_3.setObjectName(u"fermerButton_3")
        self.fermerButton_3.setGeometry(QRect(1550, 30, 141, 31))
        self.fermerButton_3.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: #ff2800")
        self.label_26 = QLabel(self.tab_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(1410, 100, 141, 31))
        self.label_26.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.searchCodeInput = QLineEdit(self.tab_3)
        self.searchCodeInput.setObjectName(u"searchCodeInput")
        self.searchCodeInput.setGeometry(QRect(1340, 240, 291, 51))
        self.searchCodeInput.setFont(font3)
        self.searchCodeInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.searchCodeInput.setAlignment(Qt.AlignCenter)
        self.searchButton = QPushButton(self.tab_3)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(1420, 350, 141, 31))
        self.searchButton.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: #000000;")
        self.tabWidget.addTab(self.tab_3, "")
        self.lineEdit_18.raise_()
        self.lineEdit_17.raise_()
        self.modifyMinInput.raise_()
        self.label_8.raise_()
        self.saveModificationsButton.raise_()
        self.modifyProduitInput.raise_()
        self.label_9.raise_()
        self.label_3.raise_()
        self.modifyCibleInput.raise_()
        self.modifyCodeInput.raise_()
        self.label_5.raise_()
        self.label_10.raise_()
        self.modifyMaxInput.raise_()
        self.lineEdit_19.raise_()
        self.lineEdit_23.raise_()
        self.fermerButton_3.raise_()
        self.label_26.raise_()
        self.searchCodeInput.raise_()
        self.searchButton.raise_()
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_21 = QLabel(self.tab_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(150, 350, 191, 31))
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.deleteProduitInput = QLineEdit(self.tab_4)
        self.deleteProduitInput.setObjectName(u"deleteProduitInput")
        self.deleteProduitInput.setGeometry(QRect(380, 220, 471, 51))
        self.deleteProduitInput.setFont(font3)
        self.deleteProduitInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.deleteProduitInput.setAlignment(Qt.AlignCenter)
        self.deleteProduitInput.setReadOnly(True)
        self.deleteCibleInput = QLineEdit(self.tab_4)
        self.deleteCibleInput.setObjectName(u"deleteCibleInput")
        self.deleteCibleInput.setGeometry(QRect(380, 340, 471, 51))
        self.deleteCibleInput.setFont(font3)
        self.deleteCibleInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.deleteCibleInput.setAlignment(Qt.AlignCenter)
        self.deleteCibleInput.setReadOnly(True)
        self.label_22 = QLabel(self.tab_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(180, 170, 131, 31))
        self.label_22.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(self.tab_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(180, 290, 131, 31))
        self.label_23.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_24 = QLabel(self.tab_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(150, 410, 191, 31))
        self.label_24.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.deleteMaxInput = QLineEdit(self.tab_4)
        self.deleteMaxInput.setObjectName(u"deleteMaxInput")
        self.deleteMaxInput.setGeometry(QRect(380, 400, 471, 51))
        self.deleteMaxInput.setFont(font3)
        self.deleteMaxInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.deleteMaxInput.setAlignment(Qt.AlignCenter)
        self.deleteMaxInput.setReadOnly(True)
        self.label_25 = QLabel(self.tab_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(170, 230, 131, 31))
        self.label_25.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.deleteMinInput = QLineEdit(self.tab_4)
        self.deleteMinInput.setObjectName(u"deleteMinInput")
        self.deleteMinInput.setGeometry(QRect(380, 280, 471, 51))
        self.deleteMinInput.setFont(font3)
        self.deleteMinInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.deleteMinInput.setAlignment(Qt.AlignCenter)
        self.deleteMinInput.setReadOnly(True)
        self.deleteCodeInput = QLineEdit(self.tab_4)
        self.deleteCodeInput.setObjectName(u"deleteCodeInput")
        self.deleteCodeInput.setGeometry(QRect(380, 160, 471, 51))
        self.deleteCodeInput.setFont(font3)
        self.deleteCodeInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.deleteCodeInput.setAlignment(Qt.AlignCenter)
        self.deleteCodeInput.setReadOnly(True)
        self.lineEdit_20 = QLineEdit(self.tab_4)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(30, 20, 1471, 51))
        self.lineEdit_20.setFont(font1)
        self.lineEdit_20.setStyleSheet(u"font: 75 22pt \"Nirmala UI\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_21 = QLineEdit(self.tab_4)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(1250, 90, 471, 511))
        self.lineEdit_21.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_22 = QLineEdit(self.tab_4)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(30, 90, 1191, 511))
        self.lineEdit_22.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_24 = QLineEdit(self.tab_4)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setGeometry(QRect(1520, 20, 201, 51))
        self.lineEdit_24.setStyleSheet(u"font: 22pt \"Cascadia Code\";\n"
"border-radius: 5px;\n"
"background-color:#ececec;")
        self.lineEdit_24.setReadOnly(True)
        self.fermerButton_4 = QPushButton(self.tab_4)
        self.fermerButton_4.setObjectName(u"fermerButton_4")
        self.fermerButton_4.setGeometry(QRect(1550, 30, 141, 31))
        self.fermerButton_4.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: #ff2800")
        self.label_27 = QLabel(self.tab_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(1410, 100, 141, 31))
        self.label_27.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:#ececec;")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.searchCodeInput_delete = QLineEdit(self.tab_4)
        self.searchCodeInput_delete.setObjectName(u"searchCodeInput_delete")
        self.searchCodeInput_delete.setGeometry(QRect(1340, 240, 291, 51))
        self.searchCodeInput_delete.setFont(font3)
        self.searchCodeInput_delete.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.searchCodeInput_delete.setAlignment(Qt.AlignCenter)
        self.deleteButton = QPushButton(self.tab_4)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(700, 700, 171, 51))
        self.deleteButton.setStyleSheet(u"/* Style de base pour le QPushButton */\n"
"\n"
"QPushButton {\n"
"    background-color: #5bb450;\n"
"font: 75 15pt \"Nirmala UI\"; /* Bleu l\u00e9g\u00e8rement plus fonc\u00e9 que l'arri\u00e8re-plan global */\n"
"    color: #ffffff; /* Texte blanc */\n"
"    border: 5px; /* Bordure bleue */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 5px 10px; /* Espacement interne */\n"
"\n"
"}\n"
"\n"
"/* Style du QPushButton lorsqu'il est survol\u00e9 */\n"
"QPushButton:hover {\n"
"    background-color: #1b6488; /* Bleu plus fonc\u00e9 au survol */\n"
"}\n"
"\n"
"/* Style du QPushButton lorsqu'il est press\u00e9 (clic) */\n"
"QPushButton:pressed {\n"
"    background-color: #1a5c7a; /* Bleu encore plus fonc\u00e9 au clic */\n"
"}\n"
"\n"
"/* Style du QPushButton lorsqu'il est en focus (tabulation) */\n"
"QPushButton:focus {\n"
"    outline: none; /* Supprimer le contour par d\u00e9faut */\n"
"    border: 2px solid #1a5c7a; /* Bordure plus fonc\u00e9e lorsqu'en focus */\n"
"}\n"
"\n"
"/* Style du QPus"
                        "hButton lorsqu'il est d\u00e9sactiv\u00e9 */\n"
"QPushButton:disabled {\n"
"    background-color: #b0b0b0; /* Fond gris clair pour les boutons d\u00e9sactiv\u00e9s */\n"
"    color: #707070; /* Couleur du texte grise pour les boutons d\u00e9sactiv\u00e9s */\n"
"    border: 2px solid #b0b0b0; /* Bordure grise pour les boutons d\u00e9sactiv\u00e9s */\n"
"}\n"
"\n"
"/* Style g\u00e9n\u00e9ral pour les widgets lorsqu'ils sont d\u00e9sactiv\u00e9s */\n"
"QWidget:disabled {\n"
"    background-color: #f0f0f0; /* Fond gris clair pour les widgets d\u00e9sactiv\u00e9s */\n"
"    color: #a0a0a0; /* Couleur du texte grise pour les widgets d\u00e9sactiv\u00e9s */\n"
"}\n"
"")
        self.searchButton_delete = QPushButton(self.tab_4)
        self.searchButton_delete.setObjectName(u"searchButton_delete")
        self.searchButton_delete.setGeometry(QRect(1420, 350, 141, 31))
        self.searchButton_delete.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: #000000;")
        self.tabWidget.addTab(self.tab_4, "")
        self.lineEdit_20.raise_()
        self.lineEdit_22.raise_()
        self.lineEdit_21.raise_()
        self.label_21.raise_()
        self.deleteProduitInput.raise_()
        self.deleteCibleInput.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.deleteMaxInput.raise_()
        self.label_25.raise_()
        self.deleteMinInput.raise_()
        self.deleteCodeInput.raise_()
        self.lineEdit_24.raise_()
        self.fermerButton_4.raise_()
        self.label_27.raise_()
        self.searchCodeInput_delete.raise_()
        self.deleteButton.raise_()
        self.searchButton_delete.raise_()
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dialog", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Liste des Produits", None))
        self.nouveauButton.setText(QCoreApplication.translate("MainWindow", u"Nouveau", None))
        self.supprimerButton.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.fermerButton.setText(QCoreApplication.translate("MainWindow", u"Fermer", None))
        self.modifierButton.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.live_search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher par Code...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Liste", None))
        self.cibleInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez le cible", None))
        self.produitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez le produit", None))
        self.minInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez le min", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cible  : ", None))
        self.codeInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez le code", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Produit :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Code : ", None))
        self.addProductButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Max  : ", None))
        self.maxInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez le max", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"Ajouter un Produit", None))
        self.fermerButton_2.setText(QCoreApplication.translate("MainWindow", u"Fermer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.modifyMinInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modifier le min", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cible  : ", None))
        self.saveModificationsButton.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.modifyProduitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modifier le produit", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Max  : ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Code : ", None))
        self.modifyCibleInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modifier le cible", None))
        self.modifyCodeInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modifier le code", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Produit :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.modifyMaxInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modifier le max", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"Modifier un Produit", None))
        self.fermerButton_3.setText(QCoreApplication.translate("MainWindow", u"Fermer", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.searchCodeInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrer le code cherch\u00e9", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Chercher", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Cible  : ", None))
        self.deleteProduitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Supprimer le produit", None))
        self.deleteCibleInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Supprimer le cible", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Code : ", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Max  : ", None))
        self.deleteMaxInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Supprimer le max", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Produit :", None))
        self.deleteMinInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Supprimer le min", None))
        self.deleteCodeInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Supprimer le code", None))
        self.lineEdit_20.setText(QCoreApplication.translate("MainWindow", u"Supprimer un Produit", None))
        self.fermerButton_4.setText(QCoreApplication.translate("MainWindow", u"Fermer", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.searchCodeInput_delete.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrer le code cherch\u00e9", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.searchButton_delete.setText(QCoreApplication.translate("MainWindow", u"Chercher", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Supprimer", None))
    # retranslateUi

