# Virtual Mouse with Hand Gestures

This project is a **Virtual Mouse** that allows you to control your computer’s cursor and perform click/scroll actions using **hand gestures** detected through a webcam. It uses **MediaPipe** for hand tracking and **PyAutoGUI** for controlling the mouse.

## ✨ Features

* **Move Cursor:** Move your index finger to control the mouse pointer.
* **Left Click:** Touch your thumb and index finger together.
* **Right Click:** Touch your thumb and ring finger together.
* **Scroll:** Extend both index and middle fingers and move them up/down to scroll.
* **Smooth Cursor Movement:** Reduces jitter for better control.

## 🛠️ Technologies Used

* OpenCV – for video capture and image processing.
* MediaPipe – for real-time hand landmark detection.
* PyAutoGUI – for controlling the mouse and performing clicks.

## 🎯 Usage Instructions

* **Move Mouse:** Point with your index finger.
* **Left Click:** Touch thumb and index finger.
* **Right Click:** Touch thumb and ring finger.
* **Scroll:** Keep both index and middle fingers extended, move hand up/down.
* **Exit:** Press **`q`** to quit.

## 📷 How It Works

1. The webcam captures live video.
2. MediaPipe Hands detects the position of your fingers.
3. Gestures are interpreted to trigger corresponding mouse actions via PyAutoGUI.

## ⚠️ Notes

* Works best in good lighting conditions.
* Keep your hand within the camera’s view for accurate tracking.
* Scroll sensitivity can be adjusted in the code:


## 📄 License

This project is open-source and available under the [MIT License](LICENSE).


