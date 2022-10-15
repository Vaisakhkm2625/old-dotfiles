#!/bin/sh

variety &
picom --config ~/.config/qtile/picom.conf &
dunst &
morgen &
exec --no-startup-id kdeconnect-cli &
teams &
snap run teams &
