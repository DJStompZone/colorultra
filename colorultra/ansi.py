# Copyright Jonathan Hartley 2013, DJ Stomp 2026. BSD 3-Clause license, see LICENSE file.
r'''
.-----------------------------------------.
.                                         .
.   ,-.     .         .  . . .            .
.  /        |         |  | | |            .
.  |    ,-. | ,-. ;-. |  | | |-  ;-. ,-:  .
.  \    | | | | | |   |  | | |   |   | |  .
.   `-' `-' ' `-' '   `--` ' `-' '   `-`  .
.                                         .
.              2026 DJ Stomp              .
.           "No Rights Reserved"          .
.                                         .
...........................................

This module generates ANSI character codes to printing colors to terminals.
See: http://en.wikipedia.org/wiki/ANSI_escape_code
'''

CSI = '\033['
OSC = '\033]'
BEL = '\a'
SGR = '38;5;'


def code_to_chars(code):
    return f'{CSI}{code}m'

def set_title(title):
    return OSC + '2;' + title + BEL

def clear_screen(mode=2):
    return CSI + str(mode) + 'J'

def clear_line(mode=2):
    return CSI + str(mode) + 'K'


class AnsiCodes(object):
    def __init__(self):
        # the subclasses declare class attributes which are numbers.
        # Upon instantiation we define instance attributes, which are the same
        # as the class attributes but wrapped with the ANSI escape sequence
        prefix = SGR if '__SGR__' in dir(self) else ''
        for name in dir(self):
            if not name.startswith('_'):
                value = f'{prefix}{getattr(self, name)}'
                setattr(self, name, code_to_chars(value))


class AnsiCursor(object):
    def UP(self, n=1):
        return CSI + str(n) + 'A'
    def DOWN(self, n=1):
        return CSI + str(n) + 'B'
    def FORWARD(self, n=1):
        return CSI + str(n) + 'C'
    def BACK(self, n=1):
        return CSI + str(n) + 'D'
    def POS(self, x=1, y=1):
        return CSI + str(y) + ';' + str(x) + 'H'

