import cv2
def main():
    cap=cv2.VideoCapture("Videos/dog.mp4")
    
    output=cv2.VideoWriter("ouput.mp4",cv2.VideoWriter_fourcc(*'MPEG'),30,(1080,1920))
    
    while True:
        ret,frame=cap.read()
        if(ret):
            cv2.rectangle(frame,(100,100),(200,200),[255,255,255],2)
            output.write(frame)
            cv2.imshow("output",frame)
            
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
    cv2.destroyAllWindows()
    output.release()
    cap.release()
    
if __name__ =="__main__":
    main()  
                