from math import log

def hue_converter(c: float, m: float, hue: float) ->tuple:
    x = c * (1 - abs((hue / 60) % 2 - 1))
    tmp = [0] * 3
    RGB = [0] * 3

    if 0 <= hue < 60:
        tmp = [c, x, 0]
    elif 60 <= hue < 120:
        tmp = [x, c, 0]
    elif 120 <= hue < 180:
        tmp = [0, c, x]
    elif 180 <= hue < 240:
        tmp = [0, x, c]
    elif 240 <= hue < 300:
        tmp = [x, 0, c]   
    elif 300 <= hue < 360:
        tmp = [c, 0, x]   
    
    for i in range(len(tmp)):
        RGB[i] = round((tmp[i] + m) * 255) 
    
    return tuple(RGB)


def convert_HSV_to_RGB(hue: float, saturation: float, value: float) -> tuple:
    c = value * saturation
    m = value - c
 
    RGB = hue_converter(c=c, m=m, hue=hue)

    return RGB


def convert_HSL_to_RGB(hue: float, saturation: float, lightness: float) -> tuple:
    c = 1 - abs(2 * lightness - 1) * saturation
    m = lightness - c / 2
    
    RGB = hue_converter(c=c, m=m, hue=hue)

    return RGB


def convert_temperature_to_RGB(T_kelvin: float):
    if T_kelvin < 6700:
        x_green = (T_kelvin / 100) - 2
        g = -140 + 104 * log(x_green)
        r = 255
    
        if T_kelvin < 2000:
            b = 0
        else: 
            x_blue = (T_kelvin / 100) - 10
            b = -255 + 116 * log(x_blue)
    else:
        x_red = (T_kelvin / 100) - 55
        x_green = (T_kelvin / 100) - 50

        r = 352 - 40 * log(x_red)
        g = 325 - 28 * log(x_green)
        b = 255
    
    r = round(r)
    g = round(g)
    b = round(b) 

    return (r, g, b)


print(convert_HSV_to_RGB(hue=300, saturation=1, value=1))
print(convert_HSL_to_RGB(hue=120, saturation=1, lightness=0.5))
print(convert_temperature_to_RGB(T_kelvin=8000))