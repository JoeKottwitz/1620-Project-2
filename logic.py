from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from gui import *
from television import Television


class Logic(QMainWindow, Ui_MainWindow):
    '''
    Class to provide functionality to the TV remote gui
    '''

    def __init__(self) -> None:
        '''
        Method to initialize the gui and handle button inputs
        '''
        super().__init__()
        self.setupUi(self)

        self.cbs = QPixmap('logo_cbs.png')
        self.espn = QPixmap('logo_espn.png')
        self.nbc = QPixmap('logo_nbc.png')
        self.pbs = QPixmap('logo_pbsKids.png')

        self.tv = Television()

        self.button_power.clicked.connect(lambda: self.submit_power())
        self.button_mute.clicked.connect(lambda: self.submit_mute())
        self.button_volume_up.clicked.connect(lambda: self.submit_volume_up())
        self.button_volume_down.clicked.connect(lambda: self.submit_volume_down())
        self.button_channel_up.clicked.connect(lambda: self.submit_channel_up())
        self.button_channel_down.clicked.connect(lambda: self.submit_channel_down())

    def submit_power(self) -> None:
        '''
        Method to turn on/off the tv remote in the gui
        '''
        self.tv.power()

        if self.tv.check_power():
            self.set_logo(self.tv.check_channel())
            if not self.tv.check_mute():
                self.progressBar_volume.setValue(self.tv.check_volume())
            self.progressBar_channel.setValue(self.tv.check_channel())
        else:
            self.scene.clear()
            self.label_channel_name.setText('')
            self.progressBar_volume.setValue(0)
            self.progressBar_channel.setValue(0)

        power_status = self.tv.check_power()
        self.button_mute.setEnabled(power_status)
        if not self.tv.check_mute():
            self.button_volume_up.setEnabled(power_status)
            self.button_volume_down.setEnabled(power_status)
        self.button_channel_up.setEnabled(power_status)
        self.button_channel_down.setEnabled(power_status)

    def submit_mute(self) -> None:
        '''
        Method to mute the volume in the gui by
        enabling/disabling the volume buttons
        '''
        self.tv.mute()
        if self.tv.check_mute():
            self.button_volume_up.setEnabled(False)
            self.button_volume_down.setEnabled(False)
            self.progressBar_volume.setValue(0)
        else:
            self.button_volume_up.setEnabled(True)
            self.button_volume_down.setEnabled(True)
            self.progressBar_volume.setValue(self.tv.check_volume())

    def submit_volume_up(self) -> None:
        '''
        Method to turn up the volume 1 in the gui
        '''
        if not self.tv.check_mute():
            self.tv.volume_up()
            volume_level = self.tv.check_volume()
            self.progressBar_volume.setValue(volume_level)

    def submit_volume_down(self) -> None:
        '''
        Method to turn down the volume 1 in the gui
        '''
        if not self.tv.check_mute():
            self.tv.volume_down()
            volume_level = self.tv.check_volume()
            self.progressBar_volume.setValue(volume_level)

    def submit_channel_up(self) -> None:
        '''
        Method to switch to the next channel in the gui
        '''
        self.clear_logo(self.tv.check_channel())

        self.tv.channel_up()
        channel_number = self.tv.check_channel()
        self.progressBar_channel.setValue(channel_number)

        self.set_logo(self.tv.check_channel())

    def submit_channel_down(self) -> None:
        '''
        Method to switch to the previous channel in the gui
        '''
        self.clear_logo(self.tv.check_channel())

        self.tv.channel_down()
        channel_number = self.tv.check_channel()
        self.progressBar_channel.setValue(channel_number)

        self.set_logo(self.tv.check_channel())

    def set_logo(self, channel) -> None:
        '''
        Method to change to the correct channel's
        logo picture and title
        :param channel: Number of channel being changed to
        '''
        self.scene = QGraphicsScene()

        if channel == 0:
            self.scene.addItem(QGraphicsPixmapItem(self.cbs))
            self.graphic_channel_logo.setScene(self.scene)
            self.graphic_channel_logo.fitInView(self.scene.sceneRect())
            self.graphic_channel_logo.show()

            self.label_channel_name.setText('CBS')
        elif channel == 1:
            self.scene.addItem(QGraphicsPixmapItem(self.espn))
            self.graphic_channel_logo.setScene(self.scene)
            self.graphic_channel_logo.fitInView(self.scene.sceneRect())
            self.graphic_channel_logo.show()

            self.label_channel_name.setText('ESPN')
        elif channel == 2:
            self.scene.addItem(QGraphicsPixmapItem(self.nbc))
            self.graphic_channel_logo.setScene(self.scene)
            self.graphic_channel_logo.fitInView(self.scene.sceneRect())
            self.graphic_channel_logo.show()

            self.label_channel_name.setText('NBC')
        elif channel == 3:
            self.scene.addItem(QGraphicsPixmapItem(self.pbs))
            self.graphic_channel_logo.setScene(self.scene)
            self.graphic_channel_logo.fitInView(self.scene.sceneRect())
            self.graphic_channel_logo.show()

            self.label_channel_name.setText('PBS Kids')

    def clear_logo(self, channel) -> None:
        '''
        Method to clear the logo and delete the
        scene so a new logo can be placed in
        :param channel: Number of channel be changed from
        '''
        self.scene.clear()
        if channel == 0:
            self.scene.removeItem(QGraphicsPixmapItem(self.cbs))
            del self.scene
        elif channel == 1:
            self.scene.removeItem(QGraphicsPixmapItem(self.espn))
            del self.scene
        elif channel == 2:
            self.scene.removeItem(QGraphicsPixmapItem(self.nbc))
            del self.scene
        elif channel == 3:
            self.scene.removeItem(QGraphicsPixmapItem(self.pbs))
            del self.scene