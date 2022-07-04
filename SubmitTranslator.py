from deep_translator import GoogleTranslator
from tqdm import tqdm
from os import listdir

banner = """
  ____                 _        _      
 / ___|_ __ ___   __ _| |_ _ __(_)_  __
| |   | '_ ` _ \ / _` | __| '__| \ \/ /
| |___| | | | | | (_| | |_| |  | |>  < 
 \____|_| |_| |_|\__,_|\__|_|  |_/_/\_\
                                       
 _____                    _       _              
|_   _| __ __ _ _ __  ___| | __ _| |_ ___  _ __  
  | || '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__| 
  | || | | (_| | | | \__ \ | (_| | || (_) | |    
  |_||_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|    
                                                 

"""



class Translator:
    def __init__(self, file_name, new_file):
        self.tr = GoogleTranslator(source='auto', target='fa')
        self.file = open(file_name, "r")
        self.sentences = self.file.readlines()
        self.flen = len(self.sentences)
        self.nums = [4*i-2 for i in range(1, self.flen)]
        self.nfile = open(new_file, "w", encoding="utf-8")

    def translate(self, sen):
        return self.tr.translate(sen)

    def write_on_file(self, sen):
        self.nfile.write(sen)
    
    def main(self):
        for i in tqdm(self.sentences):
            index = self.sentences.index(i)
            if index in self.nums:
                self.write_on_file(self.translate(i))
            else:
                self.write_on_file(i)

def RunScript():
    dirs = list(filter(lambda x: ".srt" in x, listdir()))
    if dirs == []:
        print("\u001b[31m [x] Not Found '.srt' File in this directory")
        return False

    print("\033[0;32m"+banner)
    print("\033[0;33m")
    print("\nFILES :\n ")
    print("\r"+" \n ".join(dirs))
    my_file = input("\nEnter Your File Name:")
    new_file = input("\nEnter Your New File Name [without '.srt'] :") + ".srt"
    print("\n"+'\033[0;34m')

    s = Translator(my_file, new_file)
    s.main()

if __name__ == "__main__":
    RunScript()