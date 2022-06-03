import torch
import cv2

def detecting (frame, model):
    frame = [frame]
    print(f"Detecting . . .")
    res = model(frame)
    labels, cords = res.xyxyn[0][:, -1], res.xyxyn[0][:, :-1]
    return labels, cords

def color_box(results, frame, classes, acc=0.45):
    labels, cords = results
    n = len(labels)
    x_window, y_window = frame.shape[1], frame.shape[0]
    print(f"Number of detections: {n}")

    for i in range(n): #processing of detected objects
        cords_list = cords[i]
        if cords_list[4] >= acc: #Accuracy Comparison
            print(f"Creating color box . . .")
            x1 = int(cords_list[0]*x_window)
            y1 = int(cords_list[1]*y_window)
            x2 = int(cords_list[2]*x_window)
            y2 = int(cords_list[3]*y_window)
            text_d = classes[int(labels[i])]
            color = (0, 0, 0)
            if text_d == "pistol":
                color = (255, 0, 0)
            elif text_d == "machine_gun":
                color = (255, 170, 0)
            elif text_d == "knife":
                color = (0, 170, 127)
            else:
                color = (85, 0, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2) #object box
            cv2.rectangle(frame, (x1, y1-20), (x2, y1), color, -1) #text box
            cv2.putText(frame, text_d + f" {round(float(cords_list[4]),2)}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2) #text adding

    return frame

def recognize(img_path=None, img_out=None, vid_path=None, vid_out=None, acc=0.45):
    print(f"Downloading model . . .")
    #Custom model = 'best.pt'
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)
    classes = model.names 

    if img_path != None:
        print(f"Your image: {img_path}")
        frame = cv2.imread(img_path)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = detecting(frame, model = model)   
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = color_box(res, frame, classes = classes, acc=acc)

        print(f"Done!")
        cv2.imwrite(f"{img_out}", frame) #save output image


    elif vid_path !=None:
        print(f"Your video: {vid_path}")
        cap = cv2.VideoCapture(vid_path)

        if vid_out: #Output video params
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            codec = cv2.VideoWriter_fourcc(*'mp4v')
            fps = int(cap.get(cv2.CAP_PROP_FPS))    
            out = cv2.VideoWriter(vid_out, codec, fps, (width, height))
        frame_number = 1

        while True:
            ret, frame = cap.read()
            if ret:
                print(f"Work with frame: {frame_number} ")
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                res = detecting(frame, model = model)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                frame = color_box(res, frame, classes = classes, acc=acc)
                out.write(frame)
                frame_number += 1
            else: 
                print(f"Save output video . . .")
                cap.release() #Releasing video resources
                out.release()
                break
            
