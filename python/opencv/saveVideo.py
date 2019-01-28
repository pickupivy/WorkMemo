
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
#FourCC code is passed as cv.VideoWriter_fourcc('M','J','P','G')or cv.VideoWriter_fourcc(*'MJPG') for MJPG.
out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#VideoWriter (const String &filename, int fourcc, double fps, Size frameSize, bool isColor=true)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()