import RPi.GPIO as io


io.setmode(io.BCM)
io.setwarnings(False)


class Motor():
    def __init__(self, in1, in2, enable, default_power=50):
        self.in1 = in1
        self.in2 = in2
        self.enable = enable
        self.default_power = default_power
        io.setup(in1, io.OUT)
        io.setup(in2, io.OUT)
        io.setup(enable, io.OUT)
        self.power = io.PWM(self.enable, 0.5)
        self.power.start(self.default_power)
        self.stop()

    def _clip_power(self, power):
        if power < 0:
            return 0
        if power > 100:
            return 100
        return power

    def forward(self, power=None):
        io.output(self.in1, False)
        io.output(self.in2, True)
        self.power.ChangeDutyCycle(self._clip_power(power if power else self.default_power))

    def stop(self):
        io.output(self.in1, False)
        io.output(self.in2, False)

    def backward(self, power=None):
        io.output(self.in1, True)
        io.output(self.in2, False)
        self.power.ChangeDutyCycle(self._clip_power(power if power else self.default_power))
