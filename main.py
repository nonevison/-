import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
import webbrowser
from mudule import *
"""
    main.spec 삽입용 튜플 ui = [('main.ui', '.'), ('infotap.ui', '.')]
    main.spec 생성 pyinstaller main.py
    exe파일 생성 pyinstaller main.spec
"""


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path("main.ui")
form_class = uic.loadUiType(form)[0]

form_info = resource_path("infotap.ui")
tap_info = uic.loadUiType(form_info)[0]

#form_license = resource_path("licensetap.ui")
#tap_license = uic.loadUiType(form_license)[0]

"""
class LicenseWindow(QDialog, tap_license):
      def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.show()
"""
class InfoWindow(QDialog, tap_info):
      def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.show()
           

#show display class
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.btn_googleform.clicked.connect(self.f_btn_go_googleform) #구글 폼 바로가기 버튼
        self.btn_input.clicked.connect(self.f_btn_input) #입력 버튼
        self.btn_complain.clicked.connect(self.f_btn_complain)
        self.btn_info.clicked.connect(self.f_btn_info)
        #self.btn_license.clicked.connect(self.f_btn_license)
    """
    def f_btn_license(self):
          window = LicenseWindow()
          window.exec_()
    """

    def f_btn_complain(self):
        webbrowser.open_new_tab("https://forms.gle/b3A9dEcV79aF1cvC6")


    def f_btn_info(self):
        window = InfoWindow()
        window.exec_()
          
          
    
    def f_btn_input(self):
            self.change_label_4()
            self.change_label_5()
            self.change_label_6()

    def f_btn_go_googleform(self):
            webbrowser.open_new_tab("https://forms.gle/YuYzy7Lhoa5qu5yx9")

    def change_label_4(self):
            self.label_4.setText(str(number_of_text(self.textEdit.toPlainText())))

    def change_label_5(self):
            self.label_5.setText(str(number_of_noempty(self.textEdit.toPlainText())))

    def change_label_6(self):
            self.label_6.setText(str(count_sign(self.textEdit.toPlainText())))


if __name__ == "__main__" :
    def ExceptionHook(exctype, value, traceback):
        sys.__excepthook__(exctype, value, traceback)
        sys.exit(1)
 
    sys.excepthook = ExceptionHook

    app = QApplication(sys.argv) 
 
    myWindow = WindowClass() 
 
    myWindow.show()
 
    app.exec_()