class AnsiSGR(AnsiCodes):
    __SGR__           = True
    BLACK             = 0
    MAROON            = 1
    GREEN             = 2
    OLIVE             = 3
    NAVY              = 4
    PURPLE            = 5
    TEAL              = 6
    SILVER            = 7
    GREY              = 8
    RED               = 9
    LIME              = 10
    YELLOW            = 11
    BLUE              = 12
    FUCHSIA           = 13
    AQUA              = 14
    WHITE             = 15
    GREY0             = 16
    NAVYBLUE          = 17
    DARKBLUE          = 18
    BLUE3             = 19
    BLUE4             = 20
    BLUE1             = 21
    DARKGREEN         = 22
    DEEPSKYBLUE4      = 23
    DEEPSKYBLUE5      = 24
    DEEPSKYBLUE6      = 25
    DODGERBLUE3       = 26
    DODGERBLUE2       = 27
    GREEN4            = 28
    SPRINGGREEN4      = 29
    TURQUOISE4        = 30
    DEEPSKYBLUE3      = 31
    DEEPSKYBLUE7      = 32
    DODGERBLUE1       = 33
    GREEN3            = 34
    SPRINGGREEN3      = 35
    DARKCYAN          = 36
    LIGHTSEAGREEN     = 37
    DEEPSKYBLUE2      = 38
    DEEPSKYBLUE1      = 39
    GREEN5            = 40
    SPRINGGREEN5      = 41
    SPRINGGREEN2      = 42
    CYAN3             = 43
    DARKTURQUOISE     = 44
    TURQUOISE2        = 45
    GREEN1            = 46
    SPRINGGREEN6      = 47
    SPRINGGREEN1      = 48
    MEDIUMSPRINGGREEN = 49
    CYAN2             = 50
    CYAN1             = 51
    DARKRED           = 52
    DEEPPINK4         = 53
    PURPLE4           = 54
    PURPLE5           = 55
    PURPLE3           = 56
    BLUEVIOLET        = 57
    ORANGE4           = 58
    GREY37            = 59
    MEDIUMPURPLE4     = 60
    SLATEBLUE3        = 61
    SLATEBLUE4        = 62
    ROYALBLUE1        = 63
    CHARTREUSE4       = 64
    DARKSEAGREEN4     = 65
    PALETURQUOISE4    = 66
    STEELBLUE         = 67
    STEELBLUE3        = 68
    CORNFLOWERBLUE    = 69
    CHARTREUSE3       = 70
    DARKSEAGREEN5     = 71
    CADETBLUE         = 72
    CADETBLUE2        = 73
    SKYBLUE3          = 74
    STEELBLUE1        = 75
    CHARTREUSE5       = 76
    PALEGREEN3        = 77
    SEAGREEN3         = 78
    AQUAMARINE3       = 79
    MEDIUMTURQUOISE   = 80
    STEELBLUE2        = 81
    CHARTREUSE2       = 82
    SEAGREEN2         = 83
    SEAGREEN1         = 84
    SEAGREEN4         = 85
    AQUAMARINE1       = 86
    DARKSLATEGRAY2    = 87
    DARKRED2          = 88
    DEEPPINK5         = 89
    DARKMAGENTA       = 90
    DARKMAGENTA2      = 91
    DARKVIOLET        = 92
    PURPLE2           = 93
    ORANGE5           = 94
    LIGHTPINK4        = 95
    PLUM4             = 96
    MEDIUMPURPLE3     = 97
    MEDIUMPURPLE5     = 98
    SLATEBLUE1        = 99
    YELLOW4           = 100
    WHEAT4            = 101
    GREY53            = 102
    LIGHTSLATEGREY    = 103
    MEDIUMPURPLE      = 104
    LIGHTSLATEBLUE    = 105
    YELLOW5           = 106
    DARKOLIVEGREEN3   = 107
    DARKSEAGREEN      = 108
    LIGHTSKYBLUE3     = 109
    LIGHTSKYBLUE4     = 110
    SKYBLUE2          = 111
    CHARTREUSE6       = 112
    DARKOLIVEGREEN4   = 113
    PALEGREEN4        = 114
    DARKSEAGREEN3     = 115
    DARKSLATEGRAY3    = 116
    SKYBLUE1          = 117
    CHARTREUSE1       = 118
    LIGHTGREEN        = 119
    LIGHTGREEN2       = 120
    PALEGREEN1        = 121
    AQUAMARINE2       = 122
    DARKSLATEGRAY1    = 123
    RED3              = 124
    DEEPPINK6         = 125
    MEDIUMVIOLETRED   = 126
    MAGENTA3          = 127
    DARKVIOLET2       = 128
    PURPLE6           = 129
    DARKORANGE3       = 130
    INDIANRED         = 131
    HOTPINK3          = 132
    MEDIUMORCHID3     = 133
    MEDIUMORCHID      = 134
    MEDIUMPURPLE2     = 135
    DARKGOLDENROD     = 136
    LIGHTSALMON3      = 137
    ROSYBROWN         = 138
    GREY63            = 139
    MEDIUMPURPLE6     = 140
    MEDIUMPURPLE1     = 141
    GOLD3             = 142
    DARKKHAKI         = 143
    NAVAJOWHITE3      = 144
    GREY69            = 145
    LIGHTSTEELBLUE3   = 146
    LIGHTSTEELBLUE    = 147
    YELLOW3           = 148
    DARKOLIVEGREEN5   = 149
    DARKSEAGREEN6     = 150
    DARKSEAGREEN2     = 151
    LIGHTCYAN3        = 152
    LIGHTSKYBLUE1     = 153
    GREENYELLOW       = 154
    DARKOLIVEGREEN2   = 155
    PALEGREEN2        = 156
    DARKSEAGREEN7     = 157
    DARKSEAGREEN1     = 158
    PALETURQUOISE1    = 159
    RED4              = 160
    DEEPPINK3         = 161
    DEEPPINK7         = 162
    MAGENTA4          = 163
    MAGENTA5          = 164
    MAGENTA2          = 165
    DARKORANGE4       = 166
    INDIANRED2        = 167
    HOTPINK4          = 168
    HOTPINK2          = 169
    ORCHID            = 170
    MEDIUMORCHID1     = 171
    ORANGE3           = 172
    LIGHTSALMON4      = 173
    LIGHTPINK3        = 174
    PINK3             = 175
    PLUM3             = 176
    VIOLET            = 177
    GOLD4             = 178
    LIGHTGOLDENROD3   = 179
    TAN               = 180
    MISTYROSE3        = 181
    THISTLE3          = 182
    PLUM2             = 183
    YELLOW6           = 184
    KHAKI3            = 185
    LIGHTGOLDENROD2   = 186
    LIGHTYELLOW3      = 187
    GREY84            = 188
    LIGHTSTEELBLUE1   = 189
    YELLOW2           = 190
    DARKOLIVEGREEN1   = 191
    DARKOLIVEGREEN6   = 192
    DARKSEAGREEN8     = 193
    HONEYDEW2         = 194
    LIGHTCYAN1        = 195
    RED1              = 196
    DEEPPINK2         = 197
    DEEPPINK1         = 198
    DEEPPINK8         = 199
    MAGENTA6          = 200
    MAGENTA1          = 201
    ORANGERED1        = 202
    INDIANRED1        = 203
    INDIANRED3        = 204
    HOTPINK           = 205
    HOTPINK5          = 206
    MEDIUMORCHID2     = 207
    DARKORANGE        = 208
    SALMON1           = 209
    LIGHTCORAL        = 210
    PALEVIOLETRED1    = 211
    ORCHID2           = 212
    ORCHID1           = 213
    ORANGE1           = 214
    SANDYBROWN        = 215
    LIGHTSALMON1      = 216
    LIGHTPINK1        = 217
    PINK1             = 218
    PLUM1             = 219
    GOLD1             = 220
    LIGHTGOLDENROD4   = 221
    LIGHTGOLDENROD5   = 222
    NAVAJOWHITE1      = 223
    MISTYROSE1        = 224
    THISTLE1          = 225
    YELLOW1           = 226
    LIGHTGOLDENROD1   = 227
    KHAKI1            = 228
    WHEAT1            = 229
    CORNSILK1         = 230
    GREY100           = 231
    GREY3             = 232
    GREY7             = 233
    GREY11            = 234
    GREY15            = 235
    GREY19            = 236
    GREY23            = 237
    GREY27            = 238
    GREY30            = 239
    GREY35            = 240
    GREY39            = 241
    GREY42            = 242
    GREY46            = 243
    GREY50            = 244
    GREY54            = 245
    GREY58            = 246
    GREY62            = 247
    GREY66            = 248
    GREY70            = 249
    GREY74            = 250
    GREY78            = 251
    GREY82            = 252
    GREY85            = 253
    GREY89            = 254
    GREY93            = 255

class AnsiFore(AnsiCodes):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 90
    LIGHTRED_EX     = 91
    LIGHTGREEN_EX   = 92
    LIGHTYELLOW_EX  = 93
    LIGHTBLUE_EX    = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX    = 96
    LIGHTWHITE_EX   = 97


class AnsiBack(AnsiCodes):
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 100
    LIGHTRED_EX     = 101
    LIGHTGREEN_EX   = 102
    LIGHTYELLOW_EX  = 103
    LIGHTBLUE_EX    = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX    = 106
    LIGHTWHITE_EX   = 107


class AnsiStyle(AnsiCodes):
    BRIGHT    = 1
    DIM       = 2
    NORMAL    = 22
    RESET_ALL = 0

Sgr    = AnsiSGR()
Fore   = AnsiFore()
Back   = AnsiBack()
Style  = AnsiStyle()
Cursor = AnsiCursor()
