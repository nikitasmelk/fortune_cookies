from PIL import ImageGrab
import webcolors
from time import time, sleep
import pyautogui

array_of_colors = [(80, 103, 6), (101, 128, 6), (81, 104, 6), (163, 211, 1), (172, 223, 0)];
array_of_color_names = ["darkolivegreen", "olive", "yellowgreen"]



def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

requested_colour = (119, 172, 152)
actual_name, closest_name = get_colour_name(requested_colour)



print(pyautogui.position())



# image = ImageGrab.grab()
# for y in range(0, 10, 1):
#     for x in range(0, 10, 1):
#         # color = image.getpixel((x, y))
#         # print(get_colour_name(color))
#         print(x)

# image = ImageGrab.grab()
# color = image.getpixel((518,582))
# print(get_colour_name(color))


# while True:
#   sleep(2 - time() % 2)
#   image = ImageGrab.grab()
#   color = image.getpixel((518,582))
#   print(get_colour_name(color))
#   print(image.getpixel((518, 582)))


# print(get_colour_name((80, 103, 6)))
# print(get_colour_name((101, 128, 6)))
# print(get_colour_name((81, 104, 6)))
# print(get_colour_name((163, 211, 1)))
# print(get_colour_name((81, 104, 6)))

# while True:
#   sleep(2 - time() % 2)
#   image = ImageGrab.grab()
#   color = image.getpixel((1069,160))
#   # print(get_colour_name(color))
#   if color not in array_of_colors:
#     array_of_colors.append(color)
#     color = image.getpixel((1074,160))
#   # print(get_colour_name(color))
#   if color not in array_of_colors:
#     array_of_colors.append(color)
#     color = image.getpixel((1079,160))
#   # print(get_colour_name(color))
#   if color not in array_of_colors:
#     array_of_colors.append(color)
#     color = image.getpixel((1084,160))
#   # print(get_colour_name(color))
#   if color not in array_of_colors:
#     array_of_colors.append(color)
#     color = image.getpixel((1089,160))
#   # print(get_colour_name(color))
#   if color not in array_of_colors:
#     array_of_colors.append(color)
#   print(array_of_colors)


while True:
  sleep(0.1 - time() % 0.1)
  pyautogui.click(1079, 300)
  pyautogui.click(1079, 400)
  pyautogui.click(1079, 500)
  pyautogui.click(1079, 600)
  pyautogui.click(1079, 700)
  pyautogui.click(1079, 800)
  pyautogui.click(1079, 900)
  pyautogui.click(1079, 950)
  image = ImageGrab.grab()
  for i in range(0, 50, 5):
      for j in range (0, 20, 4):
         color = image.getpixel((1069 + i,160 + j))
         name = get_colour_name(color)
         print(name)
         if color in array_of_colors or name in array_of_color_names:
             for j in range(20):
                 pyautogui.click(1040 + j, 160)

 


