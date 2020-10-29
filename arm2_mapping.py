# Choregraphe beziner export in Python.
import sys
import math
from naoqi import ALProxy
import qi
import motion
import cv2
import argparse
import pyopenpose as op
import numpy as np

port = 45821



def userArmArticular(motion_service, theta, phi, leftRight):
	# print("This is the length: ")
	# print(len(leftRight))
	print("\n")
	pFractionMaxSpeed = 0.9
	JointNamesL = ["LShoulderPitch","LShoulderRoll", "LElbowRoll","LElbowYaw"]
	JointNamesR = ["RShoulderPitch","RShoulderRoll", "RElbowRoll","RElbowYaw"]
	if not len(leftRight): return
	#ArmL = [0, theta[0], phi[0], 0]
	#ArmL = [math.pi/2, 0, phi[0], 0]	
	#ArmR = [0, theta[0], phi[0], 0]
	#ArmR = [-math.pi/2, 0, phi[0], 0]	
	JointNames, Arm = [], []
	Arm = [math.pi/12, theta[0] + math.pi/2, phi[0] + math.pi/2, 0]
	print(theta,phi)
	if len(leftRight) == 2:
		JointNames = JointNamesL + JointNamesR
		#ArmR = [-math.pi/12, theta[1], phi[1], 0]
		#ArmR = [-math.pi/2, 0, phi[1], 0]
		ArmR = [math.pi/12,theta[1]+math.pi/2, phi[1]+math.pi/2,0]
		ArmL = [math.pi/12,theta[0]+math.pi/2, phi[0]+math.pi/2,0]
		Arm = ArmL + ArmR
	elif leftRight[0] == "R":
		
		JointNames = JointNamesR
		#Arm = ArmR
		#Arm = [0, theta[0], phi[0], 0]
	elif leftRight[0] == "L":
		
		JointNames = JointNamesL
		#Arm = ArmL
			
	motion_service.angleInterpolationWithSpeed(JointNames, Arm, pFractionMaxSpeed)


def main(session):
	# Nao
	motion_service = session.service("ALMotion")
	posture_service = session.service("ALRobotPosture")
	motion_service.wakeUp()
	#posture_service.goToPosture("StandInit", 0.5)

	params = dict()
	params["model_folder"] = "/home/anton/Documents/hci-project/openpose/models"
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
		
		
		#{0: u'Nose', 1: u'Neck', 2: u'RShoulder', 3: u'RElbow', 4: u'RWrist', 5: u'LShoulder', 6: u'LElbow', 7: u'LWrist', 8: u'MidHip', 9: u'RHip', 10: u'RKnee', 11: u'RAnkle', 12: u'LHip', 13: 				u'LKnee', 14: u'LAnkle', 15: u'REye', 16: u'LEye', 17: u'REar', 18: u'LEar', 19: u'LBigToe', 20: u'LSmallToe', 21: u'LHeel', 22: u'RBigToe', 23: u'RSmallToe', 24: u'RHeel',
		# 25: 	u'Background'}

		#print (len(str(datum.poseKeypoints)))
		#print ("\n")
		if len(str(datum.poseKeypoints)) > 1000:
			# Left Shoulder
			v1 = [datum.poseKeypoints[0][5][0], datum.poseKeypoints[0][5][1]]
			# Left Elbow
			v2 = [datum.poseKeypoints[0][6][0], datum.poseKeypoints[0][6][1]]
			# Left Wrist
			v3 = [datum.poseKeypoints[0][7][0], datum.poseKeypoints[0][7][1]]
			#Right shoulder
			v4 = [datum.poseKeypoints[0][2][0], datum.poseKeypoints[0][2][1]]
			# Right Elbow
			v5 = [datum.poseKeypoints[0][3][0], datum.poseKeypoints[0][3][1]]
			# Right Wrist
			v6 = [datum.poseKeypoints[0][4][0], datum.poseKeypoints[0][4][1]]
			
			if (datum.poseKeypoints[0][5][2] > 0.5 and datum.poseKeypoints[0][6][2] > 0.5
				and datum.poseKeypoints[0][7][2] > 0.5):

				#theta.append(math.atan2(datum.poseKeypoints[0][6][1] - datum.poseKeypoints[0][5][1],
				#				   datum.poseKeypoints[0][6][0] - datum.poseKeypoints[0][5][0]))
				
				theta.append(math.atan2(abs(np.cross(v1,v2)), np.dot(v1,v2)))
				phi.append(math.atan2(abs(np.cross(v2,v3)), np.dot(v2,v3)))
				
				#phi.append(-abs(math.atan2(datum.poseKeypoints[0][7][1] - datum.poseKeypoints[0][6][1],
				#				   datum.poseKeypoints[0][7][0] - datum.poseKeypoints[0][6][0])+theta[-1]))
				#phi.append(0)				
				leftRight.append("L")
				#print("Left - Theta: " + str(math.degrees(theta[-1])) + ", Phi: " + str(math.degrees(phi[-1])) + "\n")

			if datum.poseKeypoints[0][2][2] > 0.5 and datum.poseKeypoints[0][3][2] > 0.5\
					and datum.poseKeypoints[0][4][2] > 0.5:
				#theta.append(-math.atan2(datum.poseKeypoints[0][2][1] - datum.poseKeypoints[0][3][1],
				#				   datum.poseKeypoints[0][2][0] - datum.poseKeypoints[0][3][0]))
				#phi.append(abs(-math.atan2(datum.poseKeypoints[0][3][1] - datum.poseKeypoints[0][4][1],
				#				   datum.poseKeypoints[0][3][0] - datum.poseKeypoints[0][4][0]) - theta[-1]))
				theta.append(math.atan2(abs(np.cross(v4,v5)), np.dot(v4,v5)))
				phi.append(math.atan2(abs(np.cross(v5,v6)), np.dot(v5,v6)))	
				
				leftRight.append("R")
				#print("Right - Theta: " + str(math.degrees(theta[-1])) + ", Phi: " + str(math.degrees(phi[-1])) + "\n")

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
