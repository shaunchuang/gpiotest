
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D17, use_pulseio=False)

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C Humidity: {}%".format(temperature_f, temperature_c, humidity))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2)



