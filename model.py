from view.view import View
import sys
from controller.controller import SerialPortReadingController
from seasave_serial_port_reading.searial_port_reader import PortReading

class SerialPortReading:
    def __init__(self):
        self.view = View()
        port_obj = PortReading()
        controls = self.view.ui_controls
        self.control_obj = SerialPortReadingController(controls, port_obj, self.view.ui.baud_rate, self.view.ui.port_number, self.view.ui.stopstart, self.view.ui.display_table)
        self.view.start_app()

if __name__ == '__main__':
     app = SerialPortReading()