import OledLib
from OmegaExpansion import oledExp
from random import randint
import time
import RoadDemoResources as RDS

car1 = [[RDS.tileset[j][i] for i in range(24)] for j in range(10)]
car2 = [[RDS.tileset[j][i] for i in range(24)] for j in range(len(RDS.tileset)-14, len(RDS.tileset), 1)]

transCar1 = OledLib.translateBitmap(car1)
transCar2 = OledLib.translateBitmap(car2)

car1Width = len(car1[0])
car2Width = len(car2[0])

frames = 0
car1Pos = 0
car2Pos = 0

OledLib.init()

while True:
    OledLib.bitmapBlit(car1Pos, 10, transCar1)
    OledLib.bitmapBlit(car2Pos, 32, transCar2)
    car1Pos = car1Pos + 1 if car1Pos<OledLib.OLED_WIDTH-1 else (0 if car1Pos>=OledLib.OLED_WIDTH-1 else car1Pos)
    car2Pos = car2Pos + 1 if car2Pos<OledLib.OLED_WIDTH-1 and frames%2==0 else 0 if car2Pos>=OledLib.OLED_WIDTH-1 else car2Pos
    frames += 1