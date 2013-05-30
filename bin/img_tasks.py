import numpy
from PIL import Image

"""
Image tasks: slicing, dicing, merging, cropping, etc
"""

def img_crop(file_path, height, width):
    im = Image.open(file_path)
    imgwidth, imgheight = im.size
    for i in range(imgheight // height):
        for j in range(imgwidth // width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)


def img_day_night_slice(file_path, height, width):
    for k,piece in enumerate(img_crop(file_path,height,width)):
        day_night = None
        if not k:
            day_night = "day"
        else:
            day_night = "night"
        img = Image.new('RGB', (height,width), 255)
        img.paste(piece)
        filename = os.path.basename(file_path)
        path = os.path.join(os.path.dirname(file_path), day_night+'_'+filename)
        img.save(path)


def img_merge(list_of_file_paths, destination_dir):
    np_imgs = [numpy.array(Image.open(im)) for im in list_of_file_paths]
    composite_image = numpy.amax(np_imgs, axis=0)
    new_img = Image.fromarray(composite_image)
    new_file_path = os.path.join(destination_dir, os.path.basename(list_of_file_paths[0]))
    new_img.save(new_file_path)