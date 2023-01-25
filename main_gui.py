# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import numpy as np
from os import path, remove
import json
import main 
from PyQt5 import QtCore, QtGui, QtWidgets
import parameters as pmt
from importlib import reload

from matplotlibgui import Ui_TabPlots
import matplotlib.pyplot as plt


# from mplwidget import MplWidget
####### ventana principal con el formulario
class Ui_MainWindow(object):           
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -108, 766, 990))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_param_ell2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_param_ell2.setObjectName("label_param_ell2")
        self.gridLayout_2.addWidget(self.label_param_ell2, 1, 1, 1, 1)
        self.label_param_ell1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_param_ell1.setObjectName("label_param_ell1")
        self.gridLayout_2.addWidget(self.label_param_ell1, 1, 0, 1, 1)
        self.imagen1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.imagen1.setObjectName("imagen1")
        self.gridLayout = QtWidgets.QGridLayout(self.imagen1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_imagen_1 = QtWidgets.QLabel(self.imagen1)
        self.label_imagen_1.setObjectName("label_imagen_1")
        self.gridLayout.addWidget(self.label_imagen_1, 0, 0, 1, 1)
        self.navegar_imagen_1 = QtWidgets.QPushButton(self.imagen1)
        font = QtGui.QFont()
        font.setFamily("Unifont Upper")
        self.navegar_imagen_1.setFont(font)
        self.navegar_imagen_1.setObjectName("navegar_imagen_1")
        self.gridLayout.addWidget(self.navegar_imagen_1, 0, 4, 1, 1)
        self.label_mascara = QtWidgets.QLabel(self.imagen1)
        self.label_mascara.setObjectName("label_mascara")
        self.gridLayout.addWidget(self.label_mascara, 1, 0, 1, 1)
        self.mascara_cgeck = QtWidgets.QCheckBox(self.imagen1)
        self.mascara_cgeck.setEnabled(True)
        self.mascara_cgeck.setChecked(True)
        self.mascara_cgeck.setObjectName("mascara_cgeck")
        self.gridLayout.addWidget(self.mascara_cgeck, 1, 1, 1, 1)
        self.label_mascara_archivo = QtWidgets.QLabel(self.imagen1)
        self.label_mascara_archivo.setObjectName("label_mascara_archivo")
        self.gridLayout.addWidget(self.label_mascara_archivo, 1, 2, 1, 1)
        self.line_mascara = QtWidgets.QLineEdit(self.imagen1)
        self.line_mascara.setEnabled(False)
        self.line_mascara.setProperty("ifreduc", True)
        self.line_mascara.setObjectName("line_mascara")
        self.gridLayout.addWidget(self.line_mascara, 1, 3, 1, 1)
        self.navegar_mascara = QtWidgets.QPushButton(self.imagen1)
        self.navegar_mascara.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Unifont Upper")
        self.navegar_mascara.setFont(font)
        self.navegar_mascara.setObjectName("navegar_mascara")
        self.gridLayout.addWidget(self.navegar_mascara, 1, 4, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Unifont Upper")


        self.line_imagen_1 = QtWidgets.QLineEdit(self.imagen1)
        self.line_imagen_1.setProperty("ifreduc", True)
        self.line_imagen_1.setObjectName("line_imagen_1")
        self.gridLayout.addWidget(self.line_imagen_1, 0, 1, 1, 3)
        
        self.gridLayout_2.addWidget(self.imagen1, 0, 0, 1, 2)
        self.group_param_ellip2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_param_ellip2.setEnabled(True)
        self.group_param_ellip2.setObjectName("group_param_ellip2")
        self.grid_ellip2 = QtWidgets.QGridLayout(self.group_param_ellip2)
        self.grid_ellip2.setObjectName("grid_ellip2")
        self.stepLabel_3 = QtWidgets.QLabel(self.group_param_ellip2)
        self.stepLabel_3.setEnabled(True)
        self.stepLabel_3.setObjectName("stepLabel_3")
        self.grid_ellip2.addWidget(self.stepLabel_3, 7, 0, 1, 1)
        self.converLabel_2 = QtWidgets.QLabel(self.group_param_ellip2)
        self.converLabel_2.setEnabled(True)
        self.converLabel_2.setObjectName("converLabel_2")
        self.grid_ellip2.addWidget(self.converLabel_2, 3, 0, 1, 1)
        self.minsmaLabel_2 = QtWidgets.QLabel(self.group_param_ellip2)
        self.minsmaLabel_2.setEnabled(True)
        self.minsmaLabel_2.setObjectName("minsmaLabel_2")
        self.grid_ellip2.addWidget(self.minsmaLabel_2, 5, 0, 1, 1)
        self.nclipLineEdit_2 = QtWidgets.QLineEdit(self.group_param_ellip2)
        self.nclipLineEdit_2.setEnabled(True)
        self.nclipLineEdit_2.setObjectName("nclipLineEdit_2")
        self.grid_ellip2.addWidget(self.nclipLineEdit_2, 0, 1, 1, 1)
        self.intmodeComboBox_2 = QtWidgets.QComboBox(self.group_param_ellip2)
        self.intmodeComboBox_2.setEnabled(True)
        self.intmodeComboBox_2.setObjectName("intmodeComboBox_2")
        self.grid_ellip2.addWidget(self.intmodeComboBox_2, 4, 1, 1, 1)
        self.stepLineEdit_3 = QtWidgets.QLineEdit(self.group_param_ellip2)
        self.stepLineEdit_3.setEnabled(True)
        self.stepLineEdit_3.setObjectName("stepLineEdit_3")
        self.grid_ellip2.addWidget(self.stepLineEdit_3, 7, 1, 1, 1)
        self.minsmaLineEdit_2 = QtWidgets.QLineEdit(self.group_param_ellip2)
        self.minsmaLineEdit_2.setEnabled(True)
        self.minsmaLineEdit_2.setObjectName("minsmaLineEdit_2")
        self.grid_ellip2.addWidget(self.minsmaLineEdit_2, 5, 1, 1, 1)
        self.fflagLabel_2 = QtWidgets.QLabel(self.group_param_ellip2)
        self.fflagLabel_2.setEnabled(True)
        self.fflagLabel_2.setObjectName("fflagLabel_2")
        self.grid_ellip2.addWidget(self.fflagLabel_2, 2, 0, 1, 1)
        self.fflagLineEdit_2 = QtWidgets.QLineEdit(self.group_param_ellip2)
        self.fflagLineEdit_2.setEnabled(True)
        self.fflagLineEdit_2.setObjectName("fflagLineEdit_2")
        self.grid_ellip2.addWidget(self.fflagLineEdit_2, 2, 1, 1, 1)
        self.sclipLabel_2 = QtWidgets.QLabel(self.group_param_ellip2)
        self.sclipLabel_2.setEnabled(True)
        self.sclipLabel_2.setObjectName("sclipLabel_2")
        self.grid_ellip2.addWidget(self.sclipLabel_2, 1, 0, 1, 1)
        self.maxsmaLineEdit_2 = QtWidgets.QLineEdit(self.group_param_ellip2)
        self.maxsmaLineEdit_2.setEnabled(True)
        self.maxsmaLineEdit_2.setObjectName("maxsmaLineEdit_2")
        self.grid_ellip2.addWidget(self.maxsmaLineEdit_2, 6, 1, 1, 1)
        self.converLineEdit_2 = QtWidgets.QLineEdit(self.group_param_ellip2)
        self.converLineEdit_2.setEnabled(True)
        self.converLineEdit_2.setObjectName("converLineEdit_2")
        self.grid_ellip2.addWidget(self.converLineEdit_2, 3, 1, 1, 1)
        self.maxsmaLabel_2 = QtWidgets.QLabel(self.group_param_ellip2)
        self.maxsmaLabel_2.setEnabled(True)
        self.maxsmaLabel_2.setObjectName("maxsmaLabel_2")
        self.grid_ellip2.addWidget(self.maxsmaLabel_2, 6, 0, 1, 1)
        self.cutLabel_2 = QtWidgets.QLabel(self.group_param_ellip2)
        self.cutLabel_2.setEnabled(True)
        self.cutLabel_2.setAcceptDrops(True)
        self.cutLabel_2.setObjectName("cutLabel_2")
        self.grid_ellip2.addWidget(self.cutLabel_2, 9, 0, 1, 1)
        self.sclipLineEdit_2 = QtWidgets.QLineEdit(self.group_param_ellip2)
        self.sclipLineEdit_2.setEnabled(True)
        self.sclipLineEdit_2.setObjectName("sclipLineEdit_2")
        self.grid_ellip2.addWidget(self.sclipLineEdit_2, 1, 1, 1, 1)
        self.intmodeLabel_2 = QtWidgets.QLabel(self.group_param_ellip2)
        self.intmodeLabel_2.setEnabled(True)
        self.intmodeLabel_2.setObjectName("intmodeLabel_2")
        self.grid_ellip2.addWidget(self.intmodeLabel_2, 4, 0, 1, 1)
        self.nclipLabel_2 = QtWidgets.QLabel(self.group_param_ellip2)
        self.nclipLabel_2.setEnabled(True)
        self.nclipLabel_2.setObjectName("nclipLabel_2")
        self.grid_ellip2.addWidget(self.nclipLabel_2, 0, 0, 1, 1)
        self.cutLineEdit_2 = QtWidgets.QLineEdit(self.group_param_ellip2)
        self.cutLineEdit_2.setEnabled(False)
        self.cutLineEdit_2.setAcceptDrops(True)
        self.cutLineEdit_2.setClearButtonEnabled(False)
        self.cutLineEdit_2.setObjectName("cutLineEdit_2")
        self.grid_ellip2.addWidget(self.cutLineEdit_2, 9, 1, 1, 1)
        self.stepLineEdit_4 = QtWidgets.QLineEdit(self.group_param_ellip2)
        self.stepLineEdit_4.setEnabled(False)
        self.stepLineEdit_4.setAcceptDrops(True)
        self.stepLineEdit_4.setClearButtonEnabled(False)
        self.stepLineEdit_4.setObjectName("stepLineEdit_4")
        self.grid_ellip2.addWidget(self.stepLineEdit_4, 14, 1, 1, 1)
        self.stepLabel_4 = QtWidgets.QLabel(self.group_param_ellip2)
        self.stepLabel_4.setEnabled(True)
        self.stepLabel_4.setAcceptDrops(True)
        self.stepLabel_4.setObjectName("stepLabel_4")
        self.grid_ellip2.addWidget(self.stepLabel_4, 14, 0, 1, 1)
        self.fixpar_2 = QtWidgets.QCheckBox(self.group_param_ellip2)
        self.fixpar_2.setEnabled(True)
        self.fixpar_2.setObjectName("fixpar_2")
        self.grid_ellip2.addWidget(self.fixpar_2, 8, 0, 1, 1)
        self.gridLayout_2.addWidget(self.group_param_ellip2, 3, 1, 1, 1)
        self.group_param_ellip1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_param_ellip1.setObjectName("group_param_ellip1")
        self.grid_ellip1 = QtWidgets.QGridLayout(self.group_param_ellip1)
        self.grid_ellip1.setObjectName("grid_ellip1")
        self.stepLabel = QtWidgets.QLabel(self.group_param_ellip1)
        self.stepLabel.setObjectName("stepLabel")
        self.grid_ellip1.addWidget(self.stepLabel, 7, 0, 1, 1)
        self.converLabel = QtWidgets.QLabel(self.group_param_ellip1)
        self.converLabel.setObjectName("converLabel")
        self.grid_ellip1.addWidget(self.converLabel, 3, 0, 1, 1)
        self.minsmaLabel = QtWidgets.QLabel(self.group_param_ellip1)
        self.minsmaLabel.setObjectName("minsmaLabel")
        self.grid_ellip1.addWidget(self.minsmaLabel, 5, 0, 1, 1)
        self.nclipLineEdit = QtWidgets.QLineEdit(self.group_param_ellip1)
        self.nclipLineEdit.setObjectName("nclipLineEdit")
        self.grid_ellip1.addWidget(self.nclipLineEdit, 0, 1, 1, 1)
        self.intmodeComboBox = QtWidgets.QComboBox(self.group_param_ellip1)
        self.intmodeComboBox.setObjectName("intmodeComboBox")
        self.grid_ellip1.addWidget(self.intmodeComboBox, 4, 1, 1, 1)
        self.stepLineEdit = QtWidgets.QLineEdit(self.group_param_ellip1)
        self.stepLineEdit.setObjectName("stepLineEdit")
        self.grid_ellip1.addWidget(self.stepLineEdit, 7, 1, 1, 1)
        self.minsmaLineEdit = QtWidgets.QLineEdit(self.group_param_ellip1)
        self.minsmaLineEdit.setObjectName("minsmaLineEdit")
        self.grid_ellip1.addWidget(self.minsmaLineEdit, 5, 1, 1, 1)
        self.fflagLabel = QtWidgets.QLabel(self.group_param_ellip1)
        self.fflagLabel.setObjectName("fflagLabel")
        self.grid_ellip1.addWidget(self.fflagLabel, 2, 0, 1, 1)
        self.fflagLineEdit = QtWidgets.QLineEdit(self.group_param_ellip1)
        self.fflagLineEdit.setObjectName("fflagLineEdit")
        self.grid_ellip1.addWidget(self.fflagLineEdit, 2, 1, 1, 1)
        self.sclipLabel = QtWidgets.QLabel(self.group_param_ellip1)
        self.sclipLabel.setObjectName("sclipLabel")
        self.grid_ellip1.addWidget(self.sclipLabel, 1, 0, 1, 1)
        self.maxsmaLineEdit = QtWidgets.QLineEdit(self.group_param_ellip1)
        self.maxsmaLineEdit.setObjectName("maxsmaLineEdit")
        self.grid_ellip1.addWidget(self.maxsmaLineEdit, 6, 1, 1, 1)
        self.converLineEdit = QtWidgets.QLineEdit(self.group_param_ellip1)
        self.converLineEdit.setObjectName("converLineEdit")
        self.grid_ellip1.addWidget(self.converLineEdit, 3, 1, 1, 1)
        self.maxsmaLabel = QtWidgets.QLabel(self.group_param_ellip1)
        self.maxsmaLabel.setObjectName("maxsmaLabel")
        self.grid_ellip1.addWidget(self.maxsmaLabel, 6, 0, 1, 1)
        self.cutLabel = QtWidgets.QLabel(self.group_param_ellip1)
        self.cutLabel.setEnabled(False)
        self.cutLabel.setAcceptDrops(True)
        self.cutLabel.setObjectName("cutLabel")
        self.grid_ellip1.addWidget(self.cutLabel, 9, 0, 1, 1)
        self.sclipLineEdit = QtWidgets.QLineEdit(self.group_param_ellip1)
        self.sclipLineEdit.setObjectName("sclipLineEdit")
        self.grid_ellip1.addWidget(self.sclipLineEdit, 1, 1, 1, 1)
        self.intmodeLabel = QtWidgets.QLabel(self.group_param_ellip1)
        self.intmodeLabel.setObjectName("intmodeLabel")
        self.grid_ellip1.addWidget(self.intmodeLabel, 4, 0, 1, 1)
        self.nclipLabel = QtWidgets.QLabel(self.group_param_ellip1)
        self.nclipLabel.setObjectName("nclipLabel")
        self.grid_ellip1.addWidget(self.nclipLabel, 0, 0, 1, 1)
        self.cutLineEdit = QtWidgets.QLineEdit(self.group_param_ellip1)
        self.cutLineEdit.setEnabled(False)
        self.cutLineEdit.setAcceptDrops(True)
        self.cutLineEdit.setClearButtonEnabled(False)
        self.cutLineEdit.setObjectName("cutLineEdit")
        self.grid_ellip1.addWidget(self.cutLineEdit, 9, 1, 1, 1)
        self.stepLineEdit_2 = QtWidgets.QLineEdit(self.group_param_ellip1)
        self.stepLineEdit_2.setEnabled(False)
        self.stepLineEdit_2.setAcceptDrops(True)
        self.stepLineEdit_2.setClearButtonEnabled(False)
        self.stepLineEdit_2.setObjectName("stepLineEdit_2")
        self.grid_ellip1.addWidget(self.stepLineEdit_2, 14, 1, 1, 1)
        self.stepLabel_2 = QtWidgets.QLabel(self.group_param_ellip1)
        self.stepLabel_2.setEnabled(False)
        self.stepLabel_2.setAcceptDrops(True)
        self.stepLabel_2.setObjectName("stepLabel_2")
        self.grid_ellip1.addWidget(self.stepLabel_2, 14, 0, 1, 1)
        self.fixpar = QtWidgets.QCheckBox(self.group_param_ellip1)
        self.fixpar.setObjectName("fixpar")
        self.grid_ellip1.addWidget(self.fixpar, 8, 0, 1, 1)
        self.gridLayout_2.addWidget(self.group_param_ellip1, 3, 0, 1, 1)
        self.groupBox_iso0 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_iso0.setObjectName("groupBox_iso0")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_iso0)
        self.formLayout.setObjectName("formLayout")
        self.x0Label = QtWidgets.QLabel(self.groupBox_iso0)
        self.x0Label.setObjectName("x0Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.x0Label)
        self.x0LineEdit = QtWidgets.QLineEdit(self.groupBox_iso0)
        self.x0LineEdit.setObjectName("x0LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.x0LineEdit)
        self.y0Label = QtWidgets.QLabel(self.groupBox_iso0)
        self.y0Label.setObjectName("y0Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.y0Label)
        self.y0LineEdit = QtWidgets.QLineEdit(self.groupBox_iso0)
        self.y0LineEdit.setObjectName("y0LineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.y0LineEdit)
        self.smaLabel = QtWidgets.QLabel(self.groupBox_iso0)
        self.smaLabel.setObjectName("smaLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.smaLabel)
        self.smaLineEdit = QtWidgets.QLineEdit(self.groupBox_iso0)
        self.smaLineEdit.setObjectName("smaLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.smaLineEdit)
        self.ellipticidadLabel = QtWidgets.QLabel(self.groupBox_iso0)
        self.ellipticidadLabel.setObjectName("ellipticidadLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ellipticidadLabel)
        self.ellipticidadLineEdit = QtWidgets.QLineEdit(self.groupBox_iso0)
        self.ellipticidadLineEdit.setObjectName("ellipticidadLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ellipticidadLineEdit)
        self.positionAngleLabel = QtWidgets.QLabel(self.groupBox_iso0)
        self.positionAngleLabel.setObjectName("positionAngleLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.positionAngleLabel)
        self.positionAngleLineEdit = QtWidgets.QLineEdit(self.groupBox_iso0)
        self.positionAngleLineEdit.setObjectName("positionAngleLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.positionAngleLineEdit)
        self.gridLayout_2.addWidget(self.groupBox_iso0, 2, 0, 1, 1)
        self.groupBox_iso1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_iso1.setObjectName("groupBox_iso1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_iso1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.x0Label_2 = QtWidgets.QLabel(self.groupBox_iso1)
        self.x0Label_2.setObjectName("x0Label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.x0Label_2)
        self.x0LineEdit_2 = QtWidgets.QLineEdit(self.groupBox_iso1)
        self.x0LineEdit_2.setObjectName("x0LineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.x0LineEdit_2)
        self.y0Label_2 = QtWidgets.QLabel(self.groupBox_iso1)
        self.y0Label_2.setObjectName("y0Label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.y0Label_2)
        self.y0LineEdit_2 = QtWidgets.QLineEdit(self.groupBox_iso1)
        self.y0LineEdit_2.setObjectName("y0LineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.y0LineEdit_2)
        self.smaLabel_2 = QtWidgets.QLabel(self.groupBox_iso1)
        self.smaLabel_2.setObjectName("smaLabel_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.smaLabel_2)
        self.smaLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_iso1)
        self.smaLineEdit_2.setObjectName("smaLineEdit_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.smaLineEdit_2)
        self.ellipticidadLabel_2 = QtWidgets.QLabel(self.groupBox_iso1)
        self.ellipticidadLabel_2.setObjectName("ellipticidadLabel_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ellipticidadLabel_2)
        self.ellipticidadLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_iso1)
        self.ellipticidadLineEdit_2.setObjectName("ellipticidadLineEdit_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ellipticidadLineEdit_2)
        self.positionAngleLabel_2 = QtWidgets.QLabel(self.groupBox_iso1)
        self.positionAngleLabel_2.setObjectName("positionAngleLabel_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.positionAngleLabel_2)
        self.positionAngleLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_iso1)
        self.positionAngleLineEdit_2.setObjectName("positionAngleLineEdit_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.positionAngleLineEdit_2)
        self.gridLayout_2.addWidget(self.groupBox_iso1, 2, 1, 1, 1)
        self.form_background_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.form_background_2.setObjectName("form_background_2")
        self.form_background = QtWidgets.QFormLayout(self.form_background_2)
        self.form_background.setObjectName("form_background")
        self.valorLineEdit = QtWidgets.QLineEdit(self.form_background_2)
        self.valorLineEdit.setObjectName("valorLineEdit")
        self.form_background.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.valorLineEdit)
        self.modoLabel = QtWidgets.QLabel(self.form_background_2)
        self.modoLabel.setObjectName("modoLabel")
        self.form_background.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.modoLabel)
        self.modoComboBox = QtWidgets.QComboBox(self.form_background_2)
        self.modoComboBox.setEnabled(True)
        self.modoComboBox.setObjectName("modoComboBox")
        self.form_background.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.modoComboBox)
        self.valorLabel = QtWidgets.QLabel(self.form_background_2)
        self.valorLabel.setObjectName("valorLabel")
        self.form_background.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.valorLabel)
        self.backgroundLabel = QtWidgets.QLabel(self.form_background_2)
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.form_background.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.backgroundLabel)
        self.gridLayout_2.addWidget(self.form_background_2, 12, 1, 2, 1)
        self.mask_prop_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.mask_prop_2.setObjectName("mask_prop_2")
        self.mask_prop = QtWidgets.QFormLayout(self.mask_prop_2)
        self.mask_prop.setObjectName("mask_prop")
        self.nthrLabel = QtWidgets.QLabel(self.mask_prop_2)
        self.nthrLabel.setObjectName("nthrLabel")
        self.mask_prop.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nthrLabel)
        self.nthrLineEdit = QtWidgets.QLineEdit(self.mask_prop_2)
        self.nthrLineEdit.setObjectName("nthrLineEdit")
        self.mask_prop.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nthrLineEdit)
        self.fwhmLabel = QtWidgets.QLabel(self.mask_prop_2)
        self.fwhmLabel.setObjectName("fwhmLabel")
        self.mask_prop.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fwhmLabel)
        self.fwhmLineEdit = QtWidgets.QLineEdit(self.mask_prop_2)
        self.fwhmLineEdit.setObjectName("fwhmLineEdit")
        self.mask_prop.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fwhmLineEdit)
        self.sharpLabel = QtWidgets.QLabel(self.mask_prop_2)
        self.sharpLabel.setObjectName("sharpLabel")
        self.mask_prop.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sharpLabel)
        self.sharpLineEdit = QtWidgets.QLineEdit(self.mask_prop_2)
        self.sharpLineEdit.setObjectName("sharpLineEdit")
        self.mask_prop.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sharpLineEdit)
        self.roundlimLabel = QtWidgets.QLabel(self.mask_prop_2)
        self.roundlimLabel.setObjectName("roundlimLabel")
        self.mask_prop.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.roundlimLabel)
        self.roundlimLineEdit = QtWidgets.QLineEdit(self.mask_prop_2)
        self.roundlimLineEdit.setObjectName("roundlimLineEdit")
        self.mask_prop.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.roundlimLineEdit)
        self.thresholdLabel = QtWidgets.QLabel(self.mask_prop_2)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.mask_prop.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.thresholdLabel)
        self.thresholdLineEdit = QtWidgets.QLineEdit(self.mask_prop_2)
        self.thresholdLineEdit.setObjectName("thresholdLineEdit")
        self.mask_prop.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.thresholdLineEdit)
        self.gridLayout_2.addWidget(self.mask_prop_2, 9, 1, 3, 1)
        self.form_graf_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.form_graf_2.setObjectName("form_graf_2")
        self.form_graf = QtWidgets.QFormLayout(self.form_graf_2)
        self.form_graf.setObjectName("form_graf")
        self.graficarParMetrosIsofotalesLabel = QtWidgets.QLabel(self.form_graf_2)
        self.graficarParMetrosIsofotalesLabel.setObjectName("graficarParMetrosIsofotalesLabel")
        self.form_graf.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.graficarParMetrosIsofotalesLabel)
        self.graficarParMetrosIsofotalesCheckBox = QtWidgets.QCheckBox(self.form_graf_2)
        self.graficarParMetrosIsofotalesCheckBox.setChecked(True)
        self.graficarParMetrosIsofotalesCheckBox.setObjectName("graficarParMetrosIsofotalesCheckBox")
        self.form_graf.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.graficarParMetrosIsofotalesCheckBox)
        self.lMiteHorizontalLabel = QtWidgets.QLabel(self.form_graf_2)
        self.lMiteHorizontalLabel.setObjectName("lMiteHorizontalLabel")
        self.form_graf.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lMiteHorizontalLabel)
        self.lMiteHorizontalLineEdit = QtWidgets.QLineEdit(self.form_graf_2)
        self.lMiteHorizontalLineEdit.setObjectName("lMiteHorizontalLineEdit")
        self.form_graf.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lMiteHorizontalLineEdit)
        self.graficarPerfilDeBrilloLabel = QtWidgets.QLabel(self.form_graf_2)
        self.graficarPerfilDeBrilloLabel.setObjectName("graficarPerfilDeBrilloLabel")
        self.form_graf.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.graficarPerfilDeBrilloLabel)
        self.graficarPerfilDeBrilloCheckBox = QtWidgets.QCheckBox(self.form_graf_2)
        self.graficarPerfilDeBrilloCheckBox.setChecked(True)
        self.graficarPerfilDeBrilloCheckBox.setObjectName("graficarPerfilDeBrilloCheckBox")
        self.form_graf.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.graficarPerfilDeBrilloCheckBox)
        self.lMiteHorizontalLabel_2 = QtWidgets.QLabel(self.form_graf_2)
        self.lMiteHorizontalLabel_2.setObjectName("lMiteHorizontalLabel_2")
        self.form_graf.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lMiteHorizontalLabel_2)
        self.lMiteHorizontalLineEdit_2 = QtWidgets.QLineEdit(self.form_graf_2)
        self.lMiteHorizontalLineEdit_2.setObjectName("lMiteHorizontalLineEdit_2")
        self.form_graf.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lMiteHorizontalLineEdit_2)
        self.usarRadioEquivalenteLabel = QtWidgets.QLabel(self.form_graf_2)
        self.usarRadioEquivalenteLabel.setObjectName("usarRadioEquivalenteLabel")
        self.form_graf.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.usarRadioEquivalenteLabel)
        self.usarRadioEquivalenteCheckBox = QtWidgets.QCheckBox(self.form_graf_2)
        self.usarRadioEquivalenteCheckBox.setChecked(True)
        self.usarRadioEquivalenteCheckBox.setObjectName("usarRadioEquivalenteCheckBox")
        self.form_graf.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.usarRadioEquivalenteCheckBox)
        self.escalaLabel = QtWidgets.QLabel(self.form_graf_2)
        self.escalaLabel.setObjectName("escalaLabel")
        self.form_graf.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.escalaLabel)
        self.escalaLineEdit = QtWidgets.QLineEdit(self.form_graf_2)
        self.escalaLineEdit.setObjectName("escalaLineEdit")
        self.form_graf.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.escalaLineEdit)
        self.tiempoDeExposiciNLabel = QtWidgets.QLabel(self.form_graf_2)
        self.tiempoDeExposiciNLabel.setObjectName("tiempoDeExposiciNLabel")
        self.form_graf.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.tiempoDeExposiciNLabel)
        self.tiempoDeExposiciNLineEdit = QtWidgets.QLineEdit(self.form_graf_2)
        self.tiempoDeExposiciNLineEdit.setObjectName("tiempoDeExposiciNLineEdit")
        self.form_graf.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.tiempoDeExposiciNLineEdit)
        self.unidadDeAbscisaLabel_2 = QtWidgets.QLabel(self.form_graf_2)
        self.unidadDeAbscisaLabel_2.setObjectName("unidadDeAbscisaLabel_2")
        self.form_graf.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.unidadDeAbscisaLabel_2)
        self.unidadDeAbscisaComboBox = QtWidgets.QComboBox(self.form_graf_2)
        self.unidadDeAbscisaComboBox.setObjectName("unidadDeAbscisaComboBox")
        self.form_graf.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.unidadDeAbscisaComboBox)
        self.puntoCeroDeLaMagnitudLabel = QtWidgets.QLabel(self.form_graf_2)
        self.puntoCeroDeLaMagnitudLabel.setObjectName("puntoCeroDeLaMagnitudLabel")
        self.form_graf.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.puntoCeroDeLaMagnitudLabel)
        self.puntoCeroDeLaMagnitudLineEdit = QtWidgets.QLineEdit(self.form_graf_2)
        self.puntoCeroDeLaMagnitudLineEdit.setObjectName("puntoCeroDeLaMagnitudLineEdit")
        self.form_graf.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.puntoCeroDeLaMagnitudLineEdit)
        self.gridLayout_2.addWidget(self.form_graf_2, 8, 0, 6, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.isolist = QtWidgets.QWidget(self.centralwidget)
        self.isolist.setObjectName("isolist")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.isolist)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_save_isolist = QtWidgets.QCheckBox(self.isolist)
        self.checkBox_save_isolist.setObjectName("checkBox_save_isolist")
        self.gridLayout_3.addWidget(self.checkBox_save_isolist, 0, 0, 1, 1)
        self.button_save_isolist = QtWidgets.QPushButton(self.isolist)
        self.button_save_isolist.setEnabled(False)
        self.button_save_isolist.setObjectName("button_save_isolist")
        self.gridLayout_3.addWidget(self.button_save_isolist, 0, 3, 1, 1)
        self.checkBox_save_residue = QtWidgets.QCheckBox(self.isolist)
        self.checkBox_save_residue.setObjectName("checkBox_save_residue")
        self.gridLayout_3.addWidget(self.checkBox_save_residue, 1, 0, 1, 1)
        self.line_edir_archivo_isolist = QtWidgets.QLineEdit(self.isolist)
        self.line_edir_archivo_isolist.setEnabled(False)
        self.line_edir_archivo_isolist.setObjectName("line_edir_archivo_isolist")
        self.gridLayout_3.addWidget(self.line_edir_archivo_isolist, 0, 1, 1, 2)
        self.pushButton_save_residue = QtWidgets.QPushButton(self.isolist)
        self.pushButton_save_residue.setEnabled(False)
        self.pushButton_save_residue.setObjectName("pushButton_save_residue")
        self.gridLayout_3.addWidget(self.pushButton_save_residue, 1, 3, 1, 1)
        self.lineEdit_save_residue = QtWidgets.QLineEdit(self.isolist)
        self.lineEdit_save_residue.setEnabled(False)
        self.lineEdit_save_residue.setObjectName("lineEdit_save_residue")
        self.gridLayout_3.addWidget(self.lineEdit_save_residue, 1, 1, 1, 2)
        self.verticalLayout.addWidget(self.isolist)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_pmt_file = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Unifont Upper")
        self.load_pmt_file.setFont(font)
        self.load_pmt_file.setStyleSheet("QPushButton{rgb(85, 0, 255)}")
        self.load_pmt_file.setObjectName("load_pmt_file")
        self.horizontalLayout.addWidget(self.load_pmt_file)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_save = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Unifont Upper")
        font.setPointSize(9)
        self.button_save.setFont(font)
        self.button_save.setObjectName("button_save")
        self.horizontalLayout.addWidget(self.button_save)
        self.button_save_run = QtWidgets.QPushButton(self.widget)
        self.button_save_run.setObjectName("button_save_run")
        self.horizontalLayout.addWidget(self.button_save_run)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.autockeck()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fotometría de galaxias tempranas"))
        self.label_param_ell2.setText(_translate("MainWindow", "Input para generar máscara"))
        self.label_param_ell1.setText(_translate("MainWindow", "Input de Fotometría"))
        self.imagen1.setTitle(_translate("MainWindow", "Cargar archivos"))
        self.label_imagen_1.setText(_translate("MainWindow", "Imagen"))
        self.navegar_imagen_1.setText(_translate("MainWindow", "Navegar📁"))
        self.label_mascara.setText(_translate("MainWindow", "Máscara"))
        self.mascara_cgeck.setText(_translate("MainWindow", "Generar"))
        self.label_mascara_archivo.setText(_translate("MainWindow", "Usar archivo"))
        self.navegar_mascara.setText(_translate("MainWindow", "Navegar📁"))
        
       
        self.group_param_ellip2.setTitle(_translate("MainWindow", "Parámetros de ellipse "))
        self.stepLabel_3.setText(_translate("MainWindow", "step"))
        self.converLabel_2.setText(_translate("MainWindow", "conver"))
        self.minsmaLabel_2.setText(_translate("MainWindow", "minsma"))
        self.fflagLabel_2.setText(_translate("MainWindow", "fflag"))
        self.sclipLabel_2.setText(_translate("MainWindow", "sclip"))
        self.maxsmaLabel_2.setText(_translate("MainWindow", "maxsma"))
        self.cutLabel_2.setText(_translate("MainWindow", "cut"))
        self.intmodeLabel_2.setText(_translate("MainWindow", "intmode"))
        self.nclipLabel_2.setText(_translate("MainWindow", "nclip"))
        self.stepLabel_4.setText(_translate("MainWindow", "step"))
        self.fixpar_2.setText(_translate("MainWindow", "fixpar"))
        self.group_param_ellip1.setTitle(_translate("MainWindow", "Parámetros de ellipse"))
        self.stepLabel.setText(_translate("MainWindow", "step"))
        self.converLabel.setText(_translate("MainWindow", "conver"))
        self.minsmaLabel.setText(_translate("MainWindow", "minsma"))
        self.fflagLabel.setText(_translate("MainWindow", "fflag"))
        self.sclipLabel.setText(_translate("MainWindow", "sclip"))
        self.maxsmaLabel.setText(_translate("MainWindow", "maxsma"))
        self.cutLabel.setText(_translate("MainWindow", "cut"))
        self.intmodeLabel.setText(_translate("MainWindow", "intmode"))
        self.nclipLabel.setText(_translate("MainWindow", "nclip"))
        self.stepLabel_2.setText(_translate("MainWindow", "step"))
        self.fixpar.setText(_translate("MainWindow", "fixpar"))
        self.groupBox_iso0.setTitle(_translate("MainWindow", "Isofota inicial"))
        self.x0Label.setText(_translate("MainWindow", "x0"))
        self.y0Label.setText(_translate("MainWindow", "y0"))
        self.smaLabel.setText(_translate("MainWindow", "sma"))
        self.ellipticidadLabel.setText(_translate("MainWindow", "ellipticidad"))
        self.positionAngleLabel.setText(_translate("MainWindow", "position angle"))
        self.groupBox_iso1.setTitle(_translate("MainWindow", "Isofota inicial"))
        self.x0Label_2.setText(_translate("MainWindow", "x0"))
        self.y0Label_2.setText(_translate("MainWindow", "y0"))
        self.smaLabel_2.setText(_translate("MainWindow", "sma"))
        self.ellipticidadLabel_2.setText(_translate("MainWindow", "ellipticidad"))
        self.positionAngleLabel_2.setText(_translate("MainWindow", "position angle"))
        self.form_background_2.setTitle(_translate("MainWindow", "Background"))
        self.modoLabel.setText(_translate("MainWindow", "modo"))
        self.valorLabel.setText(_translate("MainWindow", "Valor"))
        self.mask_prop_2.setTitle(_translate("MainWindow", "Parámetros del cálculo de máscara"))
        self.nthrLabel.setText(_translate("MainWindow", "nthr"))
        self.fwhmLabel.setText(_translate("MainWindow", "fwhm"))
        self.sharpLabel.setText(_translate("MainWindow", "sharp"))
        self.roundlimLabel.setText(_translate("MainWindow", "roundlim"))
        self.thresholdLabel.setText(_translate("MainWindow", "threshold"))
        self.form_graf_2.setTitle(_translate("MainWindow", "Gráficos"))
        self.graficarParMetrosIsofotalesLabel.setText(_translate("MainWindow", "Graficar parámetros isofotales"))
        self.lMiteHorizontalLabel.setText(_translate("MainWindow", "Límite horizontal"))
        self.graficarPerfilDeBrilloLabel.setText(_translate("MainWindow", "Graficar perfil de brillo"))
        self.lMiteHorizontalLabel_2.setText(_translate("MainWindow", "Límite horizontal"))
        self.usarRadioEquivalenteLabel.setText(_translate("MainWindow", "Usar radio equivalente"))
        self.escalaLabel.setText(_translate("MainWindow", "Escala"))
        self.tiempoDeExposiciNLabel.setText(_translate("MainWindow", "Tiempo de exposición"))
        self.unidadDeAbscisaLabel_2.setText(_translate("MainWindow", "Unidad de abscisa"))
        self.puntoCeroDeLaMagnitudLabel.setText(_translate("MainWindow", "Punto cero de la magnitud"))
        self.checkBox_save_isolist.setText(_translate("MainWindow", "Guardar tabla de isofotas como archivo"))
        self.button_save_isolist.setText(_translate("MainWindow", "Navegar"))
        self.checkBox_save_residue.setText(_translate("MainWindow", "Guardar residuo"))
        self.pushButton_save_residue.setText(_translate("MainWindow", "Navegar"))
        self.load_pmt_file.setText(_translate("MainWindow", "Cargar Archivo de parámetros"))
        self.button_save.setText(_translate("MainWindow", "Guardar parámetros"))
        self.button_save_run.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.button_save_run.setText(_translate("MainWindow", "Guardar y Correr"))

    ######################################################## 
        ### llamo a la segunda ventana
        ## debo usar self. en todas las variables 
        # pues si no se borra ya que
        # QMainWindow takes ownership of the widget pointer and deletes it at the appropriate time.
        # see: http://enki-editor.org/2014/08/23/Pyqt_mem_mgmt.html
        self.scond_win = QtWidgets.QTabWidget()
        self.ui = Ui_TabPlots()
        self.ui.setupUi(self.scond_win)
        self.scond_win.show()
        
        
        ## carga los parámetros al iniciciar
        self.load_pmt()           
   ###################
    # funcionalidad de los objetos:
        
        
        self.autockeck() # enable or disable sections
        
            
        self.intmodeComboBox.addItems(
            ('bilinear', 'nearest_neighbor', 'mean', 'median')
            )
        self.intmodeComboBox_2.addItems(
            ('bilinear', 'nearest_neighbor', 'mean', 'median')
            )
        self.unidadDeAbscisaComboBox.addItems(
            ('arcsec','arcmin')
            )
        self.modoComboBox.addItems(
            ('median','mean')
            )
        
        self.navegar_imagen_1.clicked.connect( lambda:
            self.browser(
                self.line_imagen_1
                )
            )

        self.navegar_mascara.clicked.connect( lambda:
            self.browser(
                self.line_mascara
                )
            )
        self.button_save_isolist.clicked.connect( lambda:
            self.browser(
                self.line_edir_archivo_isolist
                )
            )
        self.pushButton_save_residue.clicked.connect( lambda:
            self.browser(
                self.lineEdit_save_residue
                )
            )
            
        self.load_pmt_file.clicked.connect(
            self.load_pmt               
            )        
        self.button_save.clicked.connect(
            self.save_pmt
            )
        self.button_save_run.clicked.connect(
            self.save_and_run
            )                
        
        
        
        self.ui.sig.clicked.connect(
            lambda: self.mvpg(self.ui.plot_fits_stackedWidget)
                )
        self.ui.prev.clicked.connect(
            lambda: self.mvpg(self.ui.plot_fits_stackedWidget,fw=False)

                )
        self.ui.sig_2.clicked.connect(
            lambda: self.mvpg(self.ui.plot_param_stackedWidget)
            )
        self.ui.prev_2.clicked.connect(
            lambda: self.mvpg(self.ui.plot_param_stackedWidget,fw=False)
            )
    ########################################################
    # funciones:
    
    def mvpg(self, stkwig, fw=True,skip=0):
        lim = [0,stkwig.count()]
        
        if fw:
            mv = 1
            
        else:
            mv =-1
        try:
            ### avanza o retrocede 
            stkwig.setCurrentIndex(stkwig.currentIndex() + mv )
        except ValueError:
            ## si no puede, va hacia el principio o al final
            ## esto no anda? 
            stkwig.setCurrentIndex(lim[mv])
    
    def enable(self,state,*args,disable=False):
        if disable:
            compar = QtCore.Qt.Unchecked
        else:
            compar = QtCore.Qt.Checked
        if state == compar :
            flag=True
        else:
            flag=False
        for arg in args:
            for a in arg:
                a.setEnabled(flag)
        
              
    def browser(self,line_edit):
        # options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        
        # fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                                  # "QFileDialog.getOpenFileName()",
                                                  # "","All Files (*);;Python Files (*.py)",
                                                  # options=options)
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                                            'Single File')
        line_edit.setText(fileName)

    def autockeck(self):
        
        self.mascara_cgeck.stateChanged.connect(
            lambda state:
                self.enable(state,
                            [self.navegar_mascara,
                             self.line_mascara],
                            disable=True
                            )
                )
       
        self.mascara_cgeck.stateChanged.connect(
            lambda state:
                self.enable(state,
                            [self.group_param_ellip2,
                             self.groupBox_iso1,
                             self.mask_prop_2,
                             self.mask_prop]
                            )
                )
            
        self.fixpar.stateChanged.connect(
            lambda state:
                    self.enable(state,
                                [self.cutLineEdit,
                                 self.stepLineEdit_2]
                                )
                    )
        self.fixpar_2.stateChanged.connect(
            lambda state:
                    self.enable(state,
                                [self.cutLineEdit_2,
                                 self.stepLineEdit_4]
                                )
                    )            
        self.graficarParMetrosIsofotalesCheckBox.stateChanged.connect(
            lambda state:
                self.enable(state,
                            [self.lMiteHorizontalLineEdit])
                )
        self.graficarPerfilDeBrilloCheckBox.stateChanged.connect(
            lambda state:
                self.enable(state,
                            [self.lMiteHorizontalLineEdit_2,
                             self.puntoCeroDeLaMagnitudLineEdit,
                             self.tiempoDeExposiciNLineEdit])
                )
        self.usarRadioEquivalenteCheckBox.stateChanged.connect(
            lambda state:
                self.enable(state,
                            [self.unidadDeAbscisaComboBox]
                            )
                )
        self.checkBox_save_isolist.stateChanged.connect(
            lambda state:
                self.enable(state,
                            [self.button_save_isolist,
                             self.line_edir_archivo_isolist]
                            )
                )
        self.checkBox_save_residue.stateChanged.connect(
            lambda state:
                self.enable(state,
                            [self.lineEdit_save_residue,
                             self.pushButton_save_residue]
                            )
                )
        

    def save_pmt(self):
        reload(pmt)
        
        fname=pmt.fname
        
        
        fname['ref']['path'],fname['ref']['name']=path.split(self.line_imagen_1.text())
       
        fname['ref']['path']=self.tst(fname['ref']['path'])
        fname['ref']['name']= self.tst(fname['ref']['name'])
        
        fname['out']['residue']['path'], fname['out']['residue']['name'] = path.split(self.lineEdit_save_residue.text())
        fname['out']['residue']['name'], fname['out']['residue']['path']=self.tst(fname['out']['residue']['name']), self.tst(fname['out']['residue']['path'])
        fname['out']['table']['path'], fname['out']['table']['name'] = path.split(self.line_edir_archivo_isolist.text())
        fname['out']['table']['name'], fname['out']['table']['path']=self.tst(fname['out']['table']['name']),self.tst(fname['out']['table']['path'])
        guardar=pmt.guardar
        
        
    
       
        guardar['residue']  = self.checkBox_save_residue.isChecked()
        guardar['save_iso'] = self.checkBox_save_isolist.isChecked()
        
        
        ellipse_inicial= pmt.ellipse_incial
        
        ellipse_inicial['x0']    = self.nmb(self.x0LineEdit.text())
        ellipse_inicial['y0']    = self.nmb(self.y0LineEdit.text())
        ellipse_inicial['sma']   = self.nmb(self.smaLineEdit.text())
        ellipse_inicial['ellip'] = self.nmb(self.ellipticidadLineEdit.text())
        ellipse_inicial['pa']    = self.nmb(self.positionAngleLineEdit.text())
        
        ellipse_inicial_0= pmt.ellipse_incial_0
        
        ellipse_inicial_0['x0']    = self.nmb(self.x0LineEdit_2.text())
        ellipse_inicial_0['y0']    = self.nmb(self.y0LineEdit_2.text())
        ellipse_inicial_0['sma']   = self.nmb(self.smaLineEdit_2.text())
        ellipse_inicial_0['ellip'] = self.nmb(self.ellipticidadLineEdit_2.text())
        ellipse_inicial_0['pa']    = self.nmb(self.positionAngleLineEdit_2.text())


        fit_ell_par=pmt.fit_ell_par
        
        fit_ell_par['sclip']      = self.nmb(self.sclipLineEdit.text())
        fit_ell_par['nclip']      = self.nmb(self.nclipLineEdit.text())
        fit_ell_par['fflag']      = self.nmb(self.fflagLineEdit.text())
        fit_ell_par['integrmode'] = self.intmodeComboBox.currentText()
        fit_ell_par['cut']        = self.nmb(self.cutLineEdit.text())
        fit_ell_par['maxs']       = self.nmb(self.maxsmaLineEdit.text())
        fit_ell_par['fix']        = self.fixpar.isChecked()
        fit_ell_par['step0']      = self.nmb(self.stepLineEdit.text())
        fit_ell_par['step1']      = self.nmb(self.stepLineEdit_2.text())
        fit_ell_par['conver']     = self.nmb(self.converLineEdit.text())
        fit_ell_par['minsma']     = self.nmb(self.minsmaLineEdit.text())
        
        
        fit_ell_par_0=pmt.fit_ell_par_0

        fit_ell_par_0['sclip']      = self.nmb(self.sclipLineEdit_2.text())
        fit_ell_par_0['nclip']      = self.nmb(self.nclipLineEdit_2.text())
        fit_ell_par_0['fflag']      = self.nmb(self.fflagLineEdit_2.text())
        fit_ell_par_0['integrmode'] = self.intmodeComboBox_2.currentText()
        fit_ell_par_0['cut']        = self.nmb(self.cutLineEdit_2.text())
        fit_ell_par_0['maxs']       = self.nmb(self.maxsmaLineEdit_2.text())
        fit_ell_par_0['fix']        = self.fixpar_2.isChecked()
        fit_ell_par_0['step0']      = self.nmb(self.stepLineEdit_3.text())
        fit_ell_par_0['step1']      = self.nmb(self.stepLineEdit_4.text())
        fit_ell_par_0['conver']     = self.nmb(self.converLineEdit_2.text())
        fit_ell_par_0['minsma']     = self.nmb(self.minsmaLineEdit_2.text())
                                             
        
        bkg= pmt.bkg
        
        bkg['bkg']  = self.nmb(self.valorLineEdit.text())
        bkg['mode'] = self.modoComboBox.currentText()
        
        mask= pmt.mask
        
        mask['path'],mask['file'] = path.split(self.line_mascara.text())
        mask['file'],mask['path'] = self.tst(mask['file']),self.tst(mask['path']) 
        mask['calc']              = self.mascara_cgeck.isChecked()
        mask['nthr']              = self.nmb(self.nthrLineEdit.text())
        mask['fwhm']              = self.nmb(self.fwhmLineEdit.text())
        mask['sharp']             = list(
                                         map(float,self.sharpLineEdit.text()[1:-1].split(','))
                                         )
        mask['roundlim']          = list(
                                         map(float,self.roundlimLineEdit.text()[1:-1].split(','))
                                         )
        mask['threshold']         = self.nmb(self.thresholdLineEdit.text())
        
        
        plots=pmt.plots
        
        plots['param_plot'] = self.graficarParMetrosIsofotalesCheckBox.isChecked()
        plots['mu_plot']    = self.graficarPerfilDeBrilloCheckBox.isChecked()
        plots['req']        = self.usarRadioEquivalenteCheckBox.isChecked()
        plots['n_par']      = self.nmb(self.lMiteHorizontalLineEdit.text())
        pmt.plots['n_mu']   = self.nmb(self.lMiteHorizontalLineEdit_2.text())
        pmt.plots['E']      = self.nmb(self.escalaLineEdit.text())
        plots['texp']       = self.nmb( self.tiempoDeExposiciNLineEdit.text())
        plots['mu0']        = self.nmb(self.puntoCeroDeLaMagnitudLineEdit.text())
        if self.unidadDeAbscisaComboBox.currentText()=='arcmin':
            plots['arcmin'] = True
        else:
            plots['arcmin'] = False
            
        aux = {
                'fname': fname,
                'ellipse_incial' : ellipse_inicial,
                'ellipse_incial_0' : ellipse_inicial_0,
                'guardar' : guardar,
                'fit_ell_par' : fit_ell_par,
                'fit_ell_par_0' : fit_ell_par_0,
                'bkg' : bkg,
                'mask' : mask,
                'plots' : plots
            }
        
        
        
        remove('parameters.py')
        f=open('parameters.py','w+')
        for k in aux.keys():
            f.write(k+' = ')
            json.dump( aux[k], f , indent=4)
            f.write('\n')
        f.close()
        
        with open('parameters.py','r') as f:
            datar=f.read()
        reempl = { 'null':'None', 'false':'False','true':'True'}
        datar=  self.replace_all(datar,reempl)
        with open('parameters.py','w') as f:
            f.write(datar)
            
            
    def save_and_run(self):
        self.save_pmt()

    ### run main
        plt.ioff()
        img,grafs,sky=main.main()  
        
        ## pa que guarde el valor de cielo q calculo
        self.valorLineEdit.setText(self.strn(sky))
        self.save_pmt()
        
    ### pass figs to plot window
        plt.ion()
        
        _ = [self.ui.page_0,self.ui.page_1,self.ui.page_2,self.ui.page_3,self.ui.page_4,self.ui.page_5,
             self.ui.page_6,self.ui.page_7,self.ui.page_8,self.ui.page_9,self.ui.page_10]
        
        for i in range(0,8) :
            if i < len(img):
                _[i].make_plot(img[i])
            else:
                _[i].hide()
                # self.ui.plot_fits_stackedWidget.removeWidget(_[i])
                
        # print (self.ui.plot_fits_stackedWidget.count())
                

        ## los dos ultimos son de la ventana de graficos, no de imagenes
        _[-2].make_plot(grafs[0])
        _[-1].make_plot(grafs[1])
        

    def load_pmt(self):
        reload(pmt)
        
        intgm =  ['bilinear', 'nearest_neighbor', 'mean', 'median']
        mode =  ['median','mean']
        unit = ['arcsec','arcmin']
        
        self.line_imagen_1.setText(
            pmt.fname['ref']['path']+'/'+
            pmt.fname['ref']['name']
            )
        
        self.line_mascara.setText(
            self.strn(pmt.mask['path'])+'/'+
            self.strn(pmt.mask['file'])
            )
        
        
        self.mascara_cgeck.setChecked(
            pmt.mask['calc']
            )
        
        self.nclipLineEdit.setText(self.strn(
            pmt.fit_ell_par['nclip']
            ))
        self.sclipLineEdit.setText(self.strn(
            pmt.fit_ell_par['sclip']
            ))
        self.fflagLineEdit.setText(self.strn(
            pmt.fit_ell_par['fflag']
            ))
        self.converLineEdit.setText(self.strn(
            pmt.fit_ell_par['conver']
            ))
        self.minsmaLineEdit.setText(self.strn(
            pmt.fit_ell_par['minsma']
            ))
        self.maxsmaLineEdit.setText(self.strn(
            pmt.fit_ell_par['maxs']
            ))
        self.intmodeComboBox.setCurrentIndex(
            intgm.index(pmt.fit_ell_par['integrmode'])
            )
        self.stepLineEdit.setText(self.strn(
            pmt.fit_ell_par['step0']
            ))
        self.fixpar.setChecked(
            pmt.fit_ell_par['fix']
            )
        self.cutLineEdit.setText(self.strn(
            pmt.fit_ell_par['cut']
            ))
        self.stepLineEdit_2.setText(self.strn(
            pmt.fit_ell_par['step1']
            ))
        
        self.x0LineEdit.setText(self.strn(
            pmt.ellipse_incial['x0']
            ))
        self.y0LineEdit.setText(self.strn(
            pmt.ellipse_incial['y0']
            ))
        self.smaLineEdit.setText(self.strn(
            pmt.ellipse_incial['sma']
            ))
        self.ellipticidadLineEdit.setText(self.strn(
            pmt.ellipse_incial['ellip']
            ))
        self.positionAngleLineEdit.setText(self.strn(
            pmt.ellipse_incial['pa']
            ))
        
        self.nclipLineEdit_2.setText(self.strn(
            pmt.fit_ell_par_0['nclip']
            ))
        self.sclipLineEdit_2.setText(self.strn(
            pmt.fit_ell_par_0['sclip']
            ))
        self.fflagLineEdit_2.setText(self.strn(
            pmt.fit_ell_par_0['fflag']
            ))
        self.converLineEdit_2.setText(self.strn(
            pmt.fit_ell_par_0['conver']
            ))
        self.minsmaLineEdit_2.setText(self.strn(
            pmt.fit_ell_par_0['minsma']
            ))
        self.maxsmaLineEdit_2.setText(
            self.strn(pmt.fit_ell_par_0['maxs']))
        self.intmodeComboBox_2.setCurrentIndex(
            intgm.index(pmt.fit_ell_par['integrmode']))       
        self.stepLineEdit_3.setText(self.strn(
            pmt.fit_ell_par_0['step0']
            ))
        self.fixpar_2.setChecked(
            pmt.fit_ell_par_0['fix']
            )
        self.cutLineEdit_2.setText(self.strn(
            pmt.fit_ell_par_0['cut']
            ))
        self.stepLineEdit_4.setText(self.strn(
            pmt.fit_ell_par_0['step1']
            ))
        
        self.x0LineEdit_2.setText(self.strn(
            pmt.ellipse_incial_0['x0']
            ))
        self.y0LineEdit_2.setText(self.strn(
            pmt.ellipse_incial_0['y0']
            ))
        self.smaLineEdit_2.setText(self.strn(
            pmt.ellipse_incial_0['sma']
            ))
        self.ellipticidadLineEdit_2.setText(self.strn(
            pmt.ellipse_incial_0['ellip']
            ))
        self.positionAngleLineEdit_2.setText(self.strn(
            pmt.ellipse_incial_0['pa']
            ))        
        
        
        self.nthrLineEdit.setText(self.strn(
            pmt.mask['nthr'])
            )
        self.fwhmLineEdit.setText(self.strn(
            pmt.mask['fwhm']
            ))
        self.sharpLineEdit.setText(self.strn(
            pmt.mask['sharp']
            ))
        self.roundlimLineEdit.setText(self.strn(
            pmt.mask['roundlim']
            ))
        self.thresholdLineEdit.setText(self.strn(
            pmt.mask['threshold']
            ))
        
        self.graficarParMetrosIsofotalesCheckBox.setChecked(
            pmt.plots['param_plot']
            )
        self.graficarPerfilDeBrilloCheckBox.setChecked(
           pmt.plots['mu_plot']
            )
        self.usarRadioEquivalenteCheckBox.setChecked(
            pmt.plots['req']
            )
        self.lMiteHorizontalLineEdit.setText(self.strn(
            pmt.plots['n_par']
            ))
        self.lMiteHorizontalLineEdit_2.setText(self.strn(
            pmt.plots['n_mu']
            ))
        self.escalaLineEdit.setText(self.strn(
            pmt.plots['E']
            ))
        self.tiempoDeExposiciNLineEdit.setText(self.strn(
            pmt.plots['texp']
            ))
        self.puntoCeroDeLaMagnitudLineEdit.setText(self.strn(
            pmt.plots['mu0']
            ))
        
        if pmt.plots['arcmin']:
            self.unidadDeAbscisaComboBox.setCurrentIndex(unit.index('arcmin'))
        else:
           self.unidadDeAbscisaComboBox.setCurrentIndex(unit.index('arcsec'))
        
        self.checkBox_save_isolist.setChecked(
            pmt.guardar['save_iso']
            )
        self.line_edir_archivo_isolist.setText(
            self.strn(pmt.fname['out']['table']['path'])+'/'+
            self.strn(pmt.fname['out']['table']['name']
            ))
        
        self.checkBox_save_residue.setChecked(
            pmt.guardar['residue']
            )
        self.lineEdit_save_residue.setText(
            self.strn(pmt.fname['out']['residue']['path'])+'/'+
            self.strn(pmt.fname['out']['residue']['name']
            ))
        
        self.modoComboBox.setCurrentIndex(
            mode.index( pmt.bkg['mode'] ))
        
        self.valorLineEdit.setText(self.strn(pmt.bkg['bkg']))
            
        
        
    def replace_all(self,text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text
    def  strn(self,x):
        if x==None:
            y=''
        if type(x)==str: 
            y=x
        else:
            y=str(x)
        return y 
    
    def tst(self,x):
        if x=='' or x=='None':
            y=None
        else:
            y=x
        return(y)
    
    def nmb(self,x):
        if x=='' or x=='None':
            y=None
        else:
            try:    
                y=int(x)
            except ValueError:
                y=float(x)
        return y
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

