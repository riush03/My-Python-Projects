import sys

import PIL
from PIL import Image
from PIL import ImageDraw
from difflib import SequenceMatcher
from cryptography.fernet import Fernet
from __future__ import  with_statement
import contextlib

def add_watermark(img_path,res_path,text,pos):
    targ_img = Image.open(img_path)
    wm = ImageDraw.Draw(targ_img)
    col = (9,3,10)
    wm.text(pos,text,fill=col)
    targ_img.show()
    targ_img.save(res_path)

def check_plagiarism(cont1,cont2):
    with open(cont1,errors="ignore") as file1,open(cont2,errors="ignore") as file2:
        file1_data=file1.read()
        file2_data=file2.read()
        res = SequenceMatcher(None,file1_data,file2_data).ratio()
        print(f"The palgiarism level for these two ducments is `{res*100}` %.")

def encrypt_files(file_name,key):
    fernet = Fernet(key)
    with open(file_name,'rb') as file:
        original = file.read()
        encrypted = fernet.encrypt(original)
        with open(file_name,'wb') as enc_file:
            enc_file.write(encrypted)

def decrypt(file_name,key):
    fernet = Fernet(key)
    with open(file_name,'rb') as enc_file:
        encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(file_name,'wb') as dec_file:
            dec_file.write(decrypted)

     #use tinyurl api
def url_shortener(url):
    request_url = ('http://tinyurl.com/api-create.php?'+urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

def shorten():
    for tinyurl in map(url_shortener,sys.argv[1:]):
        print(tinyurl)

if __name__ == "__main__":
    """"
    Use if and elif statement to choose between different automation tasks
    
    key = Fernet.generate_key()
    file_name = input("Enter your filename:")
    encrypt(file_name,key)
    decrypt(file_name,key)
    """