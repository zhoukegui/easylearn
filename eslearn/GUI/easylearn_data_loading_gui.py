# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\My_Codes\easylearn-fmri\eslearn\gui_test\easylearn_data_loading_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1093, 845)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_group_modality = QtWidgets.QVBoxLayout()
        self.verticalLayout_group_modality.setObjectName("verticalLayout_group_modality")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_group = QtWidgets.QVBoxLayout()
        self.verticalLayout_group.setObjectName("verticalLayout_group")
        self.label_group = QtWidgets.QLabel(self.centralwidget)
        self.label_group.setObjectName("label_group")
        self.verticalLayout_group.addWidget(self.label_group)
        self.listView_groups = QtWidgets.QListView(self.centralwidget)
        self.listView_groups.setMinimumSize(QtCore.QSize(20, 10))
        self.listView_groups.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView_groups.setObjectName("listView_groups")
        self.verticalLayout_group.addWidget(self.listView_groups)
        self.group_btn = QtWidgets.QHBoxLayout()
        self.group_btn.setObjectName("group_btn")
        self.pushButton_addgroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addgroups.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_addgroups.setToolTipDuration(-5)
        self.pushButton_addgroups.setObjectName("pushButton_addgroups")
        self.group_btn.addWidget(self.pushButton_addgroups)
        self.pushButton_removegroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removegroups.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_removegroups.setObjectName("pushButton_removegroups")
        self.group_btn.addWidget(self.pushButton_removegroups)
        self.pushButton_cleargroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cleargroups.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_cleargroups.setObjectName("pushButton_cleargroups")
        self.group_btn.addWidget(self.pushButton_cleargroups)
        self.verticalLayout_group.addLayout(self.group_btn)
        self.gridLayout_2.addLayout(self.verticalLayout_group, 3, 1, 1, 1)
        self.verticalLayout_group_modality.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_group_modality.addItem(spacerItem)
        self.verticalLayout_modality = QtWidgets.QVBoxLayout()
        self.verticalLayout_modality.setObjectName("verticalLayout_modality")
        self.label_modalities = QtWidgets.QLabel(self.centralwidget)
        self.label_modalities.setObjectName("label_modalities")
        self.verticalLayout_modality.addWidget(self.label_modalities)
        self.listView_modalities = QtWidgets.QListView(self.centralwidget)
        self.listView_modalities.setMinimumSize(QtCore.QSize(20, 10))
        self.listView_modalities.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView_modalities.setObjectName("listView_modalities")
        self.verticalLayout_modality.addWidget(self.listView_modalities)
        self.modality_btn = QtWidgets.QHBoxLayout()
        self.modality_btn.setObjectName("modality_btn")
        self.pushButton_addmodalities = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addmodalities.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_addmodalities.setToolTipDuration(-5)
        self.pushButton_addmodalities.setObjectName("pushButton_addmodalities")
        self.modality_btn.addWidget(self.pushButton_addmodalities)
        self.pushButton_removemodalites = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removemodalites.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_removemodalites.setObjectName("pushButton_removemodalites")
        self.modality_btn.addWidget(self.pushButton_removemodalites)
        self.pushButton_clearmodalities = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearmodalities.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearmodalities.setObjectName("pushButton_clearmodalities")
        self.modality_btn.addWidget(self.pushButton_clearmodalities)
        self.verticalLayout_modality.addLayout(self.modality_btn)
        self.verticalLayout_group_modality.addLayout(self.verticalLayout_modality)
        self.horizontalLayout_2.addLayout(self.verticalLayout_group_modality)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_files = QtWidgets.QVBoxLayout()
        self.verticalLayout_files.setObjectName("verticalLayout_files")
        self.verticalLayout_file = QtWidgets.QVBoxLayout()
        self.verticalLayout_file.setObjectName("verticalLayout_file")
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setObjectName("label_file")
        self.verticalLayout_file.addWidget(self.label_file)
        self.listView_files = QtWidgets.QListView(self.centralwidget)
        self.listView_files.setMinimumSize(QtCore.QSize(10, 200))
        self.listView_files.setBaseSize(QtCore.QSize(10, 10))
        self.listView_files.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView_files.setObjectName("listView_files")
        self.verticalLayout_file.addWidget(self.listView_files)
        self.file_btn = QtWidgets.QHBoxLayout()
        self.file_btn.setObjectName("file_btn")
        self.pushButton_addfiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addfiles.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_addfiles.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_addfiles.setToolTipDuration(-5)
        self.pushButton_addfiles.setObjectName("pushButton_addfiles")
        self.file_btn.addWidget(self.pushButton_addfiles)
        self.pushButton_removefiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removefiles.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_removefiles.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_removefiles.setObjectName("pushButton_removefiles")
        self.file_btn.addWidget(self.pushButton_removefiles)
        self.pushButton_clearfiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearfiles.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearfiles.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_clearfiles.setObjectName("pushButton_clearfiles")
        self.file_btn.addWidget(self.pushButton_clearfiles)
        self.verticalLayout_file.addLayout(self.file_btn)
        self.verticalLayout_files.addLayout(self.verticalLayout_file)
        self.horizontalLayout_2.addLayout(self.verticalLayout_files)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_mask = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mask.setMinimumSize(QtCore.QSize(30, 40))
        self.lineEdit_mask.setObjectName("lineEdit_mask")
        self.gridLayout_3.addWidget(self.lineEdit_mask, 1, 0, 1, 1)
        self.label_mask = QtWidgets.QLabel(self.centralwidget)
        self.label_mask.setObjectName("label_mask")
        self.gridLayout_3.addWidget(self.label_mask, 0, 0, 1, 1)
        self.file_btn_2 = QtWidgets.QHBoxLayout()
        self.file_btn_2.setObjectName("file_btn_2")
        self.pushButton_selectMask = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectMask.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_selectMask.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_selectMask.setToolTipDuration(-5)
        self.pushButton_selectMask.setObjectName("pushButton_selectMask")
        self.file_btn_2.addWidget(self.pushButton_selectMask)
        self.pushButton_clearMask = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearMask.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearMask.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_clearMask.setObjectName("pushButton_clearMask")
        self.file_btn_2.addWidget(self.pushButton_clearMask)
        self.gridLayout_3.addLayout(self.file_btn_2, 2, 0, 1, 1)
        self.pushButton_mask = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mask.setStyleSheet("gridline-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));")
        self.pushButton_mask.setObjectName("pushButton_mask")
        self.gridLayout_3.addWidget(self.pushButton_mask, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_target = QtWidgets.QLabel(self.centralwidget)
        self.label_target.setObjectName("label_target")
        self.gridLayout_4.addWidget(self.label_target, 0, 0, 1, 1)
        self.file_btn_3 = QtWidgets.QHBoxLayout()
        self.file_btn_3.setObjectName("file_btn_3")
        self.pushButton_selectTarget = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectTarget.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_selectTarget.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_selectTarget.setToolTipDuration(-5)
        self.pushButton_selectTarget.setObjectName("pushButton_selectTarget")
        self.file_btn_3.addWidget(self.pushButton_selectTarget)
        self.pushButton_clearTarget = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearTarget.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearTarget.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_clearTarget.setObjectName("pushButton_clearTarget")
        self.file_btn_3.addWidget(self.pushButton_clearTarget)
        self.gridLayout_4.addLayout(self.file_btn_3, 3, 0, 1, 1)
        self.lineEdit_target = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_target.setMinimumSize(QtCore.QSize(30, 40))
        self.lineEdit_target.setObjectName("lineEdit_target")
        self.gridLayout_4.addWidget(self.lineEdit_target, 2, 0, 1, 1)
        self.pushButton_target = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_target.setObjectName("pushButton_target")
        self.gridLayout_4.addWidget(self.pushButton_target, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_covariance = QtWidgets.QLabel(self.centralwidget)
        self.label_covariance.setObjectName("label_covariance")
        self.gridLayout_5.addWidget(self.label_covariance, 0, 0, 1, 1)
        self.file_btn_4 = QtWidgets.QHBoxLayout()
        self.file_btn_4.setObjectName("file_btn_4")
        self.pushButton_selectCovariance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectCovariance.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_selectCovariance.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_selectCovariance.setToolTipDuration(-5)
        self.pushButton_selectCovariance.setObjectName("pushButton_selectCovariance")
        self.file_btn_4.addWidget(self.pushButton_selectCovariance)
        self.pushButton_clearCovriance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearCovriance.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearCovriance.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_clearCovriance.setObjectName("pushButton_clearCovriance")
        self.file_btn_4.addWidget(self.pushButton_clearCovriance)
        self.gridLayout_5.addLayout(self.file_btn_4, 3, 0, 1, 1)
        self.lineEdit_covariates = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_covariates.setMinimumSize(QtCore.QSize(30, 40))
        self.lineEdit_covariates.setObjectName("lineEdit_covariates")
        self.gridLayout_5.addWidget(self.lineEdit_covariates, 2, 0, 1, 1)
        self.pushButton_covariate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_covariate.setObjectName("pushButton_covariate")
        self.gridLayout_5.addWidget(self.pushButton_covariate, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 26))
        self.menubar.setObjectName("menubar")
        self.menuConfiguration_file = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration_file.setObjectName("menuConfiguration_file")
        self.menuHelp_H = QtWidgets.QMenu(self.menubar)
        self.menuHelp_H.setObjectName("menuHelp_H")
        self.menuSkin = QtWidgets.QMenu(self.menubar)
        self.menuSkin.setObjectName("menuSkin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChoose_configuration_file = QtWidgets.QAction(MainWindow)
        self.actionChoose_configuration_file.setObjectName("actionChoose_configuration_file")
        self.actionSave_configuration = QtWidgets.QAction(MainWindow)
        self.actionSave_configuration.setObjectName("actionSave_configuration")
        self.actionWeb = QtWidgets.QAction(MainWindow)
        self.actionWeb.setObjectName("actionWeb")
        self.actionPDF = QtWidgets.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionBlack = QtWidgets.QAction(MainWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actionDarkOrange = QtWidgets.QAction(MainWindow)
        self.actionDarkOrange.setObjectName("actionDarkOrange")
        self.actionGray = QtWidgets.QAction(MainWindow)
        self.actionGray.setObjectName("actionGray")
        self.actionBlue = QtWidgets.QAction(MainWindow)
        self.actionBlue.setObjectName("actionBlue")
        self.actionNavy = QtWidgets.QAction(MainWindow)
        self.actionNavy.setObjectName("actionNavy")
        self.actionClassic = QtWidgets.QAction(MainWindow)
        self.actionClassic.setObjectName("actionClassic")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.menuConfiguration_file.addAction(self.actionChoose_configuration_file)
        self.menuConfiguration_file.addAction(self.actionSave_configuration)
        self.menuHelp_H.addAction(self.actionWeb)
        self.menuHelp_H.addAction(self.actionPDF)
        self.menuSkin.addAction(self.actionDark)
        self.menuSkin.addAction(self.actionBlack)
        self.menuSkin.addAction(self.actionDarkOrange)
        self.menuSkin.addAction(self.actionGray)
        self.menuSkin.addAction(self.actionBlue)
        self.menuSkin.addAction(self.actionNavy)
        self.menuSkin.addAction(self.actionClassic)
        self.menuSkin.addAction(self.actionLight)
        self.menubar.addAction(self.menuConfiguration_file.menuAction())
        self.menubar.addAction(self.menuHelp_H.menuAction())
        self.menubar.addAction(self.menuSkin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_group.setText(_translate("MainWindow", "Groups"))
        self.pushButton_addgroups.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_addgroups.setText(_translate("MainWindow", "Add"))
        self.pushButton_removegroups.setText(_translate("MainWindow", "Remove"))
        self.pushButton_cleargroups.setText(_translate("MainWindow", "Clear"))
        self.label_modalities.setText(_translate("MainWindow", "Modalities"))
        self.pushButton_addmodalities.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_addmodalities.setText(_translate("MainWindow", "Add"))
        self.pushButton_removemodalites.setText(_translate("MainWindow", "Remove"))
        self.pushButton_clearmodalities.setText(_translate("MainWindow", "Clear"))
        self.label_file.setText(_translate("MainWindow", "Files"))
        self.pushButton_addfiles.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_addfiles.setText(_translate("MainWindow", "Add"))
        self.pushButton_removefiles.setText(_translate("MainWindow", "Remove"))
        self.pushButton_clearfiles.setText(_translate("MainWindow", "Clear"))
        self.label_mask.setText(_translate("MainWindow", "Mask"))
        self.pushButton_selectMask.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_selectMask.setText(_translate("MainWindow", "Select mask"))
        self.pushButton_clearMask.setText(_translate("MainWindow", "Clear mask"))
        self.pushButton_mask.setText(_translate("MainWindow", "OK"))
        self.label_target.setText(_translate("MainWindow", "Targets"))
        self.pushButton_selectTarget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_selectTarget.setText(_translate("MainWindow", "Select targets"))
        self.pushButton_clearTarget.setText(_translate("MainWindow", "Clear targets"))
        self.pushButton_target.setText(_translate("MainWindow", "Ok"))
        self.label_covariance.setText(_translate("MainWindow", "Covariates"))
        self.pushButton_selectCovariance.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_selectCovariance.setText(_translate("MainWindow", "Select covariates"))
        self.pushButton_clearCovriance.setText(_translate("MainWindow", "Clear covariates"))
        self.pushButton_covariate.setText(_translate("MainWindow", "Ok"))
        self.menuConfiguration_file.setTitle(_translate("MainWindow", "Configuration file(&F)"))
        self.menuHelp_H.setTitle(_translate("MainWindow", "Help(&H)"))
        self.menuSkin.setTitle(_translate("MainWindow", "Skin"))
        self.actionChoose_configuration_file.setText(_translate("MainWindow", "Load configuration"))
        self.actionSave_configuration.setText(_translate("MainWindow", "Save configuration"))
        self.actionWeb.setText(_translate("MainWindow", "Web"))
        self.actionPDF.setText(_translate("MainWindow", "PDF"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionDarkOrange.setText(_translate("MainWindow", "DarkOrange"))
        self.actionGray.setText(_translate("MainWindow", "Gray"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionNavy.setText(_translate("MainWindow", "Navy"))
        self.actionClassic.setText(_translate("MainWindow", "Classic"))
        self.actionLight.setText(_translate("MainWindow", "Light"))

