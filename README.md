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
- `clearBuffers`: Clears the framebuffer (all elements to `0`).
- `putPixel(x, y, value)`: Puts the `value` (`0` or `1`) at `x`, `y` coordinates.
- `putRectangle(x, y, width, height, fill)`: Puts a rectangle (`width` x `height`) at the specified `x`, `y` coordinates. Setting `fill` to `True` will fill the rectangle, where `False` will draw just the borders.
- `putBitmap(x, y, bitmap)`: Puts a `bitmap` MxN array of `0`s and `1`s to `x`, `y` coordinates.
- `translateBitmap(bitmap)`: Converts a MxN `bitmap` array where each element is a `bit` (`0` or `1`), to a `byte` array MxL where each element is a `byte` (8 `bits`). Bitmap array sizes can be: `0<M<128` and `0<N<64`, and the translated bitmap will have sizes: `0<M<128` and `0<L<8`. Useful for achieving faster rendering rates. Use before calling `bitmapBlit()`.
- `scaleBitmap(bitmap, scaleX, scaleY)`: Scales down the given `bitmap`. Each axis can scale differently by setting `scaleX`, `scaleY`. Positive integer values only.
- `rotateBitmap90(bitmap)`: Rotates the `bitmap` 90 degrees.
- `rotateBitmap180(bitmap)`: Rotates the `bitmap` 180 degrees.
- `rotateBitmap270(bitmap)`: Rotates the `bitmap` 270 degrees.
- `blit()`: Renders the whole `framebuffer` to screen at maximum fast rate.
- `pageBlit(pageNo, x, length)`: Renders portion of a page, (row) with `length` starting from `x`, to screen at maximum fast rate. Does not clear the `framebuffer` after.
- `bitmapBlit(x, y, translatedBitmap)`: Instead of filling the whole 128x64 framebuffer it renders only the region of a `translatedBitmap` on the screen at `x`, `y` location, sort of Direct Memory Access (DMA). Requires the `translatedBitmap` from `translateBitmap()` as input. Does not clear the `framebuffer` after.
