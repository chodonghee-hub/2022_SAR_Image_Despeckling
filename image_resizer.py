from PIL import Image
import os

r'''
* Change each png data to grey scale ( 8 bit ) data
* Resize : 256 x 256
* Make "resize_result" directory if not exists, and save all results at there 
'''

def __create_result_folder__() :
    try :
        dir_list = os.listdir('./')
        if 'resize_result' not in dir_list :
            os.mkdir('resize_result')
    except :
        pass

def __get_SAR_image__() :
    if 'sar_image' not in os.listdir('./') :
        raise Exception('** not exists : "sar_image" directory ')        
    else :
        f = os.listdir('./sar_image')
        
        if not f :
            raise Exception('** empty : "sar_image" directory is empty')
        
        else :
            rs = dict()            
            for fileName in f :
                rs[fileName] = Image.open(f'./sar_image/{fileName}')
                
            return rs
                        
def __resize_image__(fileName, img) :
    img_resize = img.resize((256, 256))
    imgGray = img_resize.convert('L')
    imgGray.save(f'./resize_result/r8_{fileName}')

def __init__() :
    __create_result_folder__()
    SAR_datas = __get_SAR_image__()
    
    for fileName, img in SAR_datas.items() :
        __resize_image__(fileName, img)

__init__()
