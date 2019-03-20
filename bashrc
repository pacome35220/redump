# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

alias ne="emacs -nw"
alias la="ls -la"
alias gitkraken="/opt/gitkraken/gitkraken"
alias postman="/opt/postman/Postman"
alias disas="objdump -drwCS -Mintel"

norminette() {
    src=$(find ./ -name "*.c")
    include=$(find ./ -name "*.h")
    norminette.pl -q --no-tree --show-types --showfile --ignore SPDX_LICENSE_TAG,BLOCK_COMMENT_STYLE,CONST_STRUCT,NEW_TYPEDEFS,LEADING_SPACE,CODE_INDENT,SUSPECT_CODE_INDENT --file $src $include
}

export LANG=en_US.utf8

if [[ $PATH != *"node_modules/.bin"* ]]; then
    export PATH=./node_modules/.bin:$PATH
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=O

# User specific aliases and functions

PS1='\[\033[00m\][\u@\h \W]\[\033[31;1m\]${?#0}\[\033[m\]\$ '
