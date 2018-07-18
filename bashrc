# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

alias ne="emacs -nw"
alias la="ls -la"
alias gitkraken="/opt/gitkraken/gitkraken"
alias postman="/opt/postman/postman"

export GIT_EDITOR="emacs -nw"

export LANG=en_US.utf8

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=O

# User specific aliases and functions

PS1='\[\033[00m\][\u@\h \W]\[\033[31;1m\]${?#0}\[\033[m\]\$ '
