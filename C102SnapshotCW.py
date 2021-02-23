import cv2
import random
import time
import dropbox

startTime = time.time()

def TakeSnapshot():
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        img_name = "img"+str(random.randint(0,100))+".png"
        cv2.imwrite(img_name,frame)
        startTime = time.time()
        result = False
    return img_name
    print("Take a snapshot")
    videocaptureobject.release()
    cv2.destroyAllWindows()

def UploadFile(img_name):
    accessToken = 'sl.ArzT35LqXtldTwlTL2E5ECJmxaDOATWLgIm_0ofqQLeJHYI42z709ntBiH1ZGj-jKJ1pJJYGDWF2Sokb0gcSR20cw1dR7KPqgPlsJB36zRVxyc7CRZV4wmfsczayJ704Y9M7d_A'
    filefrom = img_name
    fileto = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(accessToken)
    with open(filefrom, 'rb') as f:
        dbx.files_upload(f.read(),fileto,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded Successfully")

def main():
    while (True):
        print(startTime)
        if((time.time()-startTime)>=300):
            name = TakeSnapshot()
            UploadFile(name)

main()