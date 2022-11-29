from janome.tokenizer import Tokenizer
import re
import pyperclip


### pattern
pat_1 = r"名詞|動詞|副詞|感動詞|形容詞|形容動詞|連体詞|接頭詞"
pat_2 = r"[^(記号)]"
regex1 = re.compile(pat_1)
regex2 = re.compile(pat_2)
### clipboard
string = pyperclip.paste()

### tokenizer
t = Tokenizer()
str_list = t.tokenize(string)

## main
result = []
string = ""
for n in str_list:
    if regex2.match(n.part_of_speech):
        if regex1.match(n.part_of_speech):
            result.append(string)
            string = ""
        string += n.surface


        # if regex1.match(n.part_of_speech):
        #     string += n.surface
        #     result.append(string)
        #     string = ""
        # else:
        #     string += n.surface
print(result)

### sample
for n in str_list:
    print(n)
