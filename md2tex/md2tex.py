import re


def tex_read(path_r):
    with open(path_r) as f:
        l = ["\n"]+[s.strip() for s in f.readlines()] #2行あけるようにしている
    return l

def tex_write(list,output,header=True):
    if header:
        with open("begin.tex") as f:
            ft = f.readlines()
    else:
        ft = ""
    with open(output, mode='w') as f:
        for i in ft:
            f.write(i)
        for i in list:
            f.write(i)
            f.write("\n")
        if header == True:
            end_text = turn_off("") + "\n" + r"\end{document}"
        else:
            end_text = turn_off("") + "\n"
        f.write(end_text)

dix = {
    "math" : 0,
    "itemize" : 0,
    "enumerate" : 0,
    "tcolorbox": 0,
    }

def turn_off(str):
    if dix["math"] == 1:
        str += ""
        dix["math"] = 0
    if dix["itemize"] == 1:
        str = r"\end{itemize}" + "\n" + str
        dix["itemize"] = 0
    if dix["enumerate"] == 1:
        str = r"\end{enumerate}" + "\n" + str
        dix["enumerate"] = 0
    return str

# strがヘッダーかどうか調べる
def set_chapter(str):
    num = 0
    i = 0
    while 1:
        if len(str) > i:
            if str[i] == "#": num += 1
            else: break
            i += 1
        else: break
    if num == 1:
        str = r"\part*{" + str[num:].strip() + "}"
    elif num == 2:
        str = r"\section*{" + str[num:].strip() + "}"
    elif num == 3:
        str = r"\subsection*{" + str[num:].strip() + "}"
    elif num >= 4:
        str = r"\subsubsection*{" + str[num:].strip() + "}"
    if num > 0:
        str = turn_off(str)
    return str

# 箇条書きがないかを調べる
def set_list(str):
    if len(str) > 1:
        if str[:2] == "* " or str[:2] == "- ":
            # 箇条書きを終わらせる場合の指定
            if dix["enumerate"] == 1:
                str =  r"\end{enumerate}" + "\n"  +str
                dix["enumerate"] = 0
            elif "end" in str and "item" in str:
                str = r"\end{itemize}"
                dix["itemize"] = 0
            elif dix["itemize"] == 0:
                str = r"\begin{itemize}" + "\n" + r"\item " + str[1:].strip()
                dix["itemize"] = 1
            else:
                str = r"\item " + str[1:].strip()
        elif re.match("\d+" + ". ",str):
            match = re.match("\d+" + ". ",str)
            n = len(match.group())
            # 箇条書きを終わらせる場合の指定
            if dix["itemize"] == 1 and dix["enumerate"] == 0:
                str =  r"\end{itemize}" + "\n" + r"\begin{enumerate}" + "\n" + str
                dix["itemize"] = 0
                dix["enumerate"] = 1
            elif "end" in str and "enum" in str:
                str = r"\end{enumerate}"
                dix["enumerate"] = 0
            elif dix["enumerate"] == 0:
                str = r"\begin{enumerate}" + "\n" + r"\item " + str[n:].strip()
                dix["enumerate"] = 1
            else:
                str = r"\item " + str[n:].strip()
    return str

# > を使った部分の対応
def tcolorbox(str):
    if len(str) > 1:
        if str[:2] == "> " and dix["tcolorbox"] == 0:
            if "#" in str[:5]:
                str = r"\begin{tcolorbox}[colback=white,colbacktitle=black,coltitle=white,title={" + str[2:] + r"}]"
            else:
                str = r"\begin{tcolorbox}[colback=white,colbacktitle=black,coltitle=white]" + "\n" + str[2:]
            dix["tcolorbox"] = 1
        elif str[:2] == "> " and dix["tcolorbox"] == 1:
            str = str[2:]
    elif str == "" and dix["tcolorbox"] == 1:
        str = r"\end{tcolorbox}" + "\n"
        dix["tcolorbox"] = 0
    return str

# 数式を見つける
def find_math(str):
    if "$$" in str:
        str_list = str.split("$$")
        for i in range(len(str_list)):
            if str_list[i] == "" and dix["math"] == 0:
                str_list[i] = r"\["
                dix["math"] = 1
            elif str_list[i] == "" and dix["math"] == 1:
                str_list[i] = r"\]"
                dix["math"] = 0
        str = "".join(str_list)
    return str

# それぞれの関数をまとめる
def combine_func(str):
    str = tcolorbox(str)
    str = set_chapter(str)
    str = set_list(str)
    str = find_math(str)
    return str

if __name__ == "__main__":
    # 読み込みファイル名
    file_in = input('input file-name\n>> ')

    change_name = input("if you want to change .tex file name form .md file, insert 'y'\n>> ")

    if '.' in file_in:
        n = file_in.find(".")
        file_out = file_in[:n] + '.tex'
    else:
        file_out = file_in + '.tex'
        file_in += '.md'

    if change_name == "y":
        file_out = input("input .tex file name to output\n>> ")
        if not '.tex' in file_out:
            file_out +=  '.tex'

    #読み込み開始
    l = tex_read(file_in)
    for i in range(len(l)):
        l[i] = combine_func(l[i])
    # 書き出しファイル名
    header = input("if you needn't header and footer, insert 'y'\n>> ")
    if header == "y":
        tex_write(l,file_out,False)
    else:
        tex_write(l,file_out)



"""
<<課題>>
1. 箇条書きの階層化の問題
-
    -
    -
2. 表
\bigin{center}と[h]を忘れずに

3. 問題をsectionではなく1.2.の箇条書きの方が良い？？
##をsectionにする場合とenumerateにする場合で分けるコマンドを作っておくと良さそう
これを課題1.と合わせて解決すべし

"""
