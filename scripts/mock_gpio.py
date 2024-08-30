# scripts/mock_gpio.py

class GPIO:
    BCM = 'BCM'
    IN = 'IN'
    OUT = 'OUT'
    HIGH = 'HIGH'
    LOW = 'LOW'

    @staticmethod
    def setmode(mode):
        print(f"GPIO setmode: {mode}")

    @staticmethod
    def setup(channel, mode):
        print(f"GPIO setup: Channel={channel}, Mode={mode}")

    @staticmethod
    def input(channel):
        print(f"GPIO input: Channel={channel}")
        return GPIO.LOW

    @staticmethod
    def output(channel, state):
        print(f"GPIO output: Channel={channel}, State={state}")

    @staticmethod
    def cleanup():
        print("GPIO cleanup")
