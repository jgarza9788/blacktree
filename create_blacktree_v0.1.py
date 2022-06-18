
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

"""

variables = """

[variables]
RECSHAPE = 25,25,400,50,10
BACKGROUNDCOLOR = 0,0,0,200


NORMALCOLOR = "255,255,255,255"
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

[MeterShapes{index}]
Meter=Shape
Shape=Rectangle 25,25,800,{HEIGHT},10 | Fill Color #BACKGROUNDCOLOR# | StrokeWidth 0

"""
# ;MouseOverAction=[!SetOption MeterShapes{index} Shape "Rectangle #RECSHAPE# | Fill Color {HOVERCOLOR} | StrokeWidth 0"][!SetOption MeterIcon{index} FontColor #ICONHOVERCOLOR#][!SetOption MeterText{index} FontColor #TEXTHOVERCOLOR#][!UpdateMeter MeterShapes{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterShapes{index} Shape "Rectangle #RECSHAPE# | Fill Color #NORMALCOLOR# | StrokeWidth 0"][!SetOption MeterIcon{index} FontColor #ICONCOLOR#][!SetOption MeterText{index} FontColor #TEXTCOLOR#][!UpdateMeter MeterShapes{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;MouseOverAction=[!SetOption MeterIcon{index} FontColor {HOVERCOLOR}][!SetOption MeterText{index} FontColor {HOVERCOLOR}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterIcon{index} FontColor #ICONCOLOR#][!SetOption MeterText{index} FontColor #TEXTCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
# ;LeftMouseUpAction=["{path}"]
# ;Y={Y}

# ;MouseOverAction=[!SetOption MeterText Text "{icon0} {text}"][!SetOption MeterShapes Shape "Rectangle 50,50,500,100,10 | Fill Color #RED# | StrokeWidth 0"][!UpdateMeter MeterText][!UpdateMeter MeterShapes][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterText Text "{icon1} {text}"][!SetOption MeterShapes Shape "Rectangle 50,50,500,100,10 | Fill Color #WHITE# | StrokeWidth 0"][!UpdateMeter MeterText][!UpdateMeter MeterShapes][!Redraw]


metericon = """

[MeterIcon{index}]
Meter=String
FontFace=Hack NF
FontSize=24
FontColor=#NORMALCOLOR#
SolidColor=47,47,47,0
Padding=6,6,6,6
AntiAlias=1
Y=-12r
X=-32r
Text="{icon}"
MouseOverAction=[!SetOption MeterIcon{index} FontColor #HOVERCOLOR#][!SetOption MeterText{index} FontColor #HOVERCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
MouseLeaveAction=[!SetOption MeterIcon{index} FontColor #NORMALCOLOR#][!SetOption MeterText{index} FontColor #NORMALCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
LeftMouseUpAction=["{path}"]
"""

metertext = """

[MeterText{index}]
Meter=String
FontFace=Hack NF
;FontFace=Comic Sans MS
FontSize=12
FontColor=#NORMALCOLOR#
SolidColor=47,47,47,0
Padding=6,6,6,6
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


yshift = 60
ytextshift = 40
yiconshift = 55
xtextshift=95
xiconshift=60

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


def main():

    rm = rainmeter
    rm += variables

    tree = get_tree(r'C:\Users\JGarza\Desktop',sort_all = True)
    # pp_tree(tree)
    # print(*tree,sep='\n')
    # print(i)

    items = item_factory([tree],indent=0)
    shape = metershape.format(index=-1,HEIGHT=(20*len(items)) + 40)
    # shape = metershape.format(index=-1,HEIGHT='{HEIGHT}')
    rm += shape

    # items = item_factory([tree],indent=0)
    for index,i in enumerate(items):
        # print(i)
        try:
            rm += i.format(Y=(index*20) + 50)
        except:
            rm += i
    

    # files = get_files(r'C:\Users\JGarza\Desktop',add_root=True,exclude_pattern='^(__|@|\.)')
    # files.append(get_recycle_bin_link())
    # files.append(get_run_refresh(__file__))
    # print(*files,sep='\n')

    # for index,f in enumerate(files):
    #     Y = yshift*index
    #     shape = metershape
    #     # shape = shape.format(index=index,path=f,Y=Y)
    #     shape = shape.format(index=index,path=f,Y=Y,HOVERCOLOR=COLORS[index % len(COLORS)])
    #     icon = metericon
    #     icon = icon.format(index=index,Y=(Y+yiconshift),X=xiconshift,icon=get_icon(f,icon_map_00))
    #     text = metertext
    #     text = text.format(index=index,Y=(Y+ytextshift),X=xtextshift,text=get_text(f))
    #     rm += shape
    #     rm += icon
    #     rm += text
    
    save(rm,os.path.join(DIR,'backtree.ini'))



if __name__ == "__main__":
    # print(__file__)
    # quit()
    main()

    # t = '0123456789abcdefghijklmnop'
    # print(t[:5] + '...' + t[-5:])
