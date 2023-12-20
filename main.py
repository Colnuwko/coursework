import sys
import io
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.tr("MAP PROJECT"))
        self.setMinimumSize(800, 600)
        self.buttonUI()
    
    def button_short_path_click(self):
        self.m = folium.Map(
            location=[53.211936, 50.177311], zoom_start=13
        )

        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())

        print(1414234)
    
    def buttonUI(self):
        self.shortPathButton = QPushButton("Find shortest path")
        self.button2 = QPushButton("Another path")
        self.button_mode_walk = QPushButton("Пешком")
        self.button_mode_drive = QPushButton("Машина")
        self.button_mode_bike = QPushButton("Велосипед")
        self.button_mode_time = QPushButton("Время")
        self.button_mode_length = QPushButton("Расстояние")
        self.button_mode_bike.setFixedSize(50, 50)
        self.button_mode_drive.setFixedSize(50, 50)
        self.button_mode_walk.setFixedSize(50, 50)
        self.button_mode_length.setFixedSize(50, 50)
        self.button_mode_time.setFixedSize(50, 50)

        self.shortPathButton.setFixedSize(120, 50)
        self.button2.setFixedSize(120, 50)
        self.view = QWebEngineView()
        self.view.setContentsMargins(20, 20, 5, 5)

        self.shortPathButton.clicked.connect(self.button_short_path_click)
        
        
        self.central_widget = QWidget()
        # self.central_widget.setStyleSheet("border: 1px solid black;") 
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("border: 1px solid black;") 
        self.map = QHBoxLayout(self.central_widget)
        self.select_mode = QWidget()
        self.select_type = QWidget()        
        self.select_mode_container = QHBoxLayout(self.select_mode)
        self.select_mode_container.addWidget(self.button_mode_walk)
        self.select_mode_container.addWidget(self.button_mode_bike)
        self.select_mode_container.addWidget(self.button_mode_drive)
        self.select_type_container = QHBoxLayout(self.select_type)
        self.select_type_container.addWidget(self.button_mode_length)
        # self.select_type_container.addWidget(self.button_mode_time)

        self.button_container = QWidget()
        self.vlay = QVBoxLayout(self.button_container)
        self.vlay.setSpacing(20)
        self.vlay.addStretch()
        self.vlay.addWidget(self.shortPathButton)
        self.vlay.addWidget(self.button2)
        self.vlay.addStretch()
        self.vlay.addWidget(self.button_mode_length)
        self.map.addWidget(self.button_container)
        self.map.addWidget(self.view, stretch=1)

        self.m = folium.Map(
            location=[45.5236, -122.6750], zoom_start=13
        )

        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())