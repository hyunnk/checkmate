# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yolo_learn_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_YoloLearnWindow(object):
    def setupUi(self, YoloLearnWindow):
        YoloLearnWindow.setObjectName("YoloLearnWindow")
        YoloLearnWindow.resize(658, 244)
        YoloLearnWindow.setStyleSheet("#YoloLearnWindow{\n"
"    font: 9pt \"맑은 고딕\";\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(YoloLearnWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setStyleSheet("border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    border: 4px solid#a6aaaf;\n"
"    border-radius: 5px;\n"
"    padding: 1px 5px;\n"
"    background-color: #a6aaaf;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    border: 4px solid#a6aaaf;\n"
"    border-radius: 5px;\n"
"    padding: 1px 5px;\n"
"    background-color: #a6aaaf;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    border: 4px solid#a6aaaf;\n"
"    border-radius: 5px;\n"
"    padding: 1px 5px;\n"
"    background-color: #a6aaaf;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 298, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        YoloLearnWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(YoloLearnWindow)
        QtCore.QMetaObject.connectSlotsByName(YoloLearnWindow)

        # 찾아보기 버튼 연결 + 불러오기 버튼 연결
        self.pushButton.clicked.connect(self.open_file_dialog)
        self.pushButton_2.clicked.connect(self.open_directory_dialog)

    def retranslateUi(self, YoloLearnWindow):
        _translate = QtCore.QCoreApplication.translate
        YoloLearnWindow.setWindowTitle(_translate("YoloLearnWindow", "MainWindow"))
        self.pushButton.setText(_translate("YoloLearnWindow", "찾아보기"))
        self.pushButton_2.setText(_translate("YoloLearnWindow", "불러오기"))
        self.label_2.setText(_translate("YoloLearnWindow", "학습 파일 이름"))
        self.label_3.setText(_translate("YoloLearnWindow", "저장할 디렉토리 선택"))
        self.label.setText(_translate("YoloLearnWindow", "data.yaml 파일 선택"))
        self.pushButton_3.setText(_translate("YoloLearnWindow", "학습 시작"))

    # 파일 열기 함수
    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select data.yaml file", "", "YAML Files (*.yaml);;All Files (*)", options=options)
        if file_path:
                self.lineEdit.setText(file_path)   

    # 디렉토리 열기 함수
    def open_directory_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        directory_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory", "", options=options)
        if directory_path:
            self.lineEdit_3.setText(directory_path)  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YoloLearnWindow = QtWidgets.QMainWindow()
    ui = Ui_YoloLearnWindow()
    ui.setupUi(YoloLearnWindow)
    YoloLearnWindow.show()
    sys.exit(app.exec_())