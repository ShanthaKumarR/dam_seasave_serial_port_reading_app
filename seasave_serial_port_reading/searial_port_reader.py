import serial.tools.list_ports

class PortReading:
    def __init__(self, ):
        self.ports = serial.tools.list_ports.comports()
        self.serial_port = serial.Serial()
        self.get_connected_ports()

    def get_connected_ports(self):
        connected_ports = list()
        for port in self.ports:
            port_list = str(port).strip().split(' ')
            connected_ports.append(port_list[0])
        return connected_ports
                           
    def start_streaming(self):
        try:
            packet = self.serial_port.readline()
            return packet.decode()
        except serial.SerialTimeoutException:
            return 'time_out'
        except serial.serialutil.SerialException:
            return 'invlaid port'