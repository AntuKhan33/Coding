from email.mime import base, image
import os
from re import I
from secrets import choice
print(os.getcwd())
print(os.listdir())

names=sorted([name for name in os.listdir() if name.startswith('2')])
print(names)
fnames=sorted(name for name in os.listdir() if name.endswith(".py"))
print(fnames)
print(os.getcwd())

# os.mkdir("documents")
# dirnames = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]
# for dirname in dirnames:
#     path = os.path.join('documents', dirname)
#     os.mkdir(path)

# print(sorted(os.listdir('documents')))
    
# base_dir="images"
# png_dir=os.path.join(base_dir,'images_png')
# jpg_dir=os.path.join(base_dir,'images_jpg')
# if not os.path.exists(base_dir):
#     os.mkdir(base_dir)
    
# if not os.path.exists(png_dir):
#     os.mkdir(png_dir)
# if not os.path.exists(jpg_dir):
#     os.mkdir(jpg_dir)
# for root,dirs,files in os.walk(base_dir):
#     print(root)

# import random
# random.seed(30)
# images = [f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}" for i in range(1, 20)]
# base_dir='images'
# if not os.path.exists(base_dir):
#     os.mkdir(base_dir)
# png_dir=os.path.join(base_dir,'images_png')
# jpg_dir=os.path.join(base_dir,"images_jpg")

# if not os.path.exists(png_dir):
#     os.mkdir(png_dir)
# if not os.path.exists(png_dir):
#     os.mkdir(png_dir)

# for image in images:
#     if image.endswith('.png'):
#         open(os.path.join(png_dir,image),'w').close
#     elif image.endswith('.jpg'):
#         open(os.path.join(jpg_dir,image),'w').close()
        
# for root,dirs,files in os.walk(base_dir):
#     print(root)
#     for file in sorted(files):
#         print(f'\t{file}')


# import os
# import random


# random.seed(30)
# images = [f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}" for i in range(1, 20)]

# base_dir = 'images'
# png_dir = os.path.join(base_dir, 'images_png')
# jpg_dir = os.path.join(base_dir, 'images_jpg')

# if not os.path.exists(base_dir):
#     os.mkdir(base_dir)

# if not os.path.exists(png_dir):
#     os.mkdir(png_dir)

# if not os.path.exists(jpg_dir):
#     os.mkdir(jpg_dir)

# for image in images:
#     if image.endswith('.png'):
#         open(os.path.join(png_dir, image), 'w').close()
#     elif image.endswith('.jpg'):
#         open(os.path.join(jpg_dir, image), 'w').close()

# for root, dirs, files in os.walk(base_dir):
#     for file in sorted(files):
#         print(file)

# fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]
# paths = [os.path.join(os.getcwd(), fname) for fname in fnames]
# print(paths)

# fnames = [f"{str(i).zfill(2)}_sales.csv" for i in range(1, 25)]
# paths = [os.path.join(os.getcwd(), '2020', fname) if idx < 12 
#          else os.path.join(os.getcwd(), '2021', fname) 
#          for idx, fname in enumerate(fnames)]
         
# for path in paths:
#     print(path)

# paths=[os.path.join(os.getcwd(),f'dir_{str(i).zfill(2)}')for i in range(1,14)]
# for path in paths:
#     if not os.path.exists(path):
#         os.mkdir(path)