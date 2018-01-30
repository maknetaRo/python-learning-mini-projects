import random 
import urllib.request

def download_web_image(url):
	name = random.randrange(1, 1000)
	full_name = str(name) +".jpg"
	urllib.request.urlretrieve(url, full_name)

download_web_image("https://2.bp.blogspot.com/-kOmgOHAxsq0/WZR-qt4F0xI/AAAAAAAAUxs/cBAeopMsAlknpqqKvDhHPWLZNLQKv_mFACLcBGAs/s640/CAM04173-01-01.jpeg")



