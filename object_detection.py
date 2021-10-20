import cv2
import matplotlib.pyplot as plt

config_file = ' ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model,config_file)
classlabels = []
file_name = 'coco.names'
with open(file_name,'rt') as fpt:
    classlabels = fpt.read().rstrip('\n').split('\n')


#img = cv2.imread('lena.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5,127.5,127.5))
model.setInputSwapRB(True)
while True:
    success,img = cap.read()
    classIDs, confs, bbox = model.detect(img,confThreshold=0.5)
    print(classIDs,bbox)

    if len(classIDs)!=0:
        for classID,confidence,box in zip(classIDs.flatten(),confs.flatten(),bbox):
            if (classID<=80):
                cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                cv2.putText(img,classlabels[classID-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                cv2.putText(img,str(round(confidence*100,2)),(box[0]+150,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


    cv2.imshow('output',img)
    cv2.waitKey(1)
