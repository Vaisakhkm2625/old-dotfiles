# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

alias vi='lvim'
alias open='xdg-open'

alias qrpaste="wl-paste | qrencode -t utf8"

export FZF_DEFAULT_COMMAND='fd --color=always --type file --follow --hidden --exclude .git'
export FZF_DEFAULT_OPTS="--ansi"

fcd() {
  local target;
  target="$(fzf)" || return; 
  cd "${target%/*}";
}
