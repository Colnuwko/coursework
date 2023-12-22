import sys
from PyQt5.QtWidgets import QMessageBox, QAction, QLabel, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium 
import io
from geopy.geocoders import Nominatim
import osmnx as ox
from osmnx import routing

import algorithms
sys.stdout.encoding
sys.stdout.reconfigure(encoding='utf-8')
ox.config(log_console=True, use_cache=True)
locator = Nominatim(user_agent = "myapp")
        
class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(1280, 1080)
        MainWindow.setToolTipDuration(-3)
        MainWindow.setStyleSheet("border-image: url(\"coursework\\map.png\") 0 0 0 0 stretch stretch\n"
    "")
        self.city = None
        self.graph = None
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 481))
        self.groupBox.setObjectName("groupBox")
        self.from_label_text = QtWidgets.QLineEdit(self.groupBox)
        self.from_label_text.setGeometry(QtCore.QRect(70, 30, 211, 31))
        self.from_label_text.setObjectName("from_label_text")
        self.to_label_text = QtWidgets.QLineEdit(self.groupBox)
        self.to_label_text.setGeometry(QtCore.QRect(70, 80, 211, 31))
        self.to_label_text.setObjectName("to_label_text")
        self.latitude_from = QtWidgets.QLabel(self.groupBox)
        self.latitude_from.setGeometry(QtCore.QRect(70, 40, 71, 21))
        self.latitude_from.setAlignment(QtCore.Qt.AlignCenter)
        self.latitude_from.setObjectName("latitude_to")
        self.longitude_from = QtWidgets.QLabel(self.groupBox)
        self.longitude_from.setGeometry(QtCore.QRect(70, 90, 71, 21))
        self.longitude_from.setAlignment(QtCore.Qt.AlignCenter)
        self.longitude_from.setObjectName("longitude_from")
        self.latitude_to = QtWidgets.QLabel(self.groupBox)
        self.latitude_to.setGeometry(QtCore.QRect(70, 140, 71, 21))
        self.latitude_to.setAlignment(QtCore.Qt.AlignCenter)
        self.latitude_to.setObjectName("latitude_to")
        self.longitude_to = QtWidgets.QLabel(self.groupBox)
        self.longitude_to.setGeometry(QtCore.QRect(70, 190, 71, 21))
        self.longitude_to.setAlignment(QtCore.Qt.AlignCenter)
        self.longitude_to.setObjectName("longitude_to")
        self.calculated_res = QtWidgets.QLabel(self.groupBox)
        self.calculated_res.setGeometry(QtCore.QRect(0, 220, 300, 71))
        self.calculated_res.setStyleSheet("border: 1px solid black;")
        self.calculated_res.setAlignment(QtCore.Qt.AlignCenter)
        self.calculated_res.setObjectName("result data")
        self.calculated_res.setWordWrap(True)
        self.input_latitude_from = QtWidgets.QLineEdit(self.groupBox)
        self.input_latitude_from.setGeometry(QtCore.QRect(150, 30, 131, 31))
        self.input_latitude_from.setAcceptDrops(True)
        self.input_latitude_from.setObjectName("input_latitude_from")
        self.input_longitude_from = QtWidgets.QLineEdit(self.groupBox)
        self.input_longitude_from.setGeometry(QtCore.QRect(150, 80, 131, 31))
        self.input_longitude_from.setAcceptDrops(True)
        self.input_longitude_from.setObjectName("input_longitude_from")
        self.input_latitude_to = QtWidgets.QLineEdit(self.groupBox)
        self.input_latitude_to.setGeometry(QtCore.QRect(150, 130, 131, 31))
        self.input_latitude_to.setAcceptDrops(True)
        self.input_latitude_to.setObjectName("input_latitude_to")
        self.input_longitude_to = QtWidgets.QLineEdit(self.groupBox)
        self.input_longitude_to.setGeometry(QtCore.QRect(150, 180, 131, 31))
        self.input_longitude_to.setAcceptDrops(True)
        self.input_longitude_to.setObjectName("input_longitude_to")
        self.from_info_text = QtWidgets.QLabel(self.groupBox)
        self.from_info_text.setGeometry(QtCore.QRect(20, 40, 60, 20))
        self.from_info_text.setObjectName("from")
        self.to_info_text = QtWidgets.QLabel(self.groupBox)
        self.to_info_text.setGeometry(QtCore.QRect(20, 70, 60, 20))
        self.to_info_text.setObjectName("to_info_text")
        self.route_display_button = QtWidgets.QPushButton(self.groupBox)
        self.route_display_button.setGeometry(QtCore.QRect(10, 440, 281, 23))
        self.route_display_button.setObjectName("route_display_button")
        self.radio_button_time = QtWidgets.QRadioButton(self.groupBox)
        self.radio_button_time.setGeometry(QtCore.QRect(50, 320, 87, 17))
        self.radio_button_time.setObjectName("radio_button_time")
        self.select_type_group = QtWidgets.QButtonGroup(MainWindow)
        self.select_type_group.setObjectName("select_type_group")
        self.select_type_group.addButton(self.radio_button_time)
        self.radio_button_length = QtWidgets.QRadioButton(self.groupBox)
        self.radio_button_length.setGeometry(QtCore.QRect(150, 320, 111, 17))
        self.radio_button_length.setObjectName("radio_button_length")
        self.select_type_group.addButton(self.radio_button_length)
        self.info_ab_short_type = QtWidgets.QLabel(self.groupBox)
        self.info_ab_short_type.setGeometry(QtCore.QRect(20, 290, 261, 20))
        self.info_ab_short_type.setAlignment(QtCore.Qt.AlignCenter)
        self.info_ab_short_type.setObjectName("info_ab_short_type")
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
        self.list_of_cities.addItems(["Самара", "Москва", "Санкт-петербург", "Волгоград", "Казань"])
        self.button_select_walk_mode = QtWidgets.QRadioButton(self.groupBox_2)
        self.button_select_walk_mode.setGeometry(QtCore.QRect(220, 290, 71, 17))
        self.button_select_walk_mode.setObjectName("button_select_walk_mode")
        self.select_mode_group = QtWidgets.QButtonGroup(MainWindow)
        self.select_mode_group.setObjectName("select_mode_group")
        self.select_mode_group.addButton(self.button_select_walk_mode)
        self.button_select_drive_mode = QtWidgets.QRadioButton(self.groupBox_2)
        self.button_select_drive_mode.setGeometry(QtCore.QRect(20, 290, 81, 17))
        self.button_select_drive_mode.setObjectName("button_select_drive_mode")
        self.select_mode_group.addButton(self.button_select_drive_mode)
        self.info_of_venchile_mode = QtWidgets.QLabel(self.groupBox_2)
        self.info_of_venchile_mode.setGeometry(QtCore.QRect(20, 260, 261, 20))
        self.info_of_venchile_mode.setAutoFillBackground(False)
        self.info_of_venchile_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.info_of_venchile_mode.setObjectName("info_of_venchile_mode")
        self.button_select_bike_mode = QtWidgets.QRadioButton(self.groupBox_2)
        self.button_select_bike_mode.setGeometry(QtCore.QRect(110, 290, 101, 17))
        self.button_select_bike_mode.setObjectName("button_select_bike_mode")
        self.select_mode_group.addButton(self.button_select_bike_mode)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 330, 271, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 370, 271, 131))
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

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle("я карта я карта")
        self.groupBox.setTitle("Основное меню")
        self.from_info_text.setText("Откуда")
        self.to_info_text.setText("Куда")
        self.route_display_button.setText("Проложить маршрут")
        self.radio_button_time.setText("По времени")
        self.radio_button_length.setText("По расстоянию")
        self.info_ab_short_type.setText("Расчет оптимального пути")
        self.radio_search.setText("Поиск")
        self.radio_point.setText("Точки на карте")
        self.geo_data_type.setText("Как укажете данные?")
        self.groupBox_2.setTitle("Выбор карты")
        self.select_city.setText("Выберите Город")
        self.latitude_to.setText("latitude")
        self.longitude_from.setText("longitude")
        self.latitude_to.setText("latitude")
        self.longitude_to.setText("longitude")
        self.button_select_walk_mode.setText("Пешком")
        self.button_select_drive_mode.setText("На машине")
        self.info_of_venchile_mode.setText("Как будете добираться?")
        self.button_select_bike_mode.setText("На велосипеде")
        self.pushButton_2.setText("Загрузить данные для выбранного города")
        self.label.setText("Внимание Загрузка данных обязательна!")
        
        
        self.pushButton_2.clicked.connect(self.button_load_data_click)
        self.button_select_drive_mode.clicked.connect(self.button_click_mode_drive)
        self.button_select_walk_mode.clicked.connect(self.button_click_mode_walk)
        self.button_select_bike_mode.clicked.connect(self.button_click_mode_bike)
        self.list_of_cities.itemClicked.connect(self.select_city_click)
        self.radio_search.clicked.connect(self.click_input_search)
        self.radio_point.clicked.connect(self.click_input_point)
        self.route_display_button.clicked.connect(self.get_shortest_path)
        self.radio_button_time.clicked.connect(self.butto_click_type_time)
        self.radio_button_length.clicked.connect(self.butto_click_type_length)
        self.radio_button_time.click()
        self.radio_search.click()
        self.button_select_drive_mode.click()
        
    
    def first_set(self,coord = [53.211936, 50.177311]):
        data = algorithms.first_set(coord)
        self.view.setHtml(data.getvalue().decode())
        
        
    def button_load_data_click(self):
        if self.city == None:
                QMessageBox.about(MainWindow, "Внимание", "Вы не задали город")
        else: 
            self.coord = algorithms.get_coord(str(self.city)+","+ str("Russia"))
            self.first_set(self.coord)
            QMessageBox.about(MainWindow, "Внимание", "Загрузка графа может занять некоторое время, пожалуйста подождите")
            self.set_graph_city(str(self.city)+","+ str("Russia"))
            self.load_city = self.city
    
    def get_shortest_path(self):
        if self.graph != None: 
            if self.typ == "point":
                start_coord = [float(self.input_latitude_from.text()), float(self.input_longitude_from.text())]
                end_coord = [float(self.input_latitude_to.text()), float(self.input_longitude_to.text())]
                self.start_loc = locator.reverse(start_coord)
                self.end_loc = locator.reverse(end_coord)
            else:
                self.start_loc = self.load_city + ", " + self.from_label_text.text()
                self.end_loc = self.load_city + ", " + self.to_label_text.text()
                start_coord = algorithms.get_coord(self.start_loc)
                end_coord = algorithms.get_coord(self.end_loc)
                
            if start_coord != None and end_coord != None:   
                orig_node = ox.nearest_nodes(self.graph, start_coord[1], start_coord[0])
                dest_node = ox.nearest_nodes(self.graph, end_coord[1], end_coord[0])
                shortest_route = routing.shortest_path(self.graph, orig_node, dest_node, weight=self.type)
                self.set_path_in_map(shortest_route, start_coord, end_coord)
            else:  QMessageBox.about(MainWindow, "Внимание", "Адресс введен неверно")
        else: QMessageBox.about(MainWindow, "Внимание", "Вы не загрузили данные города")
    
    
    def set_path_in_map(self, shortest_route, start_coord, end_coord):
        print("set start in map")
        start_marker = folium.Marker(
            location = start_coord,
            popup = self.start_loc,
            icon = folium.Icon(color='green'))

        end_marker = folium.Marker(
            location = end_coord,
            popup = self.end_loc,
            icon = folium.Icon(color='red'))
        self.shortest_route_map = ox.plot_route_folium(self.graph, shortest_route, 
                                          tiles='openstreetmap')
        
        start_marker.add_to(self.shortest_route_map)
        end_marker.add_to(self.shortest_route_map)
        data = io.BytesIO()
        popup1 = folium.LatLngPopup()
        
        self.shortest_route_map.add_child(popup1)
        self.shortest_route_map.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())
        
        text = algorithms.calculating_time_and_length(self.graph, shortest_route)
        self.calculated_res.setText(text)
        
    
    
    def click_input_search(self):
        self.typ = "search"
        self.latitude_to.hide()
        self.longitude_from.hide()
        self.latitude_to.hide()
        self.longitude_to.hide()
        self.input_latitude_from.hide()
        self.input_longitude_from.hide()
        self.input_latitude_to.hide()
        self.input_longitude_to.hide()
        self.from_label_text.show()
        self.to_label_text.show()
        self.to_info_text.move(20, 90)
        
    def click_input_point(self):
        self.typ = "point"
        self.latitude_to.show()
        self.longitude_from.show()
        self.latitude_to.show()
        self.longitude_to.show()
        self.input_latitude_from.show()
        self.input_longitude_from.show()
        self.input_latitude_to.show()
        self.input_longitude_to.show()
        self.from_label_text.hide()
        self.to_label_text.hide()
        self.to_info_text.move(20, 160)
        
    def button_click_mode_drive(self):
        self.mode = "drive"
        
    def button_click_mode_bike(self):
        self.mode = "bike"
        
    def button_click_mode_walk(self):
        self.mode = "walk"
        
    def butto_click_type_length(self):
        self.type = "length"
        
    def butto_click_type_time(self):
        self.type = "travel_time"
            
    def select_city_click(self, item):
        self.city = item.text()
        self.label.show()
    
    def set_graph_city(self, city: str):
        self.graph = ox.graph_from_place(city, network_type = self.mode)
        QMessageBox.about(MainWindow, "Успех", "Загрузка данных прошла успешно")
        self.added_graph()
        self.label.hide()

    def added_graph(self):
        list_keys = {
        'secondary': 50, 'primary': 70, 'tertiary': 30, 'secondary_link': 30, 'residential': 20, 'primary_link': 30}
        self.graph = ox.add_edge_speeds(self.graph, list_keys, 50)

        self.graph = ox.add_edge_travel_times(self.graph)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
