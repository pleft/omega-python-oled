from OmegaExpansion import oledExp
from OmegaExpansion import onionI2C
import time

OLED_EXP_ADDR = 0x3C
OLED_EXP_REG_DATA = 0x40
OLED_I2C_MAX_BUFFER = 32

OLED_PAGE_SIZE = 8
OLED_PAGES = 8
OLED_WIDTH = 128
OLED_HEIGHT = OLED_PAGE_SIZE * OLED_PAGES

i2c = onionI2C.OnionI2C()

oledExp.driverInit()
oledExp.setImageColumns()
oledExp.setMemoryMode(0)

# pagebuffer 128x8 holding bytes
pagebuffer = [[0 for i in range(OLED_WIDTH)] for j in range(OLED_PAGES)]


def bin(s):
    return str(s) if s <= 1 else bin(s >> 1) + str(s & 1)


def clearBuffers():
    """
        Clears the framebuffers (all elements to 0).
    """
    global pagebuffer
    pagebuffer = [[0 for i in range(OLED_WIDTH)] for j in range(OLED_PAGES)]


def putPixel(x, y, value):
    """
        Puts the `value` (0 or 1) at `x`, `y` coordinates.
    """
    global pagebuffer
    byte = (value << (y% OLED_PAGE_SIZE))
    pagebuffer[(y / OLED_PAGE_SIZE) % OLED_PAGES][x] |= byte

def putRectangle(x, y, width, height, fill):
    """ 
        Puts a rectangle (`width` x `height`) at the specified `x`, `y` coordinates. Setting `fill` to `True` will fill the rectangle, where `False` will draw just the borders.
    """
    if fill:
        for i in range(width):
            for j in range(height):
                putPixel(x + i, y + j, 1)
    else:
        for i in range(width):
            putPixel(x + i, y, 1)
            putPixel(x + i, y + height - 1, 1)
        for j in range(height):
            putPixel(x, y + j, 1)
            putPixel(x + width - 1, y + j, 1)


def putBitmap(x, y, bitmap):
    """
        Puts a `bitmap` MxN array of 0s and 1s to `x`, `y` coordinates.
    """
    height = len(bitmap)
    width = len(bitmap[0])
    for i in range(width):
        for j in range(height):
            putPixel(x + i, y + j, bitmap[j][i])


def blit():
    """
        Renders the whole `framebuffer` to screen at maximum fast rate.
    """
    # start = int(round(time.time() * 1000))
    global pagebuffer
    page = 0
    while page < OLED_PAGES:
        count = 0
        while count < OLED_WIDTH:
            bytes = [pagebuffer[page][count + i]
                     for i in range(OLED_I2C_MAX_BUFFER)]
            i2c.writeBytes(OLED_EXP_ADDR, OLED_EXP_REG_DATA, bytes)
            count += OLED_I2C_MAX_BUFFER
        page += 1
    # after blitting to screen, clear the pagebuffer
    clearBuffers()
    # end = int(round(time.time() * 1000))
    # print("blit() took: " + str(end - start))


def pageBlit(pageNo, x, length):
    """ 
        Renders portion of a page, (row) with `length` starting from `x`, to screen at maximum fast rate. Does not clear the `framebuffer` after.
    """
    start = int(round(time.time() * 1000))
    oledExp.setCursorByPixel(pageNo, x)
    global pagebuffer
    count = 0
    while count < length:
        lineWidth = length if length < OLED_I2C_MAX_BUFFER else (
            OLED_I2C_MAX_BUFFER if length - count > OLED_I2C_MAX_BUFFER else length - count)
        bytes = [pagebuffer[pageNo][x + count + i]
                 for i in range(lineWidth)]
        i2c.writeBytes(OLED_EXP_ADDR, OLED_EXP_REG_DATA, bytes)
        count += lineWidth
    oledExp.setCursorByPixel(0, 0)
    end = int(round(time.time() * 1000))
    print("pageBlit() took: " + str(end - start))


