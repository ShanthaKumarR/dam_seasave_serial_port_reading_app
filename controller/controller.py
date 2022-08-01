from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QTableWidgetItem
import time
import serial
PARMETER_COLUMN = 0
VALUE_COLUMN = 1

class SerialPortReadingController:
    def __init__(self, controls,port_obj, baud_rate_cb, port_number_cb, start_stop_button, display_table):
        self.controls = controls(self)
        self.port_obj = port_obj
        self.start_stop_button = start_stop_button
        self.port_number_cb = port_number_cb
        self.baud_rate = baud_rate_cb
        self.display_table = display_table
        self.sensor_name = ['Temperature', 'Pressure', 'conductivity', 'salanity']
        [self.display_table.setItem(inx, PARMETER_COLUMN, QTableWidgetItem(sensor_name)) for inx, sensor_name in enumerate(self.sensor_name)]
        '''argunemts: controls - method that instantates the controls of the ui element'''
       
        self.read_data()
        port_list = self.port_obj.get_connected_ports()
        self.port_number_cb.addItems(port_list)
        self.port_number_cb.setCurrentText('COM5')
        
    def on_close_run(self, close_method):
        close_method()
    
    def set_baud_rate(self, baud_rate):
        self.port_obj.start_reading = False
        self.port_obj.baudrate = baud_rate
    
    def read_data(self):
        try:
            self.port_obj.serial_port.open()
        except serial.serialutil.SerialException:
            print('connect the instrument')
        self.data_reading_thread = StreamingThread(self.port_obj.start_streaming)
        self.data_reading_thread.start()
        self.data_reading_thread.data_from_serail_port.connect(self.set_data_to_panel)
        
    def set_data_to_panel(self, data):
        
        if (data != 'invlaid port') and (data != 'No data'):
            data = data.strip().split(' ')
            data = list(filter(None, data))
            [self.display_table.setItem(inx, VALUE_COLUMN, QTableWidgetItem(data)) for inx, data in enumerate(data)]
        elif data == 'No data':
            [self.display_table.setItem(inx, VALUE_COLUMN, QTableWidgetItem('No data')) for inx in range(self.display_table.rowCount())]
        else:
            pass

    def switch_baurd_rate(self, baud_rate):
        try:
            self.data_reading_thread.start_reading= False
            self.port_obj.serial_port.close()
            self.port_obj.serial_port.baudrate = int(baud_rate)
            self.port_obj.serial_port.open()
            self.data_reading_thread.start_reading= True
            self.data_reading_thread.start()
        except serial.serialutil.SerialException:
            print('SerialException')

    def switch_port(self, port_number):
        
        try:
            self.data_reading_thread.start_reading= False
            self.port_obj.serial_port.close()
            self.port_obj.serial_port.port = str(port_number)
            self.port_obj.serial_port.open()
            self.data_reading_thread.start_reading= True
            self.data_reading_thread.start()
        except serial.serialutil.SerialException:
            print('SerialException')
            

    def start_stop_reading_data(self):
        if self.data_reading_thread.start_reading:
            self.data_reading_thread.start_reading= False
            
        elif self.data_reading_thread.start_reading == False:
            self.data_reading_thread.start_reading= True
            self.data_reading_thread.start()
            


class StreamingThread(QThread):
    data_from_serail_port = pyqtSignal(str)

    def __init__(self, thread_function):
        super().__init__()
        self.thread_function = thread_function
        self.start_reading = True

    def run(self):
        try:
            while self.start_reading:
                packet = self.thread_function()
                self.data_from_serail_port.emit(str(packet))
                #time.sleep(0.25)
        except:
            print('no data')