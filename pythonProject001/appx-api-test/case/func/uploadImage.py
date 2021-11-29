import os
import requests
class UploadPhoto():  #上传图片
    def __init__(self,s):
        self.s = s
        self.url='https://backstageservices.dreawer.com/ic/uploadImage'

    def uploadphoto(self,file_path,proxies=None):
        print(file_path)
        file_name = os.path.split(file_path)[1]
        data = {"appname": "RETAIL","type": "IMAGE"}
        files = {"file": (file_name, open(file_path, 'rb'), 'image/jpeg')}
        a = self.s.post(url=self.url, files=files, data=data, proxies=proxies, verify=False)
        return  a.json()['data'][0]



if __name__ == '__main__':
    s = requests.session()
    file_path = './../../image/111.jpg'
    py = UploadPhoto(s)
    r = py.uploadphoto(file_path)
    print(r)
