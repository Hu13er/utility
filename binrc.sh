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

