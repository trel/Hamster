# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 663)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonFind = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFind.setEnabled(True)
        self.pushButtonFind.setGeometry(QtCore.QRect(140, 540, 93, 28))
        self.pushButtonFind.setObjectName("pushButtonFind")
        self.listDirFiles = QtWidgets.QListWidget(self.centralwidget)
        self.listDirFiles.setGeometry(QtCore.QRect(10, 40, 261, 411))
        self.listDirFiles.setObjectName("listDirFiles")
        self.lineEdit_current_dataobject = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_current_dataobject.setGeometry(QtCore.QRect(290, 10, 221, 22))
        self.lineEdit_current_dataobject.setObjectName("lineEdit_current_dataobject")
        self.lineEdit_current_collection = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_current_collection.setGeometry(QtCore.QRect(520, 10, 341, 22))
        self.lineEdit_current_collection.setObjectName("lineEdit_current_collection")
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setGeometry(QtCore.QRect(10, 510, 221, 22))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButtonGo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGo.setEnabled(True)
        self.pushButtonGo.setGeometry(QtCore.QRect(870, 10, 41, 28))
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.lineEdit_Header = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Header.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.lineEdit_Header.setObjectName("lineEdit_Header")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(361, 80, 551, 164))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_dc_doi = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_doi.setFont(font)
        self.lineEdit_dc_doi.setObjectName("lineEdit_dc_doi")
        self.verticalLayout.addWidget(self.lineEdit_dc_doi)
        self.lineEdit_dc_title = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_title.setFont(font)
        self.lineEdit_dc_title.setObjectName("lineEdit_dc_title")
        self.verticalLayout.addWidget(self.lineEdit_dc_title)
        self.lineEdit_dc_creator = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_creator.setFont(font)
        self.lineEdit_dc_creator.setObjectName("lineEdit_dc_creator")
        self.verticalLayout.addWidget(self.lineEdit_dc_creator)
        self.lineEdit_dc_publisher = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_publisher.setFont(font)
        self.lineEdit_dc_publisher.setObjectName("lineEdit_dc_publisher")
        self.verticalLayout.addWidget(self.lineEdit_dc_publisher)
        self.lineEdit_dc_publication_year = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_publication_year.setFont(font)
        self.lineEdit_dc_publication_year.setObjectName("lineEdit_dc_publication_year")
        self.verticalLayout.addWidget(self.lineEdit_dc_publication_year)
        self.lineEdit_dc_resource_type = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_resource_type.setFont(font)
        self.lineEdit_dc_resource_type.setObjectName("lineEdit_dc_resource_type")
        self.verticalLayout.addWidget(self.lineEdit_dc_resource_type)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(291, 80, 71, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(360, 275, 551, 136))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_dc_subject = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_subject.setFont(font)
        self.lineEdit_dc_subject.setObjectName("lineEdit_dc_subject")
        self.verticalLayout_3.addWidget(self.lineEdit_dc_subject)
        self.lineEdit_dc_contributor = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_contributor.setFont(font)
        self.lineEdit_dc_contributor.setObjectName("lineEdit_dc_contributor")
        self.verticalLayout_3.addWidget(self.lineEdit_dc_contributor)
        self.lineEdit_dc_dates = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_dates.setFont(font)
        self.lineEdit_dc_dates.setObjectName("lineEdit_dc_dates")
        self.verticalLayout_3.addWidget(self.lineEdit_dc_dates)
        self.lineEdit_dc_related_ids = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_related_ids.setFont(font)
        self.lineEdit_dc_related_ids.setObjectName("lineEdit_dc_related_ids")
        self.verticalLayout_3.addWidget(self.lineEdit_dc_related_ids)
        self.lineEdit_dc_description = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_description.setFont(font)
        self.lineEdit_dc_description.setObjectName("lineEdit_dc_description")
        self.verticalLayout_3.addWidget(self.lineEdit_dc_description)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(285, 275, 71, 131))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_4.addWidget(self.label_18)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_4.addWidget(self.label_21)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_4.addWidget(self.label_25)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_4.addWidget(self.label_16)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(360, 430, 551, 192))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_dc_language = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_language.setFont(font)
        self.lineEdit_dc_language.setObjectName("lineEdit_dc_language")
        self.verticalLayout_5.addWidget(self.lineEdit_dc_language)
        self.lineEdit_dc_alternate_ids = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_alternate_ids.setFont(font)
        self.lineEdit_dc_alternate_ids.setObjectName("lineEdit_dc_alternate_ids")
        self.verticalLayout_5.addWidget(self.lineEdit_dc_alternate_ids)
        self.lineEdit_dc_sizes = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_sizes.setFont(font)
        self.lineEdit_dc_sizes.setObjectName("lineEdit_dc_sizes")
        self.verticalLayout_5.addWidget(self.lineEdit_dc_sizes)
        self.lineEdit_dc_formats = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_formats.setFont(font)
        self.lineEdit_dc_formats.setObjectName("lineEdit_dc_formats")
        self.verticalLayout_5.addWidget(self.lineEdit_dc_formats)
        self.lineEdit_dc_version = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_version.setFont(font)
        self.lineEdit_dc_version.setObjectName("lineEdit_dc_version")
        self.verticalLayout_5.addWidget(self.lineEdit_dc_version)
        self.lineEdit_dc_funding_reference = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_funding_reference.setFont(font)
        self.lineEdit_dc_funding_reference.setObjectName("lineEdit_dc_funding_reference")
        self.verticalLayout_5.addWidget(self.lineEdit_dc_funding_reference)
        self.lineEdit_dc_rights_list = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dc_rights_list.setFont(font)
        self.lineEdit_dc_rights_list.setObjectName("lineEdit_dc_rights_list")
        self.verticalLayout_5.addWidget(self.lineEdit_dc_rights_list)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(283, 429, 81, 191))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_24 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_6.addWidget(self.label_24)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_6.addWidget(self.label_23)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_6.addWidget(self.label_26)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_6.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_6.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_6.addWidget(self.label_30)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_6.addWidget(self.label_27)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(290, 50, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.lineEdit_Hamster_contact = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Hamster_contact.setGeometry(QtCore.QRect(418, 50, 491, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Hamster_contact.setFont(font)
        self.lineEdit_Hamster_contact.setObjectName("lineEdit_Hamster_contact")
        self.pushButtonFind.raise_()
        self.listDirFiles.raise_()
        self.lineEdit_current_dataobject.raise_()
        self.lineEdit_current_collection.raise_()
        self.lineEdit_search.raise_()
        self.pushButtonGo.raise_()
        self.lineEdit_Header.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.lineEdit_Hamster_contact.raise_()
        self.label_31.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionUpload_Directory = QtGui.QAction(MainWindow)
        self.actionUpload_Directory.setObjectName("actionUpload_Directory")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setEnabled(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPrefs = QtGui.QAction(MainWindow)
        self.actionPrefs.setEnabled(True)
        self.actionPrefs.setObjectName("actionPrefs")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setEnabled(True)
        self.actionHelp.setObjectName("actionHelp")
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setEnabled(True)
        self.actionUndo.setObjectName("actionUndo")
        self.actionNextFile = QtGui.QAction(MainWindow)
        self.actionNextFile.setEnabled(False)
        self.actionNextFile.setObjectName("actionNextFile")
        self.actionPrevFile = QtGui.QAction(MainWindow)
        self.actionPrevFile.setEnabled(False)
        self.actionPrevFile.setObjectName("actionPrevFile")
        self.actionCopyMetadata = QtGui.QAction(MainWindow)
        self.actionCopyMetadata.setObjectName("actionCopyMetadata")
        self.actionPasteMetadata = QtGui.QAction(MainWindow)
        self.actionPasteMetadata.setObjectName("actionPasteMetadata")
        self.actionRename = QtGui.QAction(MainWindow)
        self.actionRename.setEnabled(True)
        self.actionRename.setObjectName("actionRename")
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionUpload_File = QtGui.QAction(MainWindow)
        self.actionUpload_File.setObjectName("actionUpload_File")
        self.actionDownload = QtGui.QAction(MainWindow)
        self.actionDownload.setObjectName("actionDownload")
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionProperties_Object = QtGui.QAction(MainWindow)
        self.actionProperties_Object.setObjectName("actionProperties_Object")
        self.actioniRODS_system_info = QtGui.QAction(MainWindow)
        self.actioniRODS_system_info.setObjectName("actioniRODS_system_info")
        self.actionGo_Home = QtGui.QAction(MainWindow)
        self.actionGo_Home.setObjectName("actionGo_Home")
        self.menuFile.addAction(self.actionUpload_File)
        self.menuFile.addAction(self.actionUpload_Directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDownload)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actioniRODS_system_info)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionProperties_Object)
        self.menuEdit.addAction(self.actionRename)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopyMetadata)
        self.menuEdit.addAction(self.actionPasteMetadata)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionGo_Home)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPrefs)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_Hamster_contact, self.lineEdit_dc_doi)
        MainWindow.setTabOrder(self.lineEdit_dc_doi, self.lineEdit_dc_title)
        MainWindow.setTabOrder(self.lineEdit_dc_title, self.lineEdit_dc_creator)
        MainWindow.setTabOrder(self.lineEdit_dc_creator, self.lineEdit_dc_publisher)
        MainWindow.setTabOrder(self.lineEdit_dc_publisher, self.lineEdit_dc_publication_year)
        MainWindow.setTabOrder(self.lineEdit_dc_publication_year, self.lineEdit_dc_resource_type)
        MainWindow.setTabOrder(self.lineEdit_dc_resource_type, self.lineEdit_dc_subject)
        MainWindow.setTabOrder(self.lineEdit_dc_subject, self.lineEdit_dc_contributor)
        MainWindow.setTabOrder(self.lineEdit_dc_contributor, self.lineEdit_dc_dates)
        MainWindow.setTabOrder(self.lineEdit_dc_dates, self.lineEdit_dc_related_ids)
        MainWindow.setTabOrder(self.lineEdit_dc_related_ids, self.lineEdit_dc_description)
        MainWindow.setTabOrder(self.lineEdit_dc_description, self.lineEdit_dc_language)
        MainWindow.setTabOrder(self.lineEdit_dc_language, self.lineEdit_dc_alternate_ids)
        MainWindow.setTabOrder(self.lineEdit_dc_alternate_ids, self.lineEdit_dc_sizes)
        MainWindow.setTabOrder(self.lineEdit_dc_sizes, self.lineEdit_dc_formats)
        MainWindow.setTabOrder(self.lineEdit_dc_formats, self.lineEdit_dc_version)
        MainWindow.setTabOrder(self.lineEdit_dc_version, self.lineEdit_dc_funding_reference)
        MainWindow.setTabOrder(self.lineEdit_dc_funding_reference, self.lineEdit_dc_rights_list)
        MainWindow.setTabOrder(self.lineEdit_dc_rights_list, self.lineEdit_Header)
        MainWindow.setTabOrder(self.lineEdit_Header, self.lineEdit_current_dataobject)
        MainWindow.setTabOrder(self.lineEdit_current_dataobject, self.lineEdit_current_collection)
        MainWindow.setTabOrder(self.lineEdit_current_collection, self.pushButtonGo)
        MainWindow.setTabOrder(self.pushButtonGo, self.listDirFiles)
        MainWindow.setTabOrder(self.listDirFiles, self.lineEdit_search)
        MainWindow.setTabOrder(self.lineEdit_search, self.pushButtonFind)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hamster"))
        self.pushButtonFind.setText(_translate("MainWindow", "Find   Ctrl+F"))
        self.listDirFiles.setSortingEnabled(False)
        self.pushButtonGo.setText(_translate("MainWindow", "&Go"))
        self.label_22.setText(_translate("MainWindow", "DOI"))
        self.label_13.setText(_translate("MainWindow", "Title"))
        self.label_14.setText(_translate("MainWindow", "Creator"))
        self.label_17.setText(_translate("MainWindow", "Publisher"))
        self.label_19.setText(_translate("MainWindow", "Publ. year"))
        self.label_20.setText(_translate("MainWindow", "Rsrc. type"))
        self.label_15.setText(_translate("MainWindow", "Subject"))
        self.label_18.setText(_translate("MainWindow", "Contributor"))
        self.label_21.setText(_translate("MainWindow", "Date(s)"))
        self.label_25.setText(_translate("MainWindow", "Related ID"))
        self.label_16.setText(_translate("MainWindow", "Description"))
        self.label_24.setText(_translate("MainWindow", "Language"))
        self.label_23.setText(_translate("MainWindow", "Alt. ID"))
        self.label_26.setText(_translate("MainWindow", "Size(s)"))
        self.label_28.setText(_translate("MainWindow", "Format(s)"))
        self.label_29.setText(_translate("MainWindow", "Version"))
        self.label_30.setText(_translate("MainWindow", "Funding Ref."))
        self.label_27.setText(_translate("MainWindow", "Rights List"))
        self.label_31.setText(_translate("MainWindow", "Contact Information"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.actionNew.setText(_translate("MainWindow", "&New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionUpload_Directory.setText(_translate("MainWindow", "Upl&oad Directory..."))
        self.actionUpload_Directory.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionPrefs.setText(_translate("MainWindow", "Pr&eferences..."))
        self.actionHelp.setText(_translate("MainWindow", "&Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionUndo.setText(_translate("MainWindow", "&Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionNextFile.setText(_translate("MainWindow", "Next File"))
        self.actionNextFile.setShortcut(_translate("MainWindow", "Ctrl+PgDown"))
        self.actionPrevFile.setText(_translate("MainWindow", "Previous File"))
        self.actionPrevFile.setShortcut(_translate("MainWindow", "Ctrl+PgUp"))
        self.actionCopyMetadata.setText(_translate("MainWindow", "&Copy Metadata"))
        self.actionCopyMetadata.setShortcut(_translate("MainWindow", "F5"))
        self.actionPasteMetadata.setText(_translate("MainWindow", "&Paste Metadata"))
        self.actionPasteMetadata.setShortcut(_translate("MainWindow", "F6"))
        self.actionRename.setText(_translate("MainWindow", "&Rename"))
        self.actionRename.setShortcut(_translate("MainWindow", "F2"))
        self.actionFind.setText(_translate("MainWindow", "&Find"))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionUpload_File.setText(_translate("MainWindow", "Upload &File..."))
        self.actionDownload.setText(_translate("MainWindow", "&Download..."))
        self.actionDownload.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionDelete.setText(_translate("MainWindow", "&Delete..."))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del"))
        self.actionProperties_Object.setText(_translate("MainWindow", "Pr&operties"))
        self.actionProperties_Object.setShortcut(_translate("MainWindow", "Alt+Return"))
        self.actioniRODS_system_info.setText(_translate("MainWindow", "&iRODS system info"))
        self.actionGo_Home.setText(_translate("MainWindow", "Go &Home"))
