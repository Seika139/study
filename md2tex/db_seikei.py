import re
import pyperclip

class Textmaster():

    def read_text_as_list(self,path):
        with open(path) as f:
            l = ["\n"]+[s.strip() for s in f.readlines()] #2行あけるようにしている
        return l

    def read_text_as_str(self,path):
        with open(path) as f:
            l = f.read()
        return l

    def cut_blanks(self,list):
        text_out = ""
        ignore_list = ("\n",)
        for text in list:
            if text and text not in ignore_list:
                text = self.replace_comma(text)
                text_out += text
        return text_out

    def replace_comma(self,text):
        if "，" in text:
            text = text.replace("，","、")
        return text

    def write_text(self,text,file_out):
        with open(file_out, mode='w') as f:
            if type(text) == list:
                for i in text:
                    f.write(i)
                    f.write("\n")
            elif type(text) == str:
                f.write(text)

    def count_length(self,text):
        num = len(text)
        text_out =  "文字数 : " + str(num)
        return text_out

    def seikei(self,list):
        ans = []
        for elm in list:
            if "JMT" in elm[:5]:
                ans.append(elm[2:18])
            else:
                continue
        return ans

    def bun_sakusei(self,list):
        ans = ['INSERT INTO kokonetwebapp_tagtree (chu_tag_id, dai_tag_id, sho_tag_id, sub_id) VALUES']
        for elm in list:
            text = '(\"' + elm[:-3] + '\",\"' + elm[:-6] + '\",\"' + elm + '\",' + '30),'
            ans.append(text)
        ans[-1] = ans[-1][:-1] + ";"
        return ans

if __name__ == "__main__":
    path = "test.csv"
    master = Textmaster()
    text = master.read_text_as_list(path)
    text = master.seikei(text)
    text = master.bun_sakusei(text)
    ans = ""
    for i in text:
        ans += i
    pyperclip.copy(ans)

    """
    text_box  = master.read_text_file(path)
    text = master.cut_blanks(text_box)
    master.write_text(text,file_out="report_output.txt")
    """
