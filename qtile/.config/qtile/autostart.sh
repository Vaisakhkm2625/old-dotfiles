#!/bin/sh

variety &
picom --config ~/.config/qtile/picom.conf &
dunst &
#morgen &
todoist &
exec --no-startup-id kdeconnect-cli &
alttab &
teams &
snap run teams &
