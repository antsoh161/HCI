# Choregraphe beziner export in Python.
from naoqi import ALProxy
import cv2
import argparse
import pyopenpose as op
import openpose

# Put Nao's right hand up
def rh_up():
	names = list()
	times = list()
	keys = list()
	names.append("LElbowRoll")
	times.append([0.56])
	keys.append([[-0.420077, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([0.56])
	keys.append([[-1.20334, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([0.56])
	keys.append([[0.291787, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([0.56])
	keys.append([[1.42838, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([0.56])
	keys.append([[0.234372, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([0.56])
	keys.append([[0.105453, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([0.56])
	keys.append([[0.404657, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([0.56])
	keys.append([[1.18272, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([0.56])
	keys.append([[0.998613, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([0.56])
	keys.append([[0.176676, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([0.56])
	keys.append([[0.0456092, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([0.56])
	keys.append([[-1.20166, [3, -0.2, 0], [3, 0, 0]]])

	motion = ALProxy("ALMotion", "localhost", 46309)
	motion.angleInterpolationBezier(names, times, keys)

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("--image_path", default="~/Documents/hci-project/openpose/build/examples/media/COCO_val2014_000000000192.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
	args = parser.parse_known_args()

	# Custom Params (refer to include/openpose/flags.hpp for more parameters)
	params = dict()
	params["model_folder"] = "/home/anton/Documents/hci-project/openpose/build/models"
	params["net_resolution"] = "320x176"
	params["hand"] = True
	#params["hand_detector"] = 2
	params["body"] = 1
	#params["display"] = 1
	#params["face"] = 1

	#Add others in path?
	for i in range(0, len(args[1])):
	    curr_item = args[1][i]
	    if i != len(args[1])-1: next_item = args[1][i+1]
	    else: next_item = "1"
	    if "--" in curr_item and "--" in next_item:
	        key = curr_item.replace('-','')
	        if key not in params:  params[key] = "1"
	    elif "--" in curr_item and "--" not in next_item:
	        key = curr_item.replace('-','')
	        if key not in params: params[key] = next_item

	#Constructing OpenPose object allocates GPU memory
	openpose = OpenPose(params)

        #Opening OpenCV stream
        stream = cv2.VideoCapture(1)

        font = cv2.FONT_HERSHEY_SIMPLEX

        while True:

        	ret,img = stream.read()

        # Output keypoints and the image with the human skeleton blended on it
        	keypoints, output_image = openpose.forward(img, True)

        # Print the human pose keypoints, i.e., a [#people x #keypoints x 3]-dimensional numpy object with the keypoints of all the people on that image
        	if len(keypoints)>0:
                	print('Human(s) Pose Estimated!')
                	print(keypoints)
        	else:
                	print('No humans detected!')


        # Display the stream
        	cv2.putText(output_image,'OpenPose using Python-OpenCV',(20,30), font, 1,(255,255,255),1,cv2.LINE_AA)

        	cv2.imshow('Human Pose Estimation',output_image)

        	key = cv2.waitKey(1)

        	if key==ord('q'):
                	break

        stream.release()
	cv2.destroyAllWindows()

main()
