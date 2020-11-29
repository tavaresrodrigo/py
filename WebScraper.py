from bs4 import BeautifulSoup
import  urllib.request , re
url = 'http://pudim.com.br/'
html_page = urllib.request.urlopen(url)
soup = BeautifulSoup(html_page)
images = []
for image in soup.findAll('img'):
    source = image.get('src')
    imagePath = url+str(source)
    imageNameRegex = re.compile(r'[^\/]+$')
    imageName = imageNameRegex.search(imagePath)
    images.append(source)
    try:
        urllib.request.urlretrieve(imagePath,imageName.group())
        print (imagePath + " Downloaded")
    except:
        print('Sorry an error has occurred downloading the image' + imagePath)
print(images)
urllib.request.urlcleanup()