""" 
Remove spaces to both keys and values for below dictionary

dict1 = {
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    ",
" A " : "  A    "
}
"""
#k for keys, v for values
dict((k.strip(), v.strip()) for k, v in dict1.items())