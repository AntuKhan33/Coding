import tkinter as tk
import cv2
from PIL import ImageTk, Image

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
        # Open the video source
        self.video = cv2.VideoCapture(0)
        
        # Create a canvas that will show the video frames
        self.canvas = tk.Canvas(window, width=self.video.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        # Create a button to take a photo
        self.btn_snapshot = tk.Button(window, text="Take Photo", command=self.snapshot)
        self.btn_snapshot.pack(anchor.CENTER, expand=True)
        
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
        
        self.window.mainloop()
    
    def snapshot(self):
        # Get the current frame from the video source
        ret, frame = self.video.read()
        
        if ret            # Save the frame as an image file
            cv2.imwrite("snapshot.png", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            print("Snapshot taken!")
    
    def update(self):
        # Get the latest frame from the video source
        ret, frame = self.video.read()
        
        if ret:
            # Convert the frame to RGB color space
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            
            # Convert the frame to ImageTk format
            image = Image.fromarray(frame_rgb)
            image_tk = ImageTk.PhotoImage(image)
            
            # Update the canvas with the new frame
            self.canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        
        # Call the update method again after the specified delay
        self.window.after(self.delay, self.update)

# Create a window and pass it to the Application object
App(tk.Tk(), "Real-Time Video Capture")
