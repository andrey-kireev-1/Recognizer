import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QComboBox
import recognize
from gui import Ui_Dialog

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_Dialog() #GUI object
        self.ui.setupUi(self)
        self.path = [] 
        self.acc = 0.45 #object recognition accuracy
        combo_acc = self.ui.accurancy
        i = 0
        while i < 1.05:
            combo_acc.addItem(str(float("{0:.2f}".format(i))))
            i += 0.05
        combo_acc.setCurrentText(str(0.45))
        self.ui.browse.clicked.connect(self.browsefiles)
        self.ui.btn_recog.clicked.connect(self.recog)
        self.ui.accurancy.currentTextChanged.connect(self.changeAccurancy)

    def changeAccurancy(self):
        self.acc = self.ui.accurancy.currentText()
        print(self.acc)


    def browsefiles(self): #select input-file   
        self.path = QFileDialog.getOpenFileName(self, 'Open file', dir="С:\\", filter='Images&Videos (*.jpg *.png *.avi *.mp4)')
        self.ui.filename.setText(self.path[0])
        
    def recog(self): #starting recognition
        video_formats = ['avi', 'mp4']
        image_formats = ['jpg', 'png']
        format = ''
        if self.path != []:
            format = self.path[0][-3::]
            print(f"{self.path[0][:-4]}_out.{format}")
        else:
            print("error_path")
        if format in video_formats: #video recognition
            recognize.recognize(vid_path=f"{self.path[0]}",vid_out=f"{self.path[0][:-4]}_out.{format}", acc=float(self.acc))
            os.system(f"{self.path[0][:-4]}_out.{format}") 
        elif format in image_formats: #image recognition
            recognize.recognize(img_path=f"{self.path[0]}",img_out=f"{self.path[0][:-4]}_out.{format}", acc=float(self.acc))
            os.system(f"{self.path[0][:-4]}_out.{format}")
        else:
            print("error_file")
        

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = App()
    window.show() 
    sys.exit(app.exec())