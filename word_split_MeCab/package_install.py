#Command "Import Package Local "

from google.colab import drive
drive.mount("/content/gdrive/")

package_path = "/content/gdrive/MyDrive/Colab\ Notebooks/pip_package/my-site-packages"

!pip install mecab-python3 -t $package_path
!pip install unidic -t $package_path
!python -m unidic download

import unidic
print(unidic.DICDIR)j
