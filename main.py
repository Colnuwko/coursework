import sys
from PyQt5.QtWidgets import QMessageBox, QAction, QLabel, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium 
import io
from geopy.geocoders import Nominatim
import osmnx as ox
import clipboard
from folium.plugins import MousePosition


        
class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1255, 1020)
        MainWindow.setToolTipDuration(-3)
        MainWindow.setStyleSheet("border-image: url(\"coursework\\map.png\") 0 0 0 0 stretch stretch\n"
    "")
        MainWindow.setDocumentMode(False)
        
        self.mode = None
        self.city = None
        self.graph = None
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 481))
        self.groupBox.setObjectName("groupBox")
        self.from_label_text = QtWidgets.QTextEdit(self.groupBox)
        self.from_label_text.setGeometry(QtCore.QRect(70, 30, 211, 31))
        self.from_label_text.setObjectName("from_label_text")
        self.to_label_text = QtWidgets.QTextEdit(self.groupBox)
        self.to_label_text.setGeometry(QtCore.QRect(70, 80, 211, 31))
        self.to_label_text.setObjectName("to_label_text")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 71, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 71, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(70, 160, 71, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(70, 210, 71, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(150, 30, 131, 31))
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 80, 131, 31))
        self.textEdit_2.setAcceptDrops(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 150, 131, 31))
        self.textEdit_3.setAcceptDrops(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_4.setGeometry(QtCore.QRect(150, 200, 131, 31))
        self.textEdit_4.setAcceptDrops(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.fromm = QtWidgets.QLabel(self.groupBox)
        self.fromm.setGeometry(QtCore.QRect(20, 40, 61, 20))
        self.fromm.setObjectName("from")
        self.to = QtWidgets.QLabel(self.groupBox)
        self.to.setGeometry(QtCore.QRect(20, 90, 61, 21))
        self.to.setObjectName("to")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 440, 281, 23))
        self.pushButton.setObjectName("pushButton")
        self.radio_b_time = QtWidgets.QRadioButton(self.groupBox)
        self.radio_b_time.setGeometry(QtCore.QRect(50, 300, 87, 17))
        self.radio_b_time.setObjectName("radio_b_time")
        self.select_type_group = QtWidgets.QButtonGroup(MainWindow)
        self.select_type_group.setObjectName("select_type_group")
        self.select_type_group.addButton(self.radio_b_time)
        self.radio_b_length = QtWidgets.QRadioButton(self.groupBox)
        self.radio_b_length.setGeometry(QtCore.QRect(150, 300, 111, 17))
        self.radio_b_length.setObjectName("radio_b_length")
        self.select_type_group.addButton(self.radio_b_length)
        self.short_type = QtWidgets.QLabel(self.groupBox)
        self.short_type.setGeometry(QtCore.QRect(20, 270, 261, 20))
        self.short_type.setAlignment(QtCore.Qt.AlignCenter)
        self.short_type.setObjectName("short_type")
        self.radio_search = QtWidgets.QRadioButton(self.groupBox)
        self.radio_search.setGeometry(QtCore.QRect(50, 390, 87, 17))
        self.radio_search.setObjectName("radio_search")
        self.select_type_geodata_group = QtWidgets.QButtonGroup(MainWindow)
        self.select_type_geodata_group.setObjectName("select_type_geodata_group")
        self.select_type_geodata_group.addButton(self.radio_search)
        self.radio_point = QtWidgets.QRadioButton(self.groupBox)
        self.radio_point.setGeometry(QtCore.QRect(150, 390, 111, 17))
        self.radio_point.setObjectName("radio_point")
        self.select_type_geodata_group.addButton(self.radio_point)
        self.geo_data_type = QtWidgets.QLabel(self.groupBox)
        self.geo_data_type.setGeometry(QtCore.QRect(20, 360, 261, 20))
        self.geo_data_type.setAlignment(QtCore.Qt.AlignCenter)
        self.geo_data_type.setObjectName("geo_data_type")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 500, 301, 491))
        self.groupBox_2.setObjectName("groupBox_2")
        self.select_city = QtWidgets.QLabel(self.groupBox_2)
        self.select_city.setGeometry(QtCore.QRect(17, 20, 271, 20))
        self.select_city.setAlignment(QtCore.Qt.AlignCenter)
        self.select_city.setObjectName("select_city")
        self.list_of_cities = QtWidgets.QListWidget(self.groupBox_2)
        self.list_of_cities.setGeometry(QtCore.QRect(20, 90, 261, 111))
        self.list_of_cities.setObjectName("list_of_cities")    
        self.list_of_cities.addItems(["Samara", "Moscow", "Saint Petersburg", "Volgograd", "Kazan"])
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 290, 71, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.select_mode_group = QtWidgets.QButtonGroup(MainWindow)
        self.select_mode_group.setObjectName("select_mode_group")
        self.select_mode_group.addButton(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 290, 81, 17))
        self.radioButton.setObjectName("radioButton")
        self.select_mode_group.addButton(self.radioButton)
        self.venchile_mode = QtWidgets.QLabel(self.groupBox_2)
        self.venchile_mode.setGeometry(QtCore.QRect(20, 260, 261, 20))
        self.venchile_mode.setAutoFillBackground(False)
        self.venchile_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.venchile_mode.setObjectName("venchile_mode")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 290, 101, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.select_mode_group.addButton(self.radioButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 450, 271, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 310, 271, 131))
        self.label.setStyleSheet("font: 63 20pt \"MS Shell Dlg 2\";")
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(339, 19, 1551, 991))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.view = QWebEngineView()
        self.horizontalLayout.addWidget(self.view, stretch=1)
        self.first_set()

        
    def first_set(self, coord = [53.211936, 50.177311]):
        self.m = folium.Map(
            location=coord, zoom_start=13
        )
        data = io.BytesIO()
        
        popup1 = folium.LatLngPopup()
        # self.m.add_child(folium.ClickForLatLng(format_str='"[" + lat + "," + lng + "]"', alert=True))
        # print(clipboard.paste())
        # print("Latitude of Popup: ", popup1.)   
        self.m.add_child(popup1)
        
        # self.m.add_child(folium.ClickForMarker())
        

        self.m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())
    

        
    def get_coord(self, place: str):
        ox.config(log_console=True, use_cache=True)
        locator = Nominatim(user_agent = "myapp")
        temp = locator.geocode(place).point
        self.coord = [temp.latitude, temp.longitude]
    
    
    def click_input_search(self):
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.hide()
        self.from_label_text.show()
        self.to_label_text.show()
        self.to.move(20, 90)
        
    def click_input_point(self):
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.label_5.show()
        self.textEdit.show()
        self.textEdit_2.show()
        self.textEdit_3.show()
        self.textEdit_4.show()
        self.from_label_text.hide()
        self.to_label_text.hide()
        self.to.move(20, 160)
    def button_click_mode_drive(self):
        self.mode = "drive"
        
    def button_click_mode_bike(self):
        self.mode = "bike"
        
    def button_click_mode_walk(self):
        self.mode = "walk"
        
    def select_city_click(self, item):
        self.city = item.text()
        
    def button_load_data_click(self):
        if self.mode == None:
            QMessageBox.about(MainWindow, "Внимание", "Вы не задали тип перемещения")
        else:
            if self.city == None:
                 QMessageBox.about(MainWindow, "Внимание", "Вы не задали город")
            else: 
                
                self.get_coord(str(self.city)+","+ str("Russia"))
                self.first_set(self.coord)
                QMessageBox.about(MainWindow, "Внимание", "Загрузка графа может занять некоторое время, пожалуйста подождите")
                self.set_graph_city(str(self.city)+","+ str("Russia"), self.mode)
    
    def set_graph_city(self, city: str, mode: str):
        self.graph = ox.graph_from_place(city, network_type = mode)
        QMessageBox.about(MainWindow, "Успех", "Загрузка данных прошла успешно")
    
    
    def set_path_in_map(self, shortest_path):
        pass

    def get_shortest_path(self):
        print(1)
    
    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle("MainWindow")
        self.groupBox.setTitle("main_box")
        self.fromm.setText("Откуда")
        self.to.setText("Куда")
        self.pushButton.setText("Проложить маршрут")
        self.radio_b_time.setText("По времени")
        self.radio_b_length.setText("По расстоянию")
        self.short_type.setText("Расчет оптимальног пути")
        self.radio_search.setText("Поиск")
        self.radio_point.setText("Точки на карте")
        self.geo_data_type.setText("Как укажете данные?")
        self.groupBox_2.setTitle("Select_map")
        self.select_city.setText("Выберите Город")
        self.label_2.setText("latitude")
        self.label_3.setText("longitude")
        self.label_4.setText("latitude")
        self.label_5.setText("longitude")
        
        self.radioButton_2.setText("Пешком")
        self.radioButton.setText("На машине")
        self.venchile_mode.setText("Как буде добираться?")
        self.radioButton_3.setText("На велосипеде")
        self.pushButton_2.setText("Подгрузить данны для выбранного города")
        self.label.setText("Внимание Подгрузка данных обязательна!")
        
        self.pushButton_2.clicked.connect(self.button_load_data_click)
        self.radioButton.clicked.connect(self.button_click_mode_drive)
        self.radioButton_2.clicked.connect(self.button_click_mode_walk)
        self.radioButton_3.clicked.connect(self.button_click_mode_bike)
        self.list_of_cities.itemClicked.connect(self.select_city_click)
        self.radio_search.clicked.connect(self.click_input_search)
        self.radio_point.clicked.connect(self.click_input_point)
        self.pushButton.clicked.connect(self.get_shortest_path)
        self.radio_search.click()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
