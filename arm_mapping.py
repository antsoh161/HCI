# Choregraphe beziner export in Python.
import sys
import math
from naoqi import ALProxy
import qi
import motion
import cv2
import argparse
import pyopenpose as op

port = 33583

def userArmArticular(motion_service, theta, phi, leftRight):
	# print("This is the length: ")
	# print(len(leftRight))
	print("\n")
	pFractionMaxSpeed = 0.9
	JointNamesL = ["LShoulderRoll", "LShoulderPitch", "LElbowRoll", "LElbowYaw"]
	JointNamesR = ["RShoulderRoll", "RShoulderPitch", "RElbowRoll", "RElbowYaw"]
	if not len(leftRight): return
	ArmL = [math.pi/12, theta[0], phi[0], 0]
	ArmR = [-math.pi/12, theta[0], phi[0], 0]
	JointNames, Arm = [], []
	if len(leftRight) == 2:
		JointNames = JointNamesL + JointNamesR
		ArmR = [-math.pi/12, theta[1], phi[1], 0]
		Arm = ArmL + ArmR
	elif leftRight[0] == "R":
		JointNames = JointNamesR
		Arm = ArmR
	elif leftRight[0] == "L":
		JointNames = JointNamesL
		Arm = ArmL
	motion_service.angleInterpolationWithSpeed(JointNames, Arm, pFractionMaxSpeed)


def main(session):
	# Nao
	motion_service = session.service("ALMotion")
	posture_service = session.service("ALRobotPosture")
	motion_service.wakeUp()
	# posture_service.goToPosture("StandInit", 0.5)

	params = dict()
	params["model_folder"] = "/home/humam/openpose/models"
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
		print (len(str(datum.poseKeypoints)))
		print ("\n")
		if len(str(datum.poseKeypoints)) > 1000:
			if (datum.poseKeypoints[0][5][2] > 0.7 and datum.poseKeypoints[0][6][2] > 0.7
				and datum.poseKeypoints[0][7][2] > 0.7):
				theta.append(math.atan2(datum.poseKeypoints[0][6][1] - datum.poseKeypoints[0][5][1],
								   datum.poseKeypoints[0][6][0] - datum.poseKeypoints[0][5][0]))
				phi.append(-abs(math.atan2(datum.poseKeypoints[0][7][1] - datum.poseKeypoints[0][6][1],
								   datum.poseKeypoints[0][7][0] - datum.poseKeypoints[0][6][0])-theta[-1]))
				leftRight.append("L")
				print("Left - Theta: " + str(math.degrees(theta[-1])) + ", Phi: " + str(math.degrees(phi[-1])) + "\n")

			if datum.poseKeypoints[0][2][2] > 0.7 and datum.poseKeypoints[0][3][2] > 0.7\
					and datum.poseKeypoints[0][4][2] > 0.7:
				theta.append(-math.atan2(datum.poseKeypoints[0][2][1] - datum.poseKeypoints[0][3][1],
								   datum.poseKeypoints[0][2][0] - datum.poseKeypoints[0][3][0]))
				phi.append(-math.atan2(datum.poseKeypoints[0][3][1] - datum.poseKeypoints[0][4][1],
								   datum.poseKeypoints[0][3][0] - datum.poseKeypoints[0][4][0]) + theta[-1])
				leftRight.append("R")
				print("Right - Theta: " + str(math.degrees(theta[-1])) + ", Phi: " + str(math.degrees(phi[-1])) + "\n")

			userArmArticular(motion_service,theta, phi, leftRight)
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