def bitmapBlit(x, y, translatedBitmap):
    """
        Instead of filling the whole 128x64 framebuffer it renders only the region of a `translatedBitmap` on the screen at `x`, `y` location, sort of Direct Memory Access (DMA). Requires the `translatedBitmap` from `translateBitmap()` as input. Does not clear the `framebuffer` after.
    """
    # start = int(round(time.time() * 1000))
    bitmapHeight = len(translatedBitmap)
    bitmapWidth = len(translatedBitmap[0])
    bitmapPage = 0 
    bufferPage = (y / OLED_PAGE_SIZE) % OLED_PAGES
    # print("Bitmap height: " + str(bitmapHeight))
    while bitmapPage < bitmapHeight:
        # print("Bitmap page: " + str(bitmapPage))
        oledExp.setCursorByPixel(bufferPage+bitmapPage, x)
        # bitmapWidth = bitmapWidth if OLED_WIDTH > bitmapWidth + x else OLED_WIDTH - x
        count = 0
        while count < bitmapWidth:
            lineWidth = bitmapWidth if bitmapWidth < OLED_I2C_MAX_BUFFER else (
                OLED_I2C_MAX_BUFFER if bitmapWidth - count > OLED_I2C_MAX_BUFFER else bitmapWidth - count)
            # lineWidth = lineWidth if lineWidth != 23 else 22 #segmentation fault when 23
            # print(lineWidth)
            # print(translatedBitmap[bitmapPage])
            # print(count)
            bytes = [translatedBitmap[bitmapPage][count + i] for i in range(lineWidth)]
            i2c.writeBytes(OLED_EXP_ADDR, OLED_EXP_REG_DATA, bytes)
            count += lineWidth
        oledExp.setCursorByPixel(0, 0)
        bitmapPage += 1
    # end = int(round(time.time() * 1000))
    # print("bitmapBlit() took: " + str(end - start))

def translateBitmap(bitmap):
    """
        Converts a MxN `bitmap` array where each element is a `bit` (0 or 1), to a `byte` array MxL where each element is a `byte` (8 `bits`). Bitmap array sizes can be: `0<M<128` and `0<N<64`, and the translated bitmap will have sizes: `0<M<128` and `0<L<8`. Useful for achieving faster rendering rates. Use before calling `bitmapBlit()`.
    """
    bitmapHeight = len(bitmap)
    bitmapWidth = len(bitmap[0])
    bitmapRows = ((bitmapHeight -1)/ OLED_PAGE_SIZE) + 1
    # print("bitmapHeight: " + str(bitmapHeight))
    # print("bitmapRows: " + str(bitmapRows))
    translation = [[0 for i in range(bitmapWidth)] for j in range(bitmapRows)]
    for x in range(bitmapWidth):
        for y in range(bitmapHeight):
            byte = (bitmap[y][x] << (y%OLED_PAGE_SIZE))
            translation[(y / OLED_PAGE_SIZE) % bitmapRows][x] |= byte
    return translation

def scaleBitmap(bitmap, scaleX, scaleY):
    """
        Scales down the given `bitmap`. Each axis can scale differently by setting `scaleX`, `scaleY`. Positive integer values only.
    """
    width = len(bitmap[0])
    height = len(bitmap)
    return [[bitmap[j][i] for i in range(0, width, scaleX)] for j in range(0, height, scaleY)]

def rotateBitmap90(bitmap):
    """
        Rotates the `bitmap` 90 degrees.
    """
    width = len(bitmap[0])
    height = len(bitmap)
    rotated = [[0 for i in range(height)] for j in range(width)]
    for x in range(width):
        for y in range(height):
            rotated[x][y] = bitmap[height-1-y][x]
    return rotated

def rotateBitmap180(bitmap):
    """
        Rotates the `bitmap` 180 degrees.
    """
    width = len(bitmap[0])
    height = len(bitmap)
    rotated = [[0 for i in range(width)] for j in range(height)]
    for x in range(width):
        for y in range(height):
            rotated[y][x] = bitmap[height-1-y][x]
    return rotated

def rotateBitmap270(bitmap):
    """
        Rotates the `bitmap` 270 degrees.
    """
    width = len(bitmap[0])
    height = len(bitmap)
    rotated = [[0 for i in range(height)] for j in range(width)]
    for x in range(width):
        for y in range(height):
            rotated[x][y] = bitmap[y][x]
    return rotated