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

    def stream(self):
        while True:
            io.output(self.trig, True)
            time.sleep(self.deltaT)
            io.output(self.trig, False)

            t0 = time.time()
            t1 = time.time()

            tout = time.time()
            timeout = False
            while (not timeout) and (io.input(self.echo) == 0):
                t0 = time.time()
                if (t0 - tout) > 0.01:  # 170cm
                    timeout = True

            while (not timeout) and (io.input(self.echo) == 1):
                t1 = time.time()
                if (t1 - tout) > 0.01:  # 170cm
                    timeout = True

            if not timeout:
                echoT = t1 - t0
                yield echoT * self.s_to_cm
            else:
                yield -1
