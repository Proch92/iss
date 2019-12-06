import time
import RPi.GPIO as io


io.setmode(io.BCM)
io.setwarnings(False)


class Sonar():
    def __init__(self, echo, trig):
        self.echo = echo
        self.trig = trig
        self.deltaT = 0.00001
        self.s_to_cm = 17150

        io.setup(echo, io.IN)
        io.setup(trig, io.OUT)

        io.output(trig, False)

    def read(self):
        io.output(self.trig, True)
        time.sleep(self.deltaT)
        io.output(self.trig, False)

        t0 = time.time()
        t1 = time.time()

        while io.input(self.echo) == 0:
            t0 = time.time()

        while io.input(self.echo) == 1:
            t1 = time.time()

        echoT = t1 - t0
        return echoT * self.s_to_cm
