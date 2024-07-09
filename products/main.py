from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QPushButton, QLineEdit, QTableView, QMessageBox, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

# SQLAlchemy setup
Base = declarative_base()

class Material(Base):
    __tablename__ = 'Product'
    code = Column(String, primary_key=True)
    produit = Column(String)
    min = Column(Float)
    cible = Column(Float)
    max = Column(Float)

engine = create_engine('sqlite:///products.db',echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the UI
        uic.loadUi('main.ui', self)
        
        # Find widgets
        self.tab_widget = self.findChild(QTabWidget, 'tabWidget')
        self.nouveau_button = self.findChild(QPushButton, 'nouveauButton')
        self.modifier_button = self.findChild(QPushButton, 'modifierButton')
        self.supprimer_button = self.findChild(QPushButton, 'supprimerButton')

        self.fermer_button = self.findChild(QPushButton, 'fermerButton')
        self.fermer_button_2 = self.findChild(QPushButton, 'fermerButton_2')
        self.fermer_button_3 = self.findChild(QPushButton, 'fermerButton_3')
        self.fermer_button_4 = self.findChild(QPushButton, 'fermerButton_4')

        self.live_search_input = self.findChild(QLineEdit, 'live_search_bar')

        
        # Inputs for ajouter tab
        self.code_input = self.findChild(QLineEdit, 'codeInput')
        self.produit_input = self.findChild(QLineEdit, 'produitInput')
        self.min_input = self.findChild(QLineEdit, 'minInput')
        self.cible_input = self.findChild(QLineEdit, 'cibleInput')
        self.max_input = self.findChild(QLineEdit, 'maxInput')
        self.add_product_button = self.findChild(QPushButton, 'addProductButton')
        
        # Inputs for modifier tab
        self.search_code_input = self.findChild(QLineEdit, 'searchCodeInput')
        self.search_button = self.findChild(QPushButton, 'searchButton')
        self.modify_code_input = self.findChild(QLineEdit, 'modifyCodeInput')
        self.modify_produit_input = self.findChild(QLineEdit, 'modifyProduitInput')
        self.modify_min_input = self.findChild(QLineEdit, 'modifyMinInput')
        self.modify_cible_input = self.findChild(QLineEdit, 'modifyCibleInput')
        self.modify_max_input = self.findChild(QLineEdit, 'modifyMaxInput')
        self.save_modifications_button = self.findChild(QPushButton, 'saveModificationsButton')
        


        #input for deleting tab
        self.search_code_input_delete = self.findChild(QLineEdit, 'searchCodeInput_delete')
        self.search_button_delete = self.findChild(QPushButton, 'searchButton_delete')
        self.delete_code_input = self.findChild(QLineEdit, 'deleteCodeInput')
        self.delete_produit_input = self.findChild(QLineEdit, 'deleteProduitInput')
        self.delete_min_input = self.findChild(QLineEdit, 'deleteMinInput')
        self.delete_cible_input = self.findChild(QLineEdit, 'deleteCibleInput')
        self.delete_max_input = self.findChild(QLineEdit, 'deleteMaxInput')
        self.delete_button = self.findChild(QPushButton, 'deleteButton')


        # Table view for product list in liste tab
        self.product_table_view = self.findChild(QTableView, 'productTableView')
        self.product_model = QStandardItemModel()
        self.product_model.setHorizontalHeaderLabels(['Code', 'Produit', 'Min', 'Cible', 'Max'])
        self.product_table_view.setModel(self.product_model)

        # Connect buttons to slots
        self.nouveau_button.clicked.connect(lambda: self.tab_widget.setCurrentIndex(1))
        self.modifier_button.clicked.connect(lambda: self.tab_widget.setCurrentIndex(2))
        self.supprimer_button.clicked.connect(lambda: self.tab_widget.setCurrentIndex(3))
        self.add_product_button.clicked.connect(self.add_product)
        self.search_button.clicked.connect(self.search_product)
        self.search_button_delete.clicked.connect(self.search_product_delete)
        self.save_modifications_button.clicked.connect(self.save_modifications)
        self.delete_button.clicked.connect(self.delete_product)
        self.fermer_button.clicked.connect(self.close)
        self.fermer_button_2.clicked.connect(self.close)
        self.fermer_button_3.clicked.connect(self.close)
        self.fermer_button_4.clicked.connect(self.close)

        # Initial update of product list
        self.update_product_list()

        self.live_search_input.textChanged.connect(self.live_search)

    def add_product(self):
        code = self.code_input.text()
        produit = self.produit_input.text()
        min_value = self.min_input.text()
        cible = self.cible_input.text()
        max_value = self.max_input.text()
        if code and produit and min_value and cible and max_value:
            new_product = Material(code=code, produit=produit, min=float(min_value), cible=float(cible), max=float(max_value))
            session.add(new_product)
            session.commit()
            self.code_input.clear()
            self.produit_input.clear()
            self.min_input.clear()
            self.cible_input.clear()
            self.max_input.clear()
            self.update_product_list()
            QMessageBox.information(self, 'Success', 'Product added successfully.')
        else:
            QMessageBox.warning(self, 'Input Error', 'Please fill in all fields.')

    def search_product(self):
        code = self.search_code_input.text()
        product = session.query(Material).filter_by(code=code).first()
        if product:
            self.modify_code_input.setText(product.code)
            self.modify_produit_input.setText(product.produit)
            self.modify_min_input.setText(str(product.min))
            self.modify_cible_input.setText(str(product.cible))
            self.modify_max_input.setText(str(product.max))
            QMessageBox.information(self, 'Product Found', 'Product found. You can modify the details below.')
        else:
            self.modify_code_input.clear()
            self.modify_produit_input.clear()
            self.modify_min_input.clear()
            self.modify_cible_input.clear()
            self.modify_max_input.clear()
            QMessageBox.warning(self, 'Search Error', 'Product not found.')
    

    def search_product_delete(self):
        code = self.search_code_input_delete.text()
        product = session.query(Material).filter_by(code=code).first()
        if product:
            self.delete_code_input.setText(product.code)
            self.delete_produit_input.setText(product.produit)
            self.delete_min_input.setText(str(product.min))
            self.delete_cible_input.setText(str(product.cible))
            self.delete_max_input.setText(str(product.max))
            QMessageBox.information(self, 'Product Found', 'Product found. You can delete the details below.')
        else:
            self.delete_code_input.clear()
            self.delete_produit_input.clear()
            self.delete_min_input.clear()
            self.delete_cible_input.clear()
            self.delete_max_input.clear()
            QMessageBox.warning(self, 'Search Error', 'Product not found.')

    
    def save_modifications(self):
        current_code = self.search_code_input.text()  # The code used to search the product
        new_code = self.modify_code_input.text()
        produit = self.modify_produit_input.text()
        min_value = self.modify_min_input.text()
        cible = self.modify_cible_input.text()
        max_value = self.modify_max_input.text()

        product = session.query(Material).filter_by(code=current_code).first()

        if product:
            if current_code != new_code:
                existing_product = session.query(Material).filter_by(code=new_code).first()
                if existing_product:
                    QMessageBox.warning(self, 'Update Error', 'Product with the new code already exists.')
                    return
                
            # Update product details
            product.code = new_code
            product.produit = produit
            product.min = float(min_value)
            product.cible = float(cible)
            product.max = float(max_value)
            
            session.commit()
            self.update_product_list()
            QMessageBox.information(self, 'Success', 'Product updated successfully.')
        else:
            QMessageBox.warning(self, 'Update Error', 'Product not found.')
    def delete_product(self):
        code = self.delete_code_input.text()
        product = session.query(Material).filter_by(code=code).first()
        if product:
            confirm_dialog = QMessageBox.question(self, 'Confirm Deletion', f"Do you want to delete product with code {code}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm_dialog == QMessageBox.StandardButton.Yes:
                session.delete(product)
                session.commit()
                self.delete_code_input.clear()
                self.delete_produit_input.clear()
                self.delete_min_input.clear()
                self.delete_cible_input.clear()
                self.delete_max_input.clear()
                self.update_product_list()
                QMessageBox.information(self, 'Success', 'Product deleted successfully.')
        else:
            QMessageBox.warning(self, 'Delete Error', 'Product not found.')

    def update_product_list(self, search_term=None):
        self.product_model.removeRows(0, self.product_model.rowCount())
        if search_term:
            products = session.query(Material).filter(Material.code.like(f'%{search_term}%')).all()
        else:
            products = session.query(Material).all()
        for product in products:
            code_item = QStandardItem(product.code)
            produit_item = QStandardItem(product.produit)
            min_item = QStandardItem(str(product.min))
            cible_item = QStandardItem(str(product.cible))
            max_item = QStandardItem(str(product.max))
            self.product_model.appendRow([code_item, produit_item, min_item, cible_item, max_item])

        header = self.product_table_view.horizontalHeader()
        header.setStretchLastSection(False)  # Ensure the last section is not stretched
        table_width = self.product_table_view.width()
        column_width = table_width // self.product_model.columnCount()
        for column in range(self.product_model.columnCount()):
            header.resizeSection(column, column_width)
    
    def live_search(self, search_text):
        self.update_product_list(search_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
