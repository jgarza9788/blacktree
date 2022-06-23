
import os
from numpy import True_
# import sys
from functions import *

DIR = os.path.dirname(os.path.realpath(__file__))

rainmeter = """

[Rainmeter]
Update=1000
AccurateText=1
DynamicWindowSize=1

[FrostedGlass]
Measure=Plugin
Plugin=FrostedGlass
Type=Blur
;Border=All

"""

#monoki colors
# 244,0,95 PINK
# 152,224,36 GREEN
# 250,132,25 ORANGE
# 157,101,255 PURPLE
# 88,209,235 BLUE


variables = """

[variables]
RECSHAPE = 25,25,400,50,10
BACKGROUNDCOLOR = 0,0,0,175
NORMALCOLOR = "255,255,255,255"
LITECOLOR = "255,255,255,127"
HOVERCOLOR = "88,209,235,255" 

ACTIVESHAPE="Rectangle 0,0,760,40,20 | Fill Color 88,209,235,50 | StrokeWidth 0 | Stroke Color 0,0,0,0"
INACTIVESHAPE="Rectangle 0,0,760,40,0 | Fill Color 0,0,0,0 | StrokeWidth 0"

"""

metershape = """

[BG{index}]
Meter=Shape
Shape=Rectangle 0,0,800,{HEIGHT},0 | Fill Color #BACKGROUNDCOLOR# | StrokeWidth 0

[RecreateMeter]
Meter=Shape
Shape=Rectangle 0,0,50,50,0 | Fill Color 0,0,0,0 | StrokeWidth 0
Y=0r
X=750r
MouseOverAction=[!SetOption RecreateMeterIcon FontColor #HOVERCOLOR#][!UpdateMeter RecreateMeterIcon][!Redraw]
MouseLeaveAction=[!SetOption RecreateMeterIcon FontColor #LITECOLOR#][!UpdateMeter RecreateMeterIcon][!Redraw]
LeftMouseUpAction=["{path}"]

[RecreateMeterIcon]
Meter=String
FontFace=Hack NF
FontSize=25
FontColor=#LITECOLOR#
SolidColor=47,47,47,1
Padding=0,0,0,0
AntiAlias=1
Y=6r
X=16r
Text="\uf021"

[anchor{index}]
Meter=Shape
Shape=Rectangle 0,0,10,10,0 | Fill Color 0,0,0,0 | StrokeWidth 0
X=20
Y=50

"""

# [RecreateMeter]
# Meter=String
# FontFace=Hack NF
# FontSize=24
# FontColor=#LITECOLOR#
# SolidColor=47,47,47,1
# Padding=6,6,6,6
# AntiAlias=1
# Y=24r
# X=788r
# Text="\uf021"
# MouseOverAction=[!SetOption RecreateMeter FontColor #HOVERCOLOR#][!UpdateMeter RecreateMeter][!Redraw]
# MouseLeaveAction=[!SetOption RecreateMeter FontColor #LITECOLOR#][!UpdateMeter RecreateMeter][!Redraw]
# LeftMouseUpAction=["{path}"]

#################################

# LeftMouseUpAction=["{path}"]
# ;MouseOverAction=[!SetOption MeterIcon{index} FontColor #HOVERCOLOR#][!SetOption MeterText{index} FontColor #HOVERCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterIcon{index} FontColor #NORMALCOLOR#][!SetOption MeterText{index} FontColor #NORMALCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;LeftMouseUpAction=["{path}"]

# ;MouseOverAction=[!SetOption MeterShapes{index} Shape "Rectangle #RECSHAPE# | Fill Color {HOVERCOLOR} | StrokeWidth 0"][!SetOption MeterIcon{index} FontColor #ICONHOVERCOLOR#][!SetOption MeterText{index} FontColor #TEXTHOVERCOLOR#][!UpdateMeter MeterShapes{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterShapes{index} Shape "Rectangle #RECSHAPE# | Fill Color #NORMALCOLOR# | StrokeWidth 0"][!SetOption MeterIcon{index} FontColor #ICONCOLOR#][!SetOption MeterText{index} FontColor #TEXTCOLOR#][!UpdateMeter MeterShapes{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;MouseOverAction=[!SetOption MeterIcon{index} FontColor {HOVERCOLOR}][!SetOption MeterText{index} FontColor {HOVERCOLOR}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterIcon{index} FontColor #ICONCOLOR#][!SetOption MeterText{index} FontColor #TEXTCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;LeftMouseUpAction=["{path}"]
# ;Y={Y}

