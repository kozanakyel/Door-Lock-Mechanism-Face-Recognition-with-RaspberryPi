import cv2
import argparse
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', help='Please give a name for dataset')
args = parser.parse_args()

name = args.name

#if file or person exist how to find for last images gor continuation the append images
def find_last_img_number(filelist):
    lt = []
    for i in filelist:
        ptrn = re.findall('[0-9]+', i)
        lt.append(int(ptrn[0]))

    mx = max(lt)
    return mx

#preparing for the folder structure before the video capture
current = os.getcwd()
path = 'dataset/' + name
path = os.path.join(current, path)


img_counter = 0
if os.path.exists(path):
    dir_list = os.listdir(path)
    print(dir_list, type(dir_list), type(dir_list[0]))
    print('print last images ', find_last_img_number(dir_list))
    img_counter = find_last_img_number(dir_list) + 1   #because list index start 0
else:
    os.makedirs(path)
    print(path, 'created...')


cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)


while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
