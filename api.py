import pyrebase
import os
from imageBackGroundRemove import imageBgRemove

firebaseConfig = {
#your apikey
};

firebase=pyrebase.initialize_app(firebaseConfig)
storage=firebase.storage()

imgPath='yavru-kopek.jpg'
deger=1

while True:
    if deger==1:
        imageBgRemove(img)
    elif deger==2:
        print("adsa")
