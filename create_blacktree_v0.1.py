
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

variables = """

[variables]
RECSHAPE = 25,25,400,50,10
BACKGROUNDCOLOR = 0,0,0,175


NORMALCOLOR = "255,255,255,255"
LITECOLOR = "255,255,255,127"
;HOVERCOLOR = "166,226,46,255" 
;GREEN
;HOVERCOLOR = "244,0,95,255" 
;PINK
;HOVERCOLOR = "250,132,25,255" 
;ORANGE
;HOVERCOLOR = "157,101,255,255" 
;PURPLE
HOVERCOLOR = "88,209,235,255" 
;BLUR

"""

metershape = """

[BG{index}]
Meter=Shape
Shape=Rectangle 0,0,800,{HEIGHT},10 | Fill Color #BACKGROUNDCOLOR# | StrokeWidth 0


[RecreateMeter]
Meter=String
FontFace=Hack NF
FontSize=24
FontColor=#LITECOLOR#
SolidColor=47,47,47,1
Padding=6,6,6,6
AntiAlias=1
Y=6r
X=750r
Text="\uf021"
MouseOverAction=[!SetOption RecreateMeter FontColor #HOVERCOLOR#][!UpdateMeter RecreateMeter][!Redraw]
MouseLeaveAction=[!SetOption RecreateMeter FontColor #LITECOLOR#][!UpdateMeter RecreateMeter][!Redraw]
LeftMouseUpAction=["{path}"]

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



metertext = """

[MeterText{index}]
Meter=String
FontFace=Hack NF
;FontFace=Comic Sans MS
FontSize=12
FontColor=#NORMALCOLOR#
SolidColor=47,47,47,0
Padding=10,10,10,10
AntiAlias=1
Text="{text}"
Y={Y}
X={X}
MouseOverAction=[!SetOption MeterIcon{index} FontColor #HOVERCOLOR#][!SetOption MeterText{index} FontColor #HOVERCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
MouseLeaveAction=[!SetOption MeterIcon{index} FontColor #NORMALCOLOR#][!SetOption MeterText{index} FontColor #NORMALCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
LeftMouseUpAction=["{path}"]
"""
# ;Y={Y}
# ;X={X}

# ;FontFace=Comic Sans MS
#FontFace=Hack NF

metericon = """

[MeterIcon{index}]
Meter=String
FontFace=Hack NF
FontSize=24
FontColor=#NORMALCOLOR#
SolidColor=47,47,47,0
Padding=0,0,0,0
AntiAlias=1
Y=0r
X=-20r
Text="{icon}"
MouseOverAction=[!SetOption MeterIcon{index} FontColor #HOVERCOLOR#][!SetOption MeterText{index} FontColor #HOVERCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
MouseLeaveAction=[!SetOption MeterIcon{index} FontColor #NORMALCOLOR#][!SetOption MeterText{index} FontColor #NORMALCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
LeftMouseUpAction=["{path}"]
"""

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


def get_text(string):
    result =  string.split('\\')[-1]

    if len(result) > 50:
        result = result[:40] + '...' + result[-7:]

    return result 

def exclude(text):
    if re.match(pattern=r'(^~|\.tmp|desktop\.ini|^\.)',string=text):
        return True
    else:
        return False


METERNUM = 0 
def item_factory(t,indent=0):
    global METERNUM
    result = []

    for index,i in enumerate(t):
        
        text = get_text(i['name'])
        # print('x'+text+'x')
        if exclude(text) == True:
            continue;

        print(text,i['name'],indent)

        mt = metertext.format(
            index=METERNUM,
            Y='{Y}',
            X= (indent * 50) + 85,
            text= text,
            path = i['name']
            )
        result.append(mt)

        mi = metericon.format(
            index=METERNUM,
            icon= get_icon(text,icon_map_00),
            path = i['name']
        )

        result.append(mi)

        if 'children' in i.keys():
            METERNUM += 1
            result += item_factory(i['children'],indent=indent+1)
        METERNUM += 1
        
    return result

def item_factory_v2(t,indent=0):
    global METERNUM
    result = []

    for index,i in enumerate(t):
        
        text = get_text(i['name'])
        # print('x'+text+'x')
        if exclude(text) == True:
            continue;

        print(text,i['name'],indent)

        mt = metertext.format(
            index=METERNUM,
            Y='{Y}',
            # X= (indent * 50) + 85,
            X = 40,
            text = (('     ' * indent) + get_icon(text,icon_map_00) + ' ' + text + (' '*75))[:75] + '.',
            path = i['name']
            )
        result.append(mt)

        # mi = metericon.format(
        #     index=METERNUM,
        #     icon= get_icon(text,icon_map_00),
        #     path = i['name']
        # )

        # result.append(mi)

        if 'children' in i.keys():
            METERNUM += 1
            result += item_factory_v2(i['children'],indent=indent+1)
        METERNUM += 1
        
    return result


def main():

    rm = rainmeter
    rm += variables

    tree = get_tree(r'C:\Users\JGarza\Desktop',sort_all = True)
    # pp_tree(tree)
    # print(*tree,sep='\n')
    # print(i)

    # items = item_factory([tree],indent=0)
    items = item_factory([tree],indent=0)
    shape = metershape.format(index=-1,HEIGHT=(20*len(items)) + 40,path=os.path.join(DIR,'refresh.cmd'))
    # shape = metershape.format(index=-1,HEIGHT='{HEIGHT}')
    rm += shape

    # items = item_factory([tree],indent=0)
    for index,i in enumerate(items):
        # print(i)
        try:
            rm += i.format(Y=(index*20) + 13)
        except:
            rm += i
    

    
    save(rm,os.path.join(DIR,'blacktree.ini'))



if __name__ == "__main__":

    main()

