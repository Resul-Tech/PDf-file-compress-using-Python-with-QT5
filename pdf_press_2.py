


# Created by: Resul Demirci
# contact me :https://www.linkedin.com/in/resul-demirci-a23870127/




from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox
import pypdfium2 as pdfium
import time
import sys

class Ui_Pdf_compress(object):
    def setupUi(self, Pdf_compress):
        Pdf_compress.setObjectName("Pdf_compress")
        Pdf_compress.resize(353, 242)
        Pdf_compress.setMinimumSize(QtCore.QSize(353, 242))
        Pdf_compress.setMaximumSize(QtCore.QSize(353, 242))
        self.Upload = QtWidgets.QPushButton(Pdf_compress)
        self.Upload.setGeometry(QtCore.QRect(210, 40, 112, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Upload.setFont(font)
        self.Upload.setAutoFillBackground(False)
        self.Upload.setStyleSheet("background-color: rgb(255, 253, 222);")
        self.Upload.setAutoDefault(True)
        self.Upload.setDefault(False)
        self.Upload.setFlat(False)
        self.Upload.setObjectName("Upload")
        self.pbar = QtWidgets.QProgressBar(Pdf_compress)
        self.lineEdit = QtWidgets.QLineEdit(Pdf_compress)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Pdf_compress)
        self.comboBox.setGeometry(QtCore.QRect(20, 110, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("\n"
"")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.compress_button = QtWidgets.QPushButton(Pdf_compress)
        self.compress_button.setGeometry(QtCore.QRect(210, 110, 112, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.compress_button.setFont(font)
        self.compress_button.setAutoFillBackground(False)
        self.compress_button.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.compress_button.setAutoDefault(True)
        self.compress_button.setObjectName("compress_button")
        self.label = QtWidgets.QLabel(Pdf_compress)
        self.label.setGeometry(QtCore.QRect(20, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Pdf_compress)
        self.label_2.setGeometry(QtCore.QRect(250, 220, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Pdf_compress)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 220, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Pdf_compress)
        QtCore.QMetaObject.connectSlotsByName(Pdf_compress)
   
        

    def retranslateUi(self, Pdf_compress):
        _translate = QtCore.QCoreApplication.translate
        Pdf_compress.setWindowTitle(_translate("Pdf_compress", "PDF Compress"))
        self.Upload.setText(_translate("Pdf_compress", "Upload PDF"))
        self.comboBox.setItemText(0, _translate("Pdf_compress", "High Quailty"))
        self.comboBox.setItemText(1, _translate("Pdf_compress", "Middle Quality"))
        self.comboBox.setItemText(2, _translate("Pdf_compress", "Low Quality"))
        self.compress_button.setText(_translate("Pdf_compress", "Compress"))
        self.label.setText(_translate("Pdf_compress", "Quality Options:"))
        self.label_2.setText(_translate("Pdf_compress", "Created by Resul"))
        self.Upload.clicked.connect(self.upload_pdf)
        self.compress_button.clicked.connect(self.press_pdf)
        
    def show_info_messagebox_1(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)  
        # setting message for Message Box
        msg.setText("---  PDF is compressed  --- ")        
        # setting Message box window title
        msg.setWindowTitle("  SUCCESSFULLY  ")     
        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)
        # start the app
        retval = msg.exec_()
    def show_info_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)  
        msg.setText("---  PLease choose a pdf file  --- ")        
        msg.setWindowTitle("  WARNING  ")     
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
    def show_critical_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("!!!   PDF file could not be compressed   !!!")
        msg.setWindowTitle("!!!  ERROR  !!!")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
    def upload_pdf(self):
        fileName = QFileDialog.getOpenFileName(None ,"Open a file", "",
                                            "*pdf")
        file = fileName[0]
        self.lineEdit.setText(file)
    def press_pdf(self):
        file= self.lineEdit.text()
        if file == "":
            self.show_info_messagebox()
        
        if self.comboBox.currentText()== "High Quailty":
            size = (800,1067)
        if self.comboBox.currentText()== "Middle Quality":
            size = (720,960)
        if self.comboBox.currentText()== "Low Quality":
            size = (450,600)
        image_list=[]
        if file!= "":
            try:
                
                pdf = pdfium.PdfDocument(file)
                page = pdf.get_page(0)
                pil_image = page.render_to(
                    pdfium.BitmapConv.pil_image)
                page.close()
                # convert pdt to image
                page_indices = [i for i in range(len(pdf))]
                renderer = pdf.render_to(
                    pdfium.BitmapConv.pil_image,
                    page_indices = page_indices)
                self.pbar.setVisible(True)
                self.label_3.setText("Please wait PDF is compressing...")
                self.pbar.setGeometry(20, 180, 311, 23)
                for image, index in zip(renderer, page_indices):
                    percent = (100*index)/len(page_indices)
                    percent=round(percent,2)
                    self.pbar.setValue(percent)
                    time.sleep(0.1)
                    # resie image files
                    image = image.resize(size)
                    image.convert('RGB')
                    image_list.append(image)
                # convert image to pdf
                image_list[0].save(file.replace('.pdf','_pressed.pdf'), save_all=True, append_images=image_list[1:])
                image.close()
                pdf.close() 
                self.lineEdit.clear()
                self.label_3.clear()
                
            except:
                     self.show_critical_messagebox()
            else:
                     self.pbar.setValue(100)
                     self.show_info_messagebox_1()
                     self.pbar.setVisible(False)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pdf_compress = QtWidgets.QDialog()
    ui = Ui_Pdf_compress()
    ui.setupUi(Pdf_compress)
    Pdf_compress.show()
    sys.exit(app.exec_())
