# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#default config
#ref :- https://github.com/ThomasChiroux/qtile-config/blob/master/config.py



from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen,ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook


import plugins.traverse as pt
import os
import subprocess
#import notify2 #pacman -S python-notify2
    #notify2.init('qtileconfig')
    # n = notify2.Notification("new client opened")
    # n.show()

mod = "mod4"
mod1 = "mod1" #alt
gap = 3
terminal = guess_terminal()

keys = [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
         Key(
             [mod, "shift"],
             "Return",
             lazy.layout.toggle_split(),
             desc="Toggle between split and unsplit sides of stack",
             ),
        # Toggle between different layouts as defined below
        #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

        #---------------my binds----------

        #dmenu
        Key([mod], "r", lazy.spawn('rofi -show drun'), desc="Spawn a command using a prompt widget"),
        Key([mod], "t", lazy.spawn('rofi -show window'), desc="switch to a opened window"),



        #copied
        #Media keys:
        # Sound with amixer
        ###########################(Dont uncoment, idk how this works)  Key([], "XF86AudioMute", lazy.spawn("amixer sset Master toggle")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+")),
        # Screen brightness controls with xbacklight idk why tf not working
        Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),

        # Brightness keys doesnt work either
        Key ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        Key ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

        # Play/pause mdeia control
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
        Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),


        Key([mod,mod1], "space", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
        Key([mod,mod1], "h", lazy.spawn("playerctl position 10-"), desc="Play/Pause player"),
        Key([mod,mod1], "l", lazy.spawn("playerctl position 10+"), desc="Play/Pause player"),

        #opacity
        Key([mod], "minus", lazy.window.down_opacity()),
        Key([mod], "equal", lazy.window.up_opacity()),

        # ---
        Key([mod],"f",lazy.window.toggle_fullscreen(),desc="toggle_fullscreen"),
        Key([mod,"control"],"space",lazy.window.toggle_floating(),desc="toggle_fullscreen"),
        Key([mod], "w",
            lazy.to_screen(0),
            desc='Keyboard focus to monitor 1'
            ),
        Key([mod], "e",
            lazy.to_screen(1),
            desc='Keyboard focus to monitor 2'
            ),
        Key([mod,"shift"],"o",lazy.spawn("shutdown now"),desc="shutdown the system"),


        #my launch things
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod],"b", lazy.spawn("brave"),desc="Launch browser"),
        Key([mod,"shift" ],"d", lazy.spawn("dolphin"),desc="file manager"),
        Key([mod,"shift" ],"s", lazy.spawn("flameshot gui"),desc="screen shot"),
        Key([mod],"s", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/quicksearch.sh")),desc="selection quicksearch"),
        Key([mod],"a", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/scratchpadnotes.sh")),desc="quicknote"),

        #ScratchPad binds----------
        Key([mod], 'z', lazy.group['term'].dropdown_toggle('terminal')),
        Key([mod], 'd', lazy.group['fileman'].dropdown_toggle('filemanager')),
        Key([mod], 'm', lazy.group['dict'].dropdown_toggle('dictionary')),
        Key([mod], 'n', lazy.group['calc'].dropdown_toggle('calculator')),
        ]

# groups = [Group(i) for i in "123456789"]
#static const char *tags[] = { "", "", "", "", "", "", "", "", "" };
groups = [Group("1",label=""),
          Group("2",label=""),
          Group("3",label="" ),
          Group("4",label=""),
          Group("5",label=""),
          Group("6",label=""),
          Group("7",label=""),
          Group("8",label=""),
          Group("9",label=""),
          ]


# Presets: , , ██, ░▒▓▓▒░, 
bar_left = ""
bar_right = ""


# groups = [Group("1",label="CAL"),
            #                 Group("2",label="WWW" ),
            #                 Group("3",label="DEV" ),
            #                 Group("4",label="DOC"),
            #                 Group("5",label="SYS"),
            #                 Group("6",label="VBOX"),
            #                 Group("7",label="TEAMS"),
            #                 Group("8",label="VID"),
            #                 Group("9",label="MUS"),]

scratchpad = [
        #ScratchPads
        ScratchPad("term",[DropDown("terminal","alacritty")]),
        ScratchPad("fileman",[DropDown("filemanager","dolphin")]),
        ScratchPad("dict",[DropDown("dictionary","quick-lookup --selection")]),
        ScratchPad("calc",[DropDown("calculator","qalculate-qt")])
        ]

groups.extend(scratchpad)

@hook.subscribe.client_new
def client_new(client):
    if client.name == 'Mozilla Firefox':
        client.togroup("2") #WWW -> 2
    if 'Teams' in client.name:
        client.togroup("7")
    if 'Brave' in client.name:
        client.togroup("2")
    if 'Morgen' in client.name:
        client.togroup("1")



for i in groups[0:9]:
    keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                # Or, use below if you prefer not to switch to that group.
                # # mod1 + shift + letter of group = move focused window to group
                # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                      #     desc="move focused window to group {}".format(i.name)),
                ]
            )

