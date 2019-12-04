import time
import RPi.GPIO as io


io.setmode(io.BCM)


class Motor():
    def __init__(self, in1, in2, enable):
        self.in1 = in1
        self.in2 = in2
        self.enable = enable
        io.setup(in1, io.OUT)
        io.setup(in2, io.OUT)
        io.setup(enable, io.OUT)
        self.power = io.PWM(self.enable, 0.5)
        self.power.start(80)

    def _clip_power(self, power):
        if power < 0:
            return 0
        if power > 100:
            return 100
        return power

    def forward(self, power=80):
        io.output(self.in1, False)
        io.output(self.in2, True)
        self.power.ChangeDutyCycle(self._clip_power(power))

    def stop(self):
        io.output(self.in1, False)
        io.output(self.in2, False)

    def backward(self, power=80):
        io.output(self.in1, True)
        io.output(self.in2, False)
        self.power.ChangeDutyCycle(self._clip_power(power))


def main():
    motorsx = Motor(6, 13, 5)
    motordx = Motor(19, 26, 20)

    motorsx.forward()
    time.sleep(2)
    motorsx.stop()
    motordx.forward()
    time.sleep(2)
    motordx.stop()
    time.sleep(1)
    motorsx.backward()
    motordx.backward()
    time.sleep(2)
    motorsx.stop()
    motordx.stop()

    io.cleanup()


if __name__ == '__main__':
    main()
