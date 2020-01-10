import cv2
import numpy as np
import os
net=cv2.dnn.readNet(os.path.join(__file__,"../yolov3-tiny-label_84.weights"),os.path.join(__file__,"../yolov3-tiny-label.cfg"))
classes=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
layer_names=net.getLayerNames()
output_layers=[layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]

def detect(img,conf=0.25,get_positions=False,x_line=0.2,y_line=0.1,return_image=False):
    if isinstance(img,str):
        img=cv2.imread(img)
    img2=img.copy()
    height,width,_=img.shape
    detected_lines=[]
    written_text=""
    blob=cv2.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0),True,crop=False)
    net.setInput(blob)
    outs=net.forward(output_layers)
    class_ids=[]
    confidences=[]
    boxes=[]
    for out in outs:
        for detection in out:
            scores=detection[5:]
            class_id=np.argmax(scores)
            confidence=scores[class_id]
            if confidence>conf:
                 center_x=int(detection[0]*width)
                 center_y=int(detection[1]*height)
                 w=int(detection[2]*width)
                 h=int(detection[3]*height)
                 x=int(center_x - w/ 2)
                 y=int(center_y - h /2)
                 boxes.append([x,y,w,h])
                 confidences.append(float(confidence))
                 class_ids.append(class_id)
    font=cv2.FONT_HERSHEY_PLAIN
    previous_x=-1
    previous_y=-1
    for i in range(len(boxes)):
        x, y,w,h=boxes[i]
        label = str(classes[class_ids[i]])
        cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img2,label,(x,y+30),font,1,(0,0,255),2)
        if previous_x==-1 and previous_y==-1:
            written_text+=str(label)
        else:
            if (y-previous_y)/height < y_line and (x-previous_x)/width<x_line:
                written_text+=str(label)
            else:
                detected_lines.append(written_text)
                written_text=""
                written_text+=str(label)
        previous_y=y
        previous_x=x
    if not written_text=="":
        detected_lines.append(written_text)
    if return_image:
        if get_positions:
            return {"image":img2,"lines":detected_lines,"pos":{"positions":boxes,"labels":[str(classes[w]) for w in class_ids],"confidences":confidences},}
        else:
            return {"image":img2,"lines":detected_lines,}
    else:
        if get_positions:
            return {"lines":detected_lines,"pos":{"positions":boxes,"labels":[str(classes[w]) for w in class_ids],"confidences":confidences},}
        else:
            return {"lines":detected_lines,}