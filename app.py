#!/usr/bin/python3
# https://github.com/hashirkz/ascii_stuff

from ascii import *

def app():
    wd = os.getcwd()
    img_path = input('path to img: ')
    h = input('height for .txt file: ')
    try:
        h = int(h)
    except ValueError:
        print(f'h: {h} invalid value for height')
        return 1
    
    inv = input('invert y/n: ').strip() != 'n'
    save = input('save y/n: ').strip() != 'n'
    chset = input('? character_set\nDEFAULT:  .:-=+*#%@\nOTHERS: ■█▓▒░: ')
    
    # default chset / character ramp
    # other character ramps
    if not chset: chset=' .:-=+*#%@'

    if not os.path.exists(img_path): 
        print(f'unable to read {img_path} from {wd}')
        return
    
    img = read_img(img_path, inv=inv)
    img = rescale(img, h=h)
    ascii = img_to_ascii(img, chset=chset)
    savepath = f'{os.path.basename(img_path).split(".")[0]}.txt'
    ascii = pretty_repr(ascii, show=False, save=save, savepath=savepath)
    print(ascii)

    print(f'saved to: {savepath}')

if __name__ == '__main__':
    app()