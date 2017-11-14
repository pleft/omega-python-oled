# OledLib
Onion Omega OledExpansion Graphics Library in Python

## Intro
`OledLib` is a small graphics library for the OledExpansion module for Onion Omega IoT devices.

While the `oledExp` Python module mainly deals with writing text on screen, `OledLib` dives deeper into pixel precise graphics.
`OledLib` breaks the limit of 8 pages and 128 columns, giving access to all 128x64 pixels of the screen. It is also faster since it uses the `i2c` interface
which is capable of sending 32 bytes of data simultaneously instead of only 1 byte (`oledExp.write(byte)`). 

With `OledLib`'s ability to address each pixel individually, `OledExpansion` becomes much more versatile and capable of rendering
complex graphics.

## Features
- 128x64 framebuffer, pixel-level precision 
- Up to 32 bytes sent to screen simultaneously
- 1-bit bitmap rendering
- DMA (Direct Memory Access) functionality to fast render a portion of the screen only.
- Special effects: rotation and scaling

## Prerequisites
Requires [oledExp](https://docs.onion.io/omega2-docs/oled-expansion-python-module.html) and [onionI2C](https://docs.onion.io/omega2-docs/i2c-python-module.html) 
Python modules to be installed on the Onion Omega IoT device.

## API
- `putPixel(x, y, value)`
- `putRectangle(x, y, width, height, fill)`
- `putBitmap(x, y, bitmap)`
- `translateBitmap(bitmap)`
- `scaleBitmap(bitmap, scaleX, scaleY)`
- `rotateBitmap90(bitmap)`
- `rotateBitmap180(bitmap)`
- `rotateBitmap270(bitmap)`
- `blit()`
- `pageBlit()`
- `bitmapBlit()`
