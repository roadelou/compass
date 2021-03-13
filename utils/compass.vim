" Vim syntax highlighting for the compass language.
" Contributors: roadelou
" Creation date: 13-03-2021
" Language: Vim Script


" Quit when a syntax file was already loaded.
if exists("b:current_syntax")
	finish
endif

" case is insignificant
syn case ignore

" Compass Keywords
syn keyword compassIO input output
syn keyword compassStatement each seq par await emit
syn keyword compassModule module
" Operators and special characters
syn match compassSpecial ","
syn match compassSpecial ";"
syn match compassSpecial "<-"
" Esterel Block
syn region compassBlock start="{" end="}" transparent fold

" Class linking
hi def link compassIO String
hi def link compassStatement Statement
hi def link compassModule Type
hi def link compassSpecial Special
hi def link compassIO String

let b:current_syntax = "compass"
