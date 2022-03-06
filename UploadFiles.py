import cv2
import dropbox
import time
import random

startTime = time.time()
def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        print(ret)
        imageName = "img" + str(number) + ".png"
        cv2.imwrite(imageName, frame)
        startTime = time.time()
        result = False
    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token = "SdXy6jH043cAAAAAAAAAAZe2flFqkvgHxNB4laUfBuMzfPTCfL7-iIPoq9c-F03j"
    file_from = imageName
    file_to = "/Automation/" + imageName
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to)


def main():
    while(True):
        if(time.time() - startTime >= 5):
            print("Take Picture")
            name = take_snapshot()
            print("Upload File to Dropbox")
            upload_file(name)
main()
