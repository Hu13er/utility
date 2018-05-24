# My Custom RC:
# 

# VIM
alias vim=nvim
alias vi=vim

# Note
alias note=eton

# Open
alias xop=xdg-open

# Go script
alias gor=go run

# Clipboard
alias setclip="xclip -selection c"
alias getclip="xclip -selection c -o"

function myip () {
	curl ifconfig.me
}

function newtorip () {
	echo -e 'AUTHENTICATE ""\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051
}

function start_cmus () {
	cmus --listen 0.0.0.0:1212
}

# DUAL Monitor
function cdualm () {
    xrandr --output eDP1 --auto --output HDMI2 --auto --panning 4608x2592+2560+0 --scale 1.8x1.8 --right-of eDP1
}

function dualm () {
    DX=$( echo "1920 * $1 / 1" | bc )
    DY=$( echo "1080 * $1 / 1" | bc )

    PADDING="${DX}x${DY}+2560+0"
    SCALE="${1}x${1}"

    echo "Padding: \t$PADDING"
    echo "Scale:   \t$SCALE"

    xrandr --output eDP1 --auto --output HDMI2 --auto --panning $PADDING --scale $SCALE --right-of eDP1
    return $?
}

