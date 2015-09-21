# -*- coding: utf-8 -*-

"Test all WinAnsi encoding (1252) charter set for standard predefined font"

#PyFPDF-cover-test:format=PDF
#PyFPDF-cover-test:fn=e1252.pdf
#PyFPDF-cover-test:hash=84810c2c1d1169c73e6803cbc9390b1f

import common # test utilities
from fpdf import FPDF

import sys
import os, os.path

if common.PY3K:
    unichr = chr

# PDF 1.7, annex D.1, pages 997-1000
SYMBOLS = [
    # page 997, left
    [u"A", "A", 0o101],
    [u"Æ", "AE", 0o306],
    [u"Á", "Aacute", 0o301],
    [u"Â", "Acircumflex", 0o302],
    [u"Ä", "Adieresis", 0o304],
    [u"À", "Agrave", 0o300],
    [u"Å", "Aring", 0o305],
    [u"Ã", "Atilde", 0o303],   
    [u"B", "B", 0o102],
    [u"C", "C", 0o103],
    [u"Ç", "Ccedilla", 0o307],
    [u"D", "D", 0o104],
    [u"E", "E", 0o105],
    [u"É", "Eacute", 0o311],
    [u"Ê", "Ecircumflex", 0o312],
    [u"Ë", "Edieresis", 0o313],
    [u"È", "Egrave", 0o310],
    [u"Ð", "Eth", 0o320],
    [u"€", "Euro", 0o200],
    [u"F", "F", 0o106],
    [u"G", "G", 0o107],
    [u"H", "H", 0o110],
    [u"I", "I", 0o111],
    [u"Í", "Iacute", 0o315],
    [u"Î", "Icircumflex", 0o316],
    [u"Ï", "Idieresis", 0o317],
    [u"Ì", "Igrave", 0o314],
    [u"J", "J", 0o112],
    [u"K", "K", 0o113],
    [u"L", "L", 0o114],
    [u"Ł", "Lslash", None], # No WinAnsi code
    [u"M", "M", 0o115],
    [u"N", "N", 0o116],
    [u"Ñ", "Ntilde", 0o321],
    [u"O", "O", 0o117],
    # page 997, right
    [u"Œ", "OE", 0o214],
    [u"Ó", "Oacute", 0o323],
    [u"Ô", "Ocircumflex", 0o324],
    [u"Ö", "Odieresis", 0o326],
    [u"Ò", "Ograve", 0o322],
    [u"Ø", "Oslash", 0o330],
    [u"Õ", "Otilde", 0o325],
    [u"P", "P", 0o120],
    [u"Q", "Q", 0o121],
    [u"R", "R", 0o122],
    [u"S", "S", 0o123],
    [u"Š", "Scaron", 0o212],
    [u"T", "T", 0o124],
    [u"Þ", "Thorn", 0o336],
    [u"U", "U", 0o125],
    [u"Ú", "Uacute", 0o332],
    [u"Û", "Ucircumflex", 0o333],
    [u"Ü", "Udieresis", 0o334],
    [u"Ù", "Ugrave", 0o331],
    [u"V", "V", 0o126],
    [u"W", "W", 0o127],
    [u"X", "X", 0o130],
    [u"Y", "Y", 0o131],
    [u"Ý", "Yacute", 0o335],
    [u"Ÿ", "Ydieresis", 0o237],
    [u"Z", "Z", 0o132],
    [u"Ž", "Zcaron", 0o216],
    [u"a", "a", 0o141],
    [u"á", "aacute", 0o341],
    [u"â", "acircumflex", 0o342],
    [u" ́", "acute", 0o264], # Special
    [u"ä", "adieresis", 0o344],
    [u"æ", "ae", 0o346],
    [u"à", "agrave", 0o340],
    [u"&", "ampersand", 0o46],
    # page 998, left
    [u"å", "aring", 0o345],
    [u"^", "asciicircum", 0o136],
    [u"~", "asciitilde", 0o176],
    [u"*", "asterisk", 0o52],
    [u"@", "at", 0o100],
    [u"ã", "atilde", 0o343],
    [u"b", "b", 0o142],
    [u"\\", "backslash", 0o134],
    [u"|", "bar", 0o174],
    [u"{", "braceleft", 0o173],
    [u"}", "braceright", 0o175],
    [u"[", "bracketleft", 0o133],
    [u"]", "bracketright", 0o135],
    [u" ̆", "breve", None], # # Special
    [u"¦", "brokenbar", 0o246],
    [u"•", "bullet", 0o225],
    [u"c", "c", 0o143],
    [u"ˇ", "caron", None],
    [u"ç", "ccedilla", 0o347],
    [u" ̧", "cedilla", 0o270],
    [u"¢", "cent", 0o242],
    [u"ˆ", "circumflex", 0o210],
    [u":", "colon", 0o72],
    [u",", "comma", 0o54],
    [u"©", "copyright", 0o251],
    [u"¤", "currency", 0o244],
    [u"d", "d", 0o144],
    [u"†", "dagger", 0o206],
    [u"‡", "daggerdbl", 0o207],
    [u"°", "degree", 0o260],
    [u" ̈", "dieresis", 0o250],
    [u"÷", "divide", 0o367],
    [u"$", "dollar", 0o44],
    [u" ̇", "dotaccent", None],
    [u"ı", "dotlessi", None],
    [u"e", "e", 0o145],
    [u"é", "eacute", 0o351],
    # page 998, right
    [u"ê", "ecircumflex", 0o352],
    [u"ë", "edieresis", 0o353],
    [u"è", "egrave", 0o350],
    [u"8", "eight", 0o70],
    [u"\u2026", "ellipsis", 0o205], # ...
    [u"—", "emdash", 0o227],
    [u"–", "endash", 0o226],
    [u"=", "equal", 0o75],
    [u"ð", "eth", 0o360],
    [u"!", "exclam", 0o41],
    [u"¡", "exclamdown", 0o241],
    [u"f", "f", 0o146],
    [u"\ufb01", "fi", None], # fi
    [u"5", "five", 0o65],
    [u"\ufb02", "fl", None], # fl
    [u"ƒ", "florin", 0o203],
    [u"4", "four", 0o64],
    [u"⁄", "fraction", None],
    [u"g", "g", 0o147],
    [u"ß", "germandbls", 0o337],
    [u"`", "grave", 0o140],
    [u">", "greater", 0o76],
    [u"«", "guillemotleft", 0o253],
    [u"»", "guillemotright", 0o273],
    [u"‹", "guilsinglleft", 0o213],
    [u"›", "guilsinglright", 0o233],
    [u"h", "h", 0o150],
    [u" ̋", "hungarumlaut", None],
    [u"-", "hyphen", 0o55],
    [u"i", "i", 0o151],
    [u"í", "iacute", 0o355],
    [u"î", "icircumflex", 0o356],
    [u"ï", "idieresis", 0o357],
    [u"ì", "igrave", 0o354],
    [u"j", "j", 0o152],
    [u"k", "k", 0o153],
    [u"l", "l", 0o154],
    # page 999, left
    [u"<", "less", 0o74],
    [u"¬", "logicalnot", 0o254],
    [u"ł", "lslash", None],
    [u"m", "m", 0o155],
    [u" ̄", "macron", 0o257],
    [u"−", "minus", None],
    [u"μ", "mu", 0o265],
    [u"×", "multiply", 0o327],
    [u"n", "n", 0o156],
    [u"9", "nine", 0o71],
    [u"ñ", "ntilde", 0o361],
    [u"#", "numbersign", 0o43],
    [u"o", "o", 0o157],
    [u"ó", "oacute", 0o363],
    [u"ô", "ocircumflex", 0o364],
    [u"ö", "odieresis", 0o366],
    [u"œ", "oe", 0o234],
    [u" ̨", "ogonek", None],
    [u"ò", "ograve", 0o362],
    [u"1", "one", 0o61],
    [u"\xbd", "onehalf", 0o275], # 1/2
    [u"\xbc", "onequarter", 0o274], # 1/4
    [u"\xb9", "onesuperior", 0o271],
    [u"\xaa", "ordfeminine", 0o252],
    [u"\xba", "ordmasculine", 0o272],
    [u"ø", "oslash", 0o370],
    [u"õ", "otilde", 0o365],
    [u"p", "p", 0o160],
    [u"¶", "paragraph", 0o266],
    [u"(", "parenleft", 0o50],
    [u")", "parenright", 0o51],
    [u"%", "percent", 0o45],
    [u".", "period", 0o56],
    [u"·", "periodcentered", 0o267],
    [u"‰", "perthousand", 0o211],
    [u"+", "plus", 0o53],
    [u"±", "plusminus", 0o261],
    # page 999, right
    [u"q", "q", 0o161],
    [u"?", "question", 0o77],
    [u"¿", "questiondown", 0o277],
    [u"\"", "quotedbl", 0o42],
    [u"„", "quotedblbase", 0o204],
    [u"“", "quotedblleft", 0o223],
    [u"”", "quotedblright", 0o224],
    [u"‘", "quoteleft", 0o221],
    [u"’", "quoteright", 0o222],
    [u"‚", "quotesinglbase", 0o202],
    [u"'", "quotesingle", 0o47],
    [u"r", "r", 0o162],
    [u"®", "registered", 0o256],
    [u" ̊", "ring", 0o36],
    [u"s", "s", 0o163],
    [u"š", "scaron", 0o232],
    [u"§", "section", 0o247],
    [u";", "semicolon", 0o73],
    [u"7", "seven", 0o67],
    [u"6", "six", 0o66],
    [u"/", "slash", 0o57],
    [u" ", "space", 0o40],
    [u"£", "sterling", 0o243],
    [u"t", "t", 0o164],
    [u"þ", "thorn", 0o376],
    [u"3", "three", 0o63],
    [u"\xbe", "threequarters", 0o276], # 3/4
    [u"\xb3", "threesuperior", 0o263],
    [u"˜", "tilde", 0o230],
    [u"\u2122", "trademark", 0o231], # TM
    [u"2", "two", 0o62],
    [u"\xb2", "twosuperior", 0o262],
    [u"u", "u", 0o165],
    [u"ú", "uacute", 0o372],
    [u"û", "ucircumflex", 0o373],
    [u"ü", "udieresis", 0o374],
    [u"ù", "ugrave", 0o371],
    # page 1000, left
    [u"_", "underscore", 0o137],
    [u"v", "v", 0o166],
    [u"w", "w", 0o167],
    [u"x", "x", 0o170],
    [u"y", "y", 0o171],
    [u"ý", "yacute", 0o375],
    # page 1000, right
    [u"ÿ", "ydieresis", 0o377],
    [u"¥", "yen", 0o245],
    [u"z", "z", 0o172],
    [u"ž", "zcaron", 0o236],
    [u"0", "zero", 0o60],
            
    
]

class MyPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.write(10, "Latin Character Set and WinAnsiEncoding (1252)")
        self.ln(10)
        self.set_font('Arial', '', 14)
        self.write(10, "PDF 1.7, annex D.1, pages 997-1000")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s / {nb}' % self.page_no(), 0, 0, 'C')    

@common.add_unittest
def dotest(outputname, nostamp):
    pdf = MyPDF()
    pdf.alias_nb_pages()
    pdf.compress = False
    use_exfont = False
    if nostamp:
        pdf._putinfo = lambda: common.test_putinfo(pdf)
    else:
        # This font used if:
        # 1. It exists
        # 2. In user mode
        fp = os.path.join(common.basepath, 'font/DejaVuSans.ttf')
        if os.path.exists(fp):
            use_exfont = True
            pdf.add_font('DejaVu', '', fp, uni = True)
    pdf.set_fill_color(150)
    pdf.add_page()

    def tabletop():
        pdf.set_font('Arial', 'B', 8)
        if use_exfont:
            pdf.cell(12, 8, txt = "DejaVu", border = 1, align = "C")
        pdf.cell(12, 8, txt = "Type 1", border = 1, align = "C")
        pdf.cell(12, 8, txt = "Code", border = 1, align = "C")
        pdf.cell(12, 8, txt = "1252", border = 1, align = "C")
        pdf.cell(35, 8, txt = "Name", border = 1, align = "C")
        pdf.cell(20, 8, txt = "WinAnsi", border = 1, align = "C")
        pdf.cell(20, 8, txt = "Unicode", border = 1, align = "C")
        pdf.ln()
    
    pdf.table_cnt = 0
    def print_char(char, name, code):
        #print(repr(char), name, code)
        if pdf.table_cnt > 28:
            pdf.add_page()
            pdf.table_cnt = 0
        if pdf.table_cnt == 0:
            tabletop()
        pdf.table_cnt += 1
        if len(char) != 1:
            if len(char) == 2 and char[:1] == u" ":
                ocode = ord(char[1])            
                if code is not None:
                    txt = unichr(code)
                txt = "O" + char[1:]
            else:
                raise Exception("bad charter for \"" + name + "\" " + repr(char))
        else:
            ocode = ord(char)
            txt = char

        if use_exfont:
            pdf.set_font('DejaVu', '', 14)
            pdf.cell(12, 8, txt = char, border = 1, align = "R")
        
        
        pdf.set_font('Arial', '', 14)

        # as latin-1 charter
        bg = False
        try:
            txt.encode("latin1")
        except:
            txt = ""
            bg = True
        pdf.cell(12, 8, txt = txt, border = 1, align = "R", fill = bg)

        # as winansi code
        if code is not None:
            txt = chr(code)
        else:
            txt = ""
        pdf.cell(12, 8, txt = txt, border = 1, align = "R")

        # as 1252
        bg = False
        try:
            txt = char.encode("windows-1252").decode("latin-1")
        except:
            txt = ""
            bg = True
        pdf.cell(12, 8, txt = txt, border = 1, align = "R", fill = bg)

        # charter name
        pdf.cell(35, 8, txt = name, border = 1, align = "L")
        hcode = ""
        alt = ""
        if code is not None:
            hcode = "0x%02X" % code
            if ocode != code:
                alt = "0x%02X" % ocode
        else:
            alt = "0x%02X" % ocode
        pdf.cell(20, 8, txt = hcode, border = 1, align = "L")
        pdf.cell(20, 8, txt = alt, border = 1, align = "L")
        pdf.ln()


    used = []
    for char, name, code in SYMBOLS:
        print_char(char, name, code)
        used.append(code)

    for i in range(32, 256):
        if i not in used:
            print_char(unichr(i), "Code 0x%02X" % i, i)

    pdf.output(outputname, 'F')

if __name__ == "__main__":
    common.testmain(__file__, dotest)