layouts = [
        layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], margin=gap, border_width=4),
        layout.Max(),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadTall(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        layout.Zoomy(),
        ]

widget_defaults = dict(
        font="sans",
        fontsize=14,
        padding=3,
        )

extension_defaults = widget_defaults.copy()

screens = [
        Screen(
            top=bar.Bar(
                [ 
                    widget.Spacer(length=10),
                    widget.CurrentLayout(),
                    widget.GroupBox(disable_drag = True),
                    widget.Prompt(),
                    #widget.Spacer(background="#00000000" ),
                    widget.Spacer(),
                    #widget.WindowName(format = '{name}'),
                    widget.TaskList(theme_mode="preferred"),
                    #widget.Spacer(background="#00000000" ),
                    widget.Spacer(),
                    widget.Chord(
                        chords_colors={
                            "launch": ("#ff0000", "#ffffff"),
                            },
                        name_transform=lambda name: name.upper(),
                        ),
                    #widget.TextBox("default config", name="default"),
                    widget.TextBox("vaisakh", name="default",foreground="#d75f5f"),
                    # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                    # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                    # widget.StatusNotifier(),
                    widget.Systray(),
                    widget.Volume(),
                    widget.Net(interface="wlp0s20f3",format=" {down}↓↑{up}", width= 108),
                    #widget.CPUGraph(),
                    #widget.BatteryIcon(),
                    #widget.Battery(notify_below=10,update_interval=10),
                    widget.Battery(format="{char} {percent:2.0%}",discharge_char="", charge_char="",full_char="",notify_below=10,update_interval=10),
                    #widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                    widget.Clock(format="%Y-%m-%d" ),
                    # widget.TextBox("",padding=0,fontsize=20, name="default",foreground="#d75f5f"),
                    widget.Clock(background="#c4a7e7", foreground="#191724", format="%I:%M%p", update_interval=60.0),
                    widget.QuickExit(default_text='⏻',  countdown_format='[{} seconds remaining]',background="#ff0000"),
                    widget.Spacer(length=1,background="#ff0000")
                    ],
                24,
                margin=gap*2,
                #background=["#0000FF","#000000", "#FFFFFF"]
                background="#000011aa",
                border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                 #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            right=bar.Gap(gap), 
            left=bar.Gap(gap),
            bottom=bar.Gap(gap)
            ),
        ]

# Drag floating layouts.
mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
        ]



dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            ]
        )


floating_window_index = 0

def float_cycle(qtile, forward: bool):
    global floating_window_index
    floating_windows = []
    for window in qtile.current_group.windows:
        if window.floating:
            floating_windows.append(window)
    if not floating_windows:
        return
    floating_window_index = min(floating_window_index, len(floating_windows) -1)
    if forward:
        floating_window_index += 1
    else:
        floating_window_index += 1
    if floating_window_index >= len(floating_windows):
        floating_window_index = 0
    if floating_window_index < 0:
        floating_window_index = len(floating_windows) - 1
    win = floating_windows[floating_window_index]
    win.cmd_bring_to_front()
    win.cmd_focus()

@lazy.function
def float_cycle_backward(qtile):
    float_cycle(qtile, False)

@lazy.function
def float_cycle_forward(qtile):
    float_cycle(qtile, True)

keys.extend( [ Key([mod, "mod1"], "period", float_cycle_forward),
    Key([mod, "mod1"], "comma", float_cycle_backward),
])



auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#autostart
@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

keys.extend([
    Key([mod], 'k', lazy.function(pt.up)),
    Key([mod], 'j', lazy.function(pt.down)),
    Key([mod], 'h', lazy.function(pt.left)),
    Key([mod], 'l', lazy.function(pt.right)),
])