# ;MouseOverAction=[!SetOption MeterText Text "{icon0} {text}"][!SetOption MeterShapes Shape "Rectangle 50,50,500,100,10 | Fill Color #RED# | StrokeWidth 0"][!UpdateMeter MeterText][!UpdateMeter MeterShapes][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterText Text "{icon1} {text}"][!SetOption MeterShapes Shape "Rectangle 50,50,500,100,10 | Fill Color #WHITE# | StrokeWidth 0"][!UpdateMeter MeterText][!UpdateMeter MeterShapes][!Redraw]

#################################



file_item = """

[MeterShape{index}]
Meter=Shape
;Shape=Rectangle 0,0,750,40,0 | FillColor 0,0,0,0 | StrokeWidth 0
Shape=#INACTIVESHAPE#
Y=0r
X=0r
;MouseOverAction=[!SetOption MeterIcon{index} FontColor #HOVERCOLOR#][!SetOption MeterText{index} FontColor #HOVERCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
;MouseLeaveAction=[!SetOption MeterIcon{index} FontColor #NORMALCOLOR#][!SetOption MeterText{index} FontColor #NORMALCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
;MouseOverAction=[!SetOption MeterShape{index} Shape #ACTIVESHAPE#][!SetOption MeterIcon{index} FontColor #HOVERCOLOR#][!SetOption MeterText{index} FontColor #HOVERCOLOR#][!UpdateMeter MeterShape{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
;MouseLeaveAction=[!SetOption MeterShape{index} Shape #INACTIVESHAPE#][!SetOption MeterIcon{index} FontColor #NORMALCOLOR#][!SetOption MeterText{index} FontColor #NORMALCOLOR#][!UpdateMeter MeterShape{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
MouseOverAction=[!SetOption MeterShape{index} Shape "#ACTIVESHAPE#"][!SetOption MeterString{index} FontColor #HOVERCOLOR#][!SetOption MeterIcon{index} FontColor #HOVERCOLOR#][!UpdateMeter MeterShape{index}][!UpdateMeter MeterString{index}][!UpdateMeter MeterIcon{index}][!Redraw]
MouseLeaveAction=[!SetOption MeterShape{index} Shape "#INACTIVESHAPE#"][!SetOption MeterIcon{index} FontColor #NORMALCOLOR#][!SetOption MeterString{index} FontColor #NORMALCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterShape{index}][!UpdateMeter MeterString{index}][!Redraw]

LeftMouseUpAction=["{path}"]




[MeterString{index}]
Meter=String
FontFace=Hack NF
FontSize=18
;FontSize=15
;FontSize=30
FontColor=#NORMALCOLOR#
SolidColor=47,47,47,0
Padding=0,0,0,0
AntiAlias=1
Y=6r
X=-10r
StringAlign=Left
Text="{textindent}{text}"

[MeterIcon{index}]
Meter=String
FontFace=Hack NF
FontSize=36
;;FontSize=15
;;FontSize=30
FontColor=#NORMALCOLOR#
SolidColor=47,47,47,0
Padding=0,0,0,0
AntiAlias=1
Y=-16r
X=-38r
StringAlign=Left
Text="{iconindent}{icon}"

[anchor{index}]
Meter=Shape
Shape=Rectangle 0,0,10,10,0 | Fill Color 0,0,0,0 | StrokeWidth 0
Y={Y}
X=20


"""

# [MeterString{index}]
# Meter=String
# FontFace=Hack NF
# FontSize=18
# FontColor=#NORMALCOLOR#
# SolidColor=47,47,47,0
# Padding=0,0,0,0
# AntiAlias=1
# Y=6r
# Y=5r
# Y=-6r
# X=-24r
# StringAlign=Left
# Text="{indent}{icon}  {text}"

