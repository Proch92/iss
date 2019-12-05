import time
import RPi.GPIO as io
import asyncio


io.setmode(io.BCM)
io.setwarnings(False)


class Sonar():
	def __init__(self, echo, trig, vcc):
		self.echo = echo
		self.trig = trig
		self.vcc = vcc
		self.deltaT = 0.015
		self.ms_to_cm = 58.2

		io.setup(echo, io.IN)
		io.setup(trig, io.OUT)
		io.setup(vcc, io.OUT)

		io.output(trig, False)
		io.output(vcc, True)

	async def read(self):
		io.output(self.trig, True)
		await asyncio.sleep(self.deltaT)
		io.output(self.trig, False)

		while io.input(self.echo) == False:
			pass
		t0 = time.time()

		while io.input(self.echo) == True:
			pass
		t1 = time.time()

		echoT = t1 - t0
		return echoT / ms_to_cm
