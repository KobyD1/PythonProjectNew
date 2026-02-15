import os
import shutil
import time

import cv2
import numpy as np
from PIL import Image


# to install packages matplotlib 3.7.3 ,opencv-python 4.8.78  before
# install open cv by pip install opencv-python
# version of opencv-python is 4.8.1.78
class ImagesUtils():

    def __init__(self, driver, is_learning):
        self.driver = driver
        self.is_learning = is_learning
        self.mismatch_mark = [0, 255, 255]

    def compare_images(self, path_image_under_test: str, path_ref: str, path_res: str) -> bool:
        image1 = cv2.imread(path_image_under_test)
        image2 = cv2.imread(path_ref)

        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        difference[mask != 255] = [0, 0, 255]

        image1[mask != 255] = self.mismatch_mark
        image2[mask != 255] = self.mismatch_mark

        # store images
        cv2.imwrite(path_res, image1)
        return result

    def compare_image_rectangle(self, path_file_ref: str, rectangle, name: str) -> bool:

        properties = self.__prapare(name, path_file_ref)
        Image.open(properties.get('path_res'))
        box = (rectangle['x'], rectangle['y'], rectangle['x+width'], rectangle['y+highet'])
        self.__get_screen_capture(properties.get('path_screenshot'))
        shutil.copyfile(properties.get('path_screenshot'), properties.get('path_res'))
        self.__crop_image(box, properties.get('path_crop'), properties.get('path_screenshot'))

        is_equals = self.compare_images(properties.get('path_crop'), path_file_ref, properties.get('path_res'))
        return is_equals

    def compare_image_list(self, images: list, name: str) -> bool:
        is_pass = False
        ms = str(round(time.time() * 1000.0))
        ms = ms[6:]
        path_dir = f"..//Images//Results//{name}{ms}"
        print(f'Create folder for list at {path_dir}')
        path_screenshot = path_dir + "//screenshot.png"
        os.makedirs(path_dir, exist_ok=True)
        self.__get_screen_capture(path_screenshot)
        index = 0
        for image in images:
            path_file_ref = image[2]
            index += 1
            print(f'Trying to compare image at image index {index}')
            coardination = self.get_image_coardination(image)
            path_crop = f'{path_dir}//crop_{index}.png'
            path_result = f'{path_dir}//result_{index}.png'

            self.__crop_image(coardination, path_crop, path_screenshot)
            is_pass = self.compare_images(path_file_ref, path_crop, path_result)
            if is_pass:
                break
        return is_pass

    def get_image_coardination(self, image: tuple) -> tuple:
        im = Image.open(image[2])
        width = im.size[0]
        highet = im.size[1]
        coardination = (
            image[0],
            image[1],
            image[0] + width,
            image[1] + highet
        )

        return coardination

    def compare_image_coardinations(self, path_file_ref: str, coardinations, name: str):
        im = Image.open(path_file_ref)
        width = im.size[0]
        highet = im.size[1]
        rectangle = {
            'x': coardinations['x'],
            'y': coardinations['y'],
            'x+width': coardinations['x'] + width,
            'y+highet': coardinations['y'] + highet
        }
        is_equals = self.compare_image_rectangle(path_file_ref, rectangle, name)
        return is_equals

    def __prapare(self, prefix: str, path_file_ref: str):
        ms = str(round(time.time() * 1000.0))
        ms = ms[6:]
        path_dir = "..//Images//Results//" + prefix + ms
        os.makedirs(path_dir, exist_ok=True)
        assert os.path.exists(path_file_ref), 'Ref. file not found at ' + path_file_ref

        properties = {
            'path_root': "..//Images//Results//" + prefix + ms,
            'path_crop': path_dir + "//cropped.png",
            'path_res': path_dir + "//result.png",
            'path_screenshot': path_dir + "//screenshot.png"
        }
        self.__get_screen_capture(properties.get('path_res'))
        shutil.copyfile(path_file_ref, path_dir + "//ref.png")

        return properties

    def close_file(self, path: str):
        try:
            file = open(path, "r+")
        finally:
            file.close()

    def __get_screen_capture(self, path: str):
        print(f'get screen capture at {path}')
        self.driver.save_screenshot(path)

    def __crop_image(self, rectangle: tuple, path_save: str, path_under_test: str):
        im = Image.open(path_under_test)
        cropped = im.crop(rectangle)
        cropped.save(path_save)
