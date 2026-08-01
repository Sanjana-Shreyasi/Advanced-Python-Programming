class WeatherStation:
    def __init__(self):
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)

    def remove_device(self, device):
        self._devices.remove(device)

    def broadcast(self, temperature):
        for device in self._devices:
            device.show(temperature)


class Device:
    def show(self, temperature):
        print(f"Temperature updated: {temperature}")


# Usage
station = WeatherStation()
device1 = Device()
device2 = Device()

station.add_device(device1)
station.add_device(device2)

station.broadcast("32°C")

# Output 
'''Temperature updated: 32°C
Temperature updated: 32°C'''