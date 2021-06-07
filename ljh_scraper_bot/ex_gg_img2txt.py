def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print('Texts:')
    
    f=open('res.txt','w',encoding='utf8')
    for text in texts:
        # print('\n"{}"'.format(text.description))
        f.write(text.description)

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        # print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


import selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path = 'C:\Python\chromedriver.exe')
url = "https://www.google.com/"
driver.get(url)
driver.save_screenshot('ss.png')

# fpath=r'C:\Python\python'
fname='ss.png'
# path=fpath+fname
detect_text(fname)

# with open('res.txt','r',encoding='utf8') as f1:
#     temp=f1.read()
# with open('output.txt','w',encoding='utf8') as f2:
#     f2.write(temp[:temp.find('학교장')+3])
