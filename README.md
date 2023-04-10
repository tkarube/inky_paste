# inky_paste

Inky pHAT (ePaper/eInk/EPD)
https://shop.pimoroni.com/products/inky-phat

example:

```
#!/usr/bin/env python3

from PIL import Image
import inky_paste

# PIMORONI Inky pHAT boilerplate
from inky.auto import auto
inky_display = auto()

inky_display.set_border(inky_display.WHITE)
inky_display_img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))

# --- Write your program below ---

img_path = "./Tux.png"
#inky_display_img = inky_paste.image(inky_display_img, img_path, 0, 0)
inky_display_img = inky_paste.image_convert(inky_display_img, img_path, 0, 0)

inky_paste.text(inky_display_img, "Hello", inky_display.RED, 22, 90, 5)
inky_paste.text(inky_display_img, "Hello, World!", inky_display.BLACK, 22, 95, 27)
inky_paste.text(inky_display_img, "Hello, World!", inky_display.RED, 22, 100, 49)
inky_paste.text(inky_display_img, "Hello, World!", inky_display.BLACK, 22, 105, 71)
inky_paste.text(inky_display_img, "Hello, World!", inky_display.RED, 22, 100, 93)

# --- Write your program above ---

# Display the image
inky_display.set_image(inky_display_img)
inky_display.show()
```
