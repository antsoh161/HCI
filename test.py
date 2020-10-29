# Choregraphe beziner export in Python.
import sys
import math
from naoqi import ALProxy
import qi
import motion
import cv2
import argparse
import pyopenpose as op

port = 45821
angle = 0
def userArmArticular(motion_service):
	# print("This is the length: ")
	# print(len(leftRight))
	print("\n")
	pFractionMaxSpeed = 0.9
	JointNamesL = ["LShoulderRoll", "LShoulderPitch", "LElbowRoll", "LElbowYaw"]
	JointNamesR = ["RShoulderRoll", "RShoulderPitch", "RElbowRoll", "RElbowYaw"]
	global angle
	angle = angle + math.pi/6
	if(angle > math.pi*2):
		angle = 0
	newName = ["LElbowRoll"]
	Arm = [-angle]
	motion_service.angleInterpolationWithSpeed(newName, Arm, pFractionMaxSpeed)


def main(session):
	# Nao
	motion_service = session.service("ALMotion")
	posture_service = session.service("ALRobotPosture")
	motion_service.wakeUp()
	# posture_service.goToPosture("StandInit", 0.5)

	params = dict()
	params["model_folder"] = "/home/anton/Documents/hci-project/openpose/models"
	# params["model_pose"] = "COCO"
	params["net_resolution"] = "160x80"
	params["body"] = 1
	params["display"] = 1

	# Starting OpenPose
	opWrapper = op.WrapperPython()
	opWrapper.configure(params)
	opWrapper.start()

	# Process Videao
	datum = op.Datum()
	cam = cv2.VideoCapture(0) # modify here for camera number
	while(cv2.waitKey(1) != 27):
		# Get camera frame
		ret, frame = cam.read()
		datum.cvInputData = frame
		opWrapper.emplaceAndPop([datum])
		frame = datum.cvOutputData
		cv2.imshow("Webcam", frame) # datum.cvOutputData)
		leftRight, theta, phi = [], [], []
		userArmArticular(motion_service)
	# Always clean up
	cam.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="localhost",
                        help="Robot IP address. On robot or Local Naoqi: use 'localhost'.")
    parser.add_argument("--port", type=int, default=port,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
