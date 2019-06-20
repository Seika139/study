import re

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

if __name__ == "__main__":
    path = "./report.md"
    master = Textmaster()
    text = master.read_text_as_str(path)
    print(master.count_length(text))

    """
    text_box  = master.read_text_file(path)
    text = master.cut_blanks(text_box)
    master.write_text(text,file_out="report_output.txt")
    """
