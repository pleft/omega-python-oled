import OledLib
from OmegaExpansion import oledExp
from random import randint
import time

batman = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1],
[1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1],
[1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1],
[1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1],
[1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1],
[1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1],
[1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
[1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
[1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
[1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
[1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
[1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
[1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1],
[1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1],
[1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1],
[1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1],
[1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1],
[1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

start = int(round(time.time() * 1000))
# bitmap blitting example at random positions
oledExp.clear()
oledExp.write("Bitmap bliting")
time.sleep(2)
oledExp.clear()
frames = 0
exampleStart = int(round(time.time() * 1000))
for i in range(10):
	OledLib.putBitmap(randint(0, 60), randint(8, 20), batman)
	OledLib.blit()
	frames += 1
exampleEnd = int(round(time.time() * 1000))
millis = exampleEnd - exampleStart
print("Bitmap bliting took: " + str(millis) + " milliseconds") 
print("Total Frames: " + str(frames))
print("FPS: " + str(frames*1000/float(millis)))
time.sleep(1)

# scalling example (zooming in, both axes scale)
oledExp.clear()
oledExp.write("Scaling: zoom in")
time.sleep(2)
frames = 0
exampleStart = int(round(time.time() * 1000))
for scale in range(8, 0, -1):
	scaledBatman = OledLib.scaleBitmap(batman, scale, scale)
	h = len(scaledBatman)
	w = len(scaledBatman[0])
	OledLib.putBitmap(64-w/2, 32-h/2, scaledBatman)
	OledLib.blit()
	frames += 1
exampleEnd = int(round(time.time() * 1000))
millis = exampleEnd - exampleStart
print("Scaling: zoom in took: " + str(millis) + " milliseconds") 
print("Total Frames: " + str(frames))
print("FPS: " + str(frames*1000/float(millis)))
time.sleep(1)

# rotate bitmap 90, 180, 270, 360 degrees
oledExp.clear()
oledExp.write("Rotation: 90, 180, 270 degrees")
time.sleep(2)
oledExp.clear()
frames = 0
exampleStart = int(round(time.time() * 1000))
rotatedBatman = OledLib.rotateBitmap90(batman)
h = len(rotatedBatman)
w = len(rotatedBatman[0])
OledLib.putBitmap(64-w/2, 32-h/2, rotatedBatman)
OledLib.blit()
frames += 1

rotatedBatman = OledLib.rotateBitmap180(batman)
h = len(rotatedBatman)
w = len(rotatedBatman[0])
OledLib.putBitmap(64-w/2, 32-h/2, rotatedBatman)
OledLib.blit()
frames += 1

rotatedBatman = OledLib.rotateBitmap270(batman)
h = len(rotatedBatman)
w = len(rotatedBatman[0])
OledLib.putBitmap(64-w/2, 32-h/2, rotatedBatman)
OledLib.blit()
frames += 1

h = len(batman)
w = len(batman[0])
OledLib.putBitmap(64-w/2, 32-h/2, batman)
OledLib.blit()
frames += 1

exampleEnd = int(round(time.time() * 1000))
millis = exampleEnd - exampleStart
print("Rotation: 90, 180, 270 degrees took: " + str(millis) + " milliseconds") 
print("Total Frames: " + str(frames))
print("FPS: " + str(frames*1000/float(millis)))
time.sleep(1)

# scaling example (x-axis only)
oledExp.clear()
oledExp.write("Scaling: x-axis")
time.sleep(2)
oledExp.clear()
frames = 0
exampleStart = int(round(time.time() * 1000))
scale = 1
while scale<=8:
	scaledBatman = OledLib.scaleBitmap(batman, scale, 1)
	h = len(scaledBatman)
	w = len(scaledBatman[0])
	OledLib.putBitmap(64-w/2, 32-h/2, scaledBatman)
	OledLib.blit()
	scale += 1
	frames += 1

scale = 8
while scale>0:
	scaledBatman = OledLib.scaleBitmap(batman, scale, 1)
	h = len(scaledBatman)
	w = len(scaledBatman[0])
	OledLib.putBitmap(64-w/2, 32-h/2, scaledBatman)
	OledLib.blit()
	scale -= 1
	frames += 1

exampleEnd = int(round(time.time() * 1000))
millis = exampleEnd - exampleStart
print("Scaling: x-axis took: " + str(millis) + " milliseconds") 
print("Total Frames: " + str(frames))
print("FPS: " + str(frames*1000/float(millis)))
time.sleep(1)

# scaling and rotating example (y-axis only)
oledExp.clear()
oledExp.write("Scaling and rotating: y-axis")
time.sleep(2)
oledExp.clear()
frames = 0
exampleStart = int(round(time.time() * 1000))
OledLib.putBitmap(64-w/2, 32-h/2, batman)
OledLib.blit()
frames += 1
scale = 1
while scale<=8:
	scaledBatman = OledLib.scaleBitmap(batman, 1, scale)
	h = len(scaledBatman)
	w = len(scaledBatman[0])
	OledLib.putBitmap(64-w/2, 32-h/2, scaledBatman)
	OledLib.blit()
	scale += 1
	frames += 1

rotatedBatman = OledLib.rotateBitmap180(batman)
h = len(rotatedBatman)
w = len(rotatedBatman[0])

scale = 8
while scale>0:
	scaledBatman = OledLib.scaleBitmap(rotatedBatman, 1, scale)
	h = len(scaledBatman)
	w = len(scaledBatman[0])
	OledLib.putBitmap(64-w/2, 32-h/2, scaledBatman)
	OledLib.blit()
	scale -= 1
	frames += 1

exampleEnd = int(round(time.time() * 1000))
millis = exampleEnd - exampleStart
print("Scaling and rotating: y-axis took: " + str(millis) + " milliseconds") 
print("Total Frames: " + str(frames))
print("FPS: " + str(frames*1000/float(millis)))

time.sleep(1)
oledExp.write("Enjoy OledLib!")
end = int(round(time.time() * 1000))
print("Demo completed in: " + str(end-start) + " milliseconds.")