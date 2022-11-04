#!/bin/sh

variety &         # wallpaper setter
picom --config ~/.config/qtile/picom.conf &
dunst &           # notificaiton deamon
#morgen &
todoist &         # my todo app 
exec --no-startup-id kdeconnect-cli & #KDE connect deamon
flameshot &       # screen shot app
#alttab &          # utility for alttabing

teams &           # teams for work
snap run teams &  # teams for collage
