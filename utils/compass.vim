" Vim syntax highlighting for the compass language.
" Contributors: roadelou
" Creation date: 13-03-2021
" Language: Vim Script

" Depending how your setup is organized, you might need to add the following
" line somewhere in your configuration.
" au! BufRead,BufNewFile *.cmps set filetype=compass

" Quit when a syntax file was already loaded.
if exists("b:current_syntax")
	finish
endif

" case is insignificant
syn case ignore

" Compass Keywords
syn keyword compassIO input output
syn keyword compassStatement each seq par await emit local
syn keyword compassStatement if elif else endif
syn keyword compassModule module endmodule submodule extern
" Operators and special characters
syn match compassSpecial ","
syn match compassSpecial ";"
syn match compassSpecial "<-"
syn match compassSpecial "=="
syn match compassSpecial "+"
syn match compassSpecial "-"
syn match compassSpecial "*"
syn match compassSpecial "/"
syn match compassSpecial "%"
syn match compassSpecial "||"
syn match compassSpecial "&&"
syn match compassSpecial "!"
syn match compassComment "#.*$"

" Esterel Block
syn region compassBlock start="{" end="}" transparent fold
syn region compassModule start="module" end="endmodule" transparent fold
syn region compassModule start="if" end="endif" transparent fold

" Class linking
hi def link compassIO String
hi def link compassStatement Statement
hi def link compassModule Type
hi def link compassSpecial Special
hi def link compassIO String
hi def link compassComment Comment

let b:current_syntax = "compass"
