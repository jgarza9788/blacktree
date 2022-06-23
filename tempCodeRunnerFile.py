[RecreateMeter]
Meter=String
FontFace=Hack NF
FontSize=24
FontColor=#LITECOLOR#
SolidColor=47,47,47,1
Padding=6,6,6,6
AntiAlias=1
Y=24r
X=788r
Text="\uf021"
MouseOverAction=[!SetOption RecreateMeter FontColor #HOVERCOLOR#][!UpdateMeter RecreateMeter][!Redraw]
MouseLeaveAction=[!SetOption RecreateMeter FontColor #LITECOLOR#][!UpdateMeter RecreateMeter][!Redraw]
LeftMouseUpAction=["{path}"]