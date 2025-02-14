import time
import board
import adafruit_bme680


class Sensor:
    def __init__(self,sea_pressure=1013.25, temp_offset=-5):
        i2c = board.I2C()

        self.Sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
        self.sea_pressure = sea_pressure
        self.temp_offset = temp_offset

    def setPressure(self,new_pressure):
        self.Sensor.sea_pressure = new_pressure
        self.Sensor.sea_level_pressure = new_pressure

    def getData(self):
        #returns temp, pressure, altitude, gas, huidity
        return (
            self.Sensor.temperature + self.temp_offset,
            self.Sensor.pressure,
            self.Sensor.altitude,
            self.Sensor.gas,
            self.Sensor.relative_humidity
        )