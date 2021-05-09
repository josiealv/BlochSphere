import cv2
import numpy as np
   
#functiom code from geeks4geeks: https://www.geeksforgeeks.org/python-play-a-video-using-opencv/
def main(filename):
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(filename)
    
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video file")
    
    # Read until video is completed
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow(filename, frame)
            # Press Q on keyboard to  exit
            if cv2.waitKey(75) & 0xFF == ord('q'):
                break
        # Break the loop
        else: 
            break
    # When everything done, release 
    # the video capture object
    cap.release()
    
    # Closes all the frames
    cv2.destroyAllWindows()