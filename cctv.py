import picamera
from time import sleep
import keyboard
import subprocess

zoom_factor = 1

def zoom(amount):
	global zoom_factor
	zoom_factor = zoom_factor + amount
	if(zoom_factor < 1.0):
		zoom_factor = 1.0
	camera.zoom = (0.5 - 1/zoom_factor/2, 0.5 - 1/zoom_factor/2, 1.0/zoom_factor, 1.0/zoom_factor)

def get_best_resolution():
	tvservice_status = subprocess.check_output(['tvservice', '-s'])
	resolution = tvservice_status.split()[8]
	width, height = resolution.split(b'x')
	aspect_height_16 = int(height) / (int(width) / 16)
	height_for_1280 = 80 * int(aspect_height_16)
	return (1280, height_for_1280)


def contrast_mode(mode):
	if(mode == 0):
		camera.image_effect = 'none'
		camera.brightness = 65
		camera.contrast = 50
		camera.saturation = -100
		camera.sharpness = 90
		camera.exposure_mode = 'fixedfps'
		camera.exposure_compensation = 0
		camera.video_denoise = True
		camera.video_stabilization = True
		camera.drc_strength = 'off'
		camera.color_effects = None
	elif(mode == 1):
		camera.image_effect = 'negative'
		camera.brightness = 65
		camera.contrast = 90
		camera.saturation = -100
		camera.sharpness = 100
		camera.exposure_mode = 'fixedfps'
		camera.exposure_compensation = 0
		camera.video_denoise = True
		camera.video_stabilization = True
		camera.drc_strength = 'off'
		camera.color_effects = None
	elif(mode == 2):
		camera.image_effect = 'negative'
		camera.brightness = 65
		camera.contrast = 100
		camera.saturation = -100
		camera.sharpness = 90
		camera.exposure_mode = 'fixedfps'
		camera.exposure_compensation = 0
		camera.video_denoise = True
		camera.video_stabilization = True
		camera.drc_strength = 'off'
		camera.color_effects = None
	elif(mode == 3):
		camera.image_effect = 'none'
		camera.brightness = 50
		camera.contrast = 50
		camera.saturation = 0
		camera.sharpness = 50
		camera.exposure_mode = 'fixedfps'
		camera.exposure_compensation = 0
		camera.video_denoise = True
		camera.video_stabilization = True
		camera.drc_strength = 'off'
		camera.color_effects = None
	elif(mode == 4):
		camera.image_effect = 'negative'
		camera.brightness = 65
		camera.contrast = 90
		camera.saturation = -100
		camera.sharpness = 100
		camera.exposure_mode = 'fixedfps'
		camera.exposure_compensation = 0
		camera.video_denoise = True
		camera.video_stabilization = True
		camera.drc_strength = 'off'
		camera.color_effects = (180, 128)
	elif(mode == 5):
		camera.image_effect = 'negative'
		camera.brightness = 65
		camera.contrast = 90
		camera.saturation = -100
		camera.sharpness = 100
		camera.exposure_mode = 'fixedfps'
		camera.exposure_compensation = 0
		camera.video_denoise = True
		camera.video_stabilization = True
		camera.drc_strength = 'off'
		camera.color_effects = (200, 128)
	elif(mode == 6):
		camera.image_effect = 'none'
		camera.brightness = 65
		camera.contrast = 50
		camera.saturation = -100
		camera.sharpness = 90
		camera.exposure_mode = 'fixedfps'
		camera.exposure_compensation = 0
		camera.video_denoise = True
		camera.video_stabilization = True
		camera.drc_strength = 'off'
		camera.color_effects = None
	elif(mode == 7):
		camera.image_effect = 'none'
		camera.brightness = 65
		camera.contrast = 50
		camera.saturation = -100
		camera.sharpness = 90
		camera.exposure_mode = 'fixedfps'
		camera.exposure_compensation = 0
		camera.video_denoise = True
		camera.video_stabilization = True
		camera.drc_strength = 'off'
		camera.color_effects = None
	elif(mode == 8):
		camera.image_effect = 'none'
		camera.brightness = 65
		camera.contrast = 50
		camera.saturation = -100
		camera.sharpness = 90
		camera.exposure_mode = 'fixedfps'
		camera.exposure_compensation = 0
		camera.video_denoise = True
		camera.video_stabilization = True
		camera.drc_strength = 'off'
		camera.color_effects = None


camera = picamera.PiCamera()
camera.resolution = get_best_resolution()
camera.framerate = 60
camera.brightness = 65
camera.contrast = 50
camera.saturation = -100
camera.sharpness = 90
camera.exposure_mode = 'fixedfps'
#camera.video_denoise = True
#camera.video_stabilization = True
#camera.drc_strength = 'off'
#camera.exposure_compensation = 0
camera.color_effects = (128, 128)
#camera.image_effect = 'negative'
camera.start_preview()
keyboard.add_hotkey('+', zoom, args=[0.1])
keyboard.add_hotkey('-', zoom, args=[-0.1])
keyboard.add_hotkey('1', contrast_mode, args=[0])
keyboard.add_hotkey('2', contrast_mode, args=[1])
keyboard.add_hotkey('3', contrast_mode, args=[2])
keyboard.add_hotkey('4', contrast_mode, args=[3])
keyboard.add_hotkey('5', contrast_mode, args=[4])
keyboard.add_hotkey('6', contrast_mode, args=[5])
keyboard.add_hotkey('7', contrast_mode, args=[6])
keyboard.add_hotkey('8', contrast_mode, args=[7])
keyboard.add_hotkey('9', contrast_mode, args=[8])

while True:
		sleep(1)