# ;MyFillColor = FillColor 0,0,0,0
# ;MouseOverAction=[!SetOption MeterShape{index} MyFillColor "FillColor 0,0,0,100"][!SetOption MeterIcon{index} FontColor #HOVERCOLOR#][!SetOption MeterText{index} FontColor #HOVERCOLOR#][!UpdateMeter MeterShape{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterShape{index} MyFillColor "FillColor 0,0,0,0"][!SetOption MeterIcon{index} FontColor #NORMALCOLOR#][!SetOption MeterText{index} FontColor #NORMALCOLOR#][!UpdateMeter MeterShape{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]


# [MeterIcon{index}]
# Meter=String
# FontFace=Hack NF
# FontSize=40
# FontColor=#NORMALCOLOR#
# SolidColor=47,47,47,0
# Padding=0,0,0,0
# AntiAlias=1
# Y=-12r
# X=12r
# StringAlign=Left
# Text="{icon}"

# [MeterText{index}]
# Meter=String
# FontFace=Hack NF
# FontSize=12
# FontColor=#NORMALCOLOR#
# SolidColor=47,47,47,0
# Padding=0,0,0,0
# AntiAlias=1
# Y=20r
# X=45r
# StringAlign=Left
# Text="Desktop"


# yshift = 60
# ytextshift = 40
# yiconshift = 55
# xtextshift=95
# xiconshift=60

# regex patters that map to nerd font icons
icon_map_00 = {
    # 'Desktop$':'\uf108 - desktop',
    # '\.py':'\ue235 - python',
    # '\.bat':'\ue795 - bat',
    # '\.wt(\.|)':'\ue795 - winterminal',
    # '\.url$':'\uf465 - url',
    # ' - Shortcut\.lnk':'\uf482 - folderlink',
    'Desktop$':'\uf108',
    '(\.png|\.psd|\.jpg)': '\uf7e8',
    '\.py':'\ue235',
    '(\.bat|\.wt|\.vbs)':'\ue795',
    # '\.wt(\.|)':'\ue795',
    # '\.vbs(\.|)':'\uf481',
    # '\.url$':'\uf465',
    ' - Shortcut\.lnk':'\uf482',
    '(\.xls|\.xlsx|\.csv)': '\uf71b',
    '\.pdf':'\uf725',
    '(\.url|\.lnk)':'\uf268',
    '\.txt':'\uf15c',
}


def get_text(string,max_length=40):
    result =  string.split('\\')[-1]

    if len(result) > max_length:
        result = result[:(max_length-10)] + '...' + result[-7:]

    return result 

def exclude(text):
    if re.match(pattern=r'(^~|\.tmp|desktop\.ini|^\.)',string=text):
        return True
    else:
        return False

METERNUM = 0 

def item_factory_v3(t,indent=0):
    global METERNUM
    result = []

    for index,i in enumerate(t):
        
        text = get_text(i['name'])
        # print('x'+text+'x')
        if exclude(text) == True:
            continue;

        print(text,i['name'],indent)

        fi = file_item.format(
            index=METERNUM,
            Y='{Y}',
            # indent='   '*(indent+1),
            textindent = '    '*(indent+1),
            iconindent = '  '*(indent+1),
            icon=get_icon(text,icon_map_00),
            text=text,
            path=i['name']
            )
        result.append(fi)


        if 'children' in i.keys():
            METERNUM += 1
            result += item_factory_v3(i['children'],indent=indent+1)
        METERNUM += 1

    return result


def main():
    rm = rainmeter
    rm += variables

    tree = get_tree(r'C:\Users\JGarza\Desktop',sort_all = True)

    items = item_factory_v3([tree],indent=0)
    shape = metershape.format(index=-1,HEIGHT=(40*len(items)) + 80,path=os.path.join(DIR,'refresh.cmd'))
    rm += shape

    for index,i in enumerate(items):
        rm += i.format(Y=(40*(index+1)) + 50)

    save(rm,os.path.join(DIR,'blacktree.ini'))



if __name__ == "__main__":

    main()

