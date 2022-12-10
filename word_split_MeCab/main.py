import sys
package_path = "/content/gdrive/Mydrive/Colab Notebooks/pip_package/my-site-package"
sys.path.append(package_path)
#  result.surface : 語彙
# result.feature[0] : 品詞
import MeCab
import unidic

output = []
tagger = MeCab.Tagger()
txt = input()
node = tagger.parseToNode(txt)

temp = ""
prev = ""

exit()
while node:
  feature = node.feature.split(",")
  word = node.surface
  speech = feature[0]
  if (not (speech == "助詞" or speech == "補助記号" or speech == "助動詞")) and (prev == "助詞" or prev == "補助記号" or prev == "助動詞"):

    print(temp,prev,speech)
    output.append(temp)
    temp = ""
  temp += word
  prev = speech
  node = node.next
output.append(temp)

print(output)
