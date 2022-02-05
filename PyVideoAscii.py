from os import system, name
from sys import stdout, argv
from cv2 import VideoCapture, waitKey, CAP_PROP_POS_FRAMES
from PIL import Image
from win32gui import GetForegroundWindow, ShowWindow
from win32con import SW_MAXIMIZE

if len(argv) > 2: sharpness = int((int(argv[2]) * (45 - 35) / 100) + 35)
else: sharpness = 35

ASCII = ["?", "*", "S", "@", "#", "+", "%", ";", ":", ",", "."]
clear = lambda: system('cls' if name == 'nt' else 'clear')

def pixel_to_ascii(Frame):
	pixels = Frame.getdata()
	return "".join([ASCII[pxl//sharpness] for pxl in pixels])

def ascii_frame(Frame):
	data = pixel_to_ascii(resized_frame(Frame))
	total_pxl = len(data)
	ascii_frame = "\n".join([data[i:(i+120)] for i in range(0, total_pxl, 120)])
	stdout.write(ascii_frame)

def resized_frame(Frame):
	w, h = Frame.size
	height = int((h/w/2) * 120)
	return Frame.resize((120, height)).convert('L')

def main(source):
	rec = VideoCapture(source)
	while True:
		clear()
		_, frame = rec.read()
		ascii_frame(Image.fromarray(frame))
		waitKey(1)

if __name__ == '__main__':
	ShowWindow(GetForegroundWindow(), SW_MAXIMIZE)
	if len(argv) > 1: main(argv[1])
	else: print("usage : python3 PyVideoAscii.py [Video_source] [Sharpness(%)]")

