# Choregraphe simplified export in Python.
from naoqi import ALProxy
def rh_up_open(motion):
	names = list()
	times = list()
	keys = list()

	names.append("LElbowRoll")
	times.append([0.56])
	keys.append([-0.420076])

	names.append("LElbowYaw")
	times.append([0.56])
	keys.append([-1.20334])

	names.append("LHand")
	times.append([0.56])
	keys.append([0.291787])

	names.append("LShoulderPitch")
	times.append([0.56])
	keys.append([1.42838])

	names.append("LShoulderRoll")
	times.append([0.56])
	keys.append([0.234372])

	names.append("LWristYaw")
	times.append([0.56])
	keys.append([0.105453])

	names.append("RElbowRoll")
	times.append([0.56])
	keys.append([0.404656])

	names.append("RElbowYaw")
	times.append([0.56])
	keys.append([1.18272])

	names.append("RHand")
	times.append([0.56])
	keys.append([0.998613])

	names.append("RShoulderPitch")
	times.append([0.56])
	keys.append([0.176676])

	names.append("RShoulderRoll")
	times.append([0.56])
	keys.append([0.0456091])

	names.append("RWristYaw")
	times.append([0.56])
	keys.append([-1.20166])

	try:
	  motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  print err

def rh_up_closed(motion):
	names = list()
	times = list()
	keys = list()

	names.append("LElbowRoll")
	times.append([0.72])
	keys.append([-0.420076])

	names.append("LElbowYaw")
	times.append([0.72])
	keys.append([-1.20334])

	names.append("LHand")
	times.append([0.72])
	keys.append([0.291787])

	names.append("LShoulderPitch")
	times.append([0.72])
	keys.append([1.41652])

	names.append("LShoulderRoll")
	times.append([0.72])
	keys.append([0.254684])

	names.append("LWristYaw")
	times.append([0.72])
	keys.append([0.105453])

	names.append("RElbowRoll")
	times.append([0.72])
	keys.append([0.40112])

	names.append("RElbowYaw")
	times.append([0.72])
	keys.append([1.17523])

	names.append("RHand")
	times.append([0.72])
	keys.append([0.00435097])

	names.append("RShoulderPitch")
	times.append([0.72])
	keys.append([0.185244])

	names.append("RShoulderRoll")
	times.append([0.72])
	keys.append([0.0422499])

	names.append("RWristYaw")
	times.append([0.72])
	keys.append([-1.20166])

	try:
	  motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  print err

def lh_up_open(motion):
	names = list()
	times = list()
	keys = list()

	names.append("LElbowRoll")
	times.append([0.88])
	keys.append([-0.418385])

	names.append("LElbowYaw")
	times.append([0.88])
	keys.append([-1.20061])

	names.append("LHand")
	times.append([0.88])
	keys.append([0.998033])

	names.append("LShoulderPitch")
	times.append([0.88])
	keys.append([0.155382])

	names.append("LShoulderRoll")
	times.append([0.88])
	keys.append([0.19374])

	names.append("LWristYaw")
	times.append([0.88])
	keys.append([1.25211])

	names.append("RElbowRoll")
	times.append([0.88])
	keys.append([0.418385])

	names.append("RElbowYaw")
	times.append([0.88])
	keys.append([1.20061])

	names.append("RHand")
	times.append([0.88])
	keys.append([0.291787])

	names.append("RShoulderPitch")
	times.append([0.88])
	keys.append([1.44974])

	names.append("RShoulderRoll")
	times.append([0.88])
	keys.append([-0.224273])

	names.append("RWristYaw")
	times.append([0.88])
	keys.append([0.0935271])

	try:
	  motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  print err


def lh_up_closed(motion):
	names = list()
	times = list()
	keys = list()

	names.append("LElbowRoll")
	times.append([0.92])
	keys.append([-0.418385])

	names.append("LElbowYaw")
	times.append([0.92])
	keys.append([-1.20061])

	names.append("LHand")
	times.append([0.92])
	keys.append([0.297076])

	names.append("LShoulderPitch")
	times.append([0.92])
	keys.append([0.155382])

	names.append("LShoulderRoll")
	times.append([0.92])
	keys.append([0.19374])

	names.append("LWristYaw")
	times.append([0.92])
	keys.append([1.25211])

	names.append("RElbowRoll")
	times.append([0.92])
	keys.append([0.418385])

	names.append("RElbowYaw")
	times.append([0.92])
	keys.append([1.20061])

	names.append("RHand")
	times.append([0.92])
	keys.append([0.291787])

	names.append("RShoulderPitch")
	times.append([0.92])
	keys.append([1.44974])

	names.append("RShoulderRoll")
	times.append([0.92])
	keys.append([-0.224273])

	names.append("RWristYaw")
	times.append([0.92])
	keys.append([0.0935271])

	try:
	  motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  print err

def both_h_down(motion):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.8])
	keys.append([-0.169037])

	names.append("HeadYaw")
	times.append([0.8])
	keys.append([-0.00771189])

	names.append("LAnklePitch")
	times.append([0.8])
	keys.append([0.0764796])

	names.append("LAnkleRoll")
	times.append([0.8])
	keys.append([-0.096198])

	names.append("LElbowRoll")
	times.append([0.8])
	keys.append([-0.589406])

	names.append("LElbowYaw")
	times.append([0.8])
	keys.append([-1.20896])

	names.append("LHand")
	times.append([0.8])
	keys.append([0.327578])

	names.append("LHipPitch")
	times.append([0.8])
	keys.append([0.178901])

	names.append("LHipRoll")
	times.append([0.8])
	keys.append([0.0985544])

	names.append("LHipYawPitch")
	times.append([0.8])
	keys.append([-0.155683])

	names.append("LKneePitch")
	times.append([0.8])
	keys.append([-0.0903419])

	names.append("LShoulderPitch")
	times.append([0.8])
	keys.append([1.50457])

	names.append("LShoulderRoll")
	times.append([0.8])
	keys.append([0.196611])

	names.append("LWristYaw")
	times.append([0.8])
	keys.append([0.101606])

	names.append("RAnklePitch")
	times.append([0.8])
	keys.append([0.0766072])

	names.append("RAnkleRoll")
	times.append([0.8])
	keys.append([0.0866722])

	names.append("RElbowRoll")
	times.append([0.8])
	keys.append([0.512675])

	names.append("RElbowYaw")
	times.append([0.8])
	keys.append([1.31118])

	names.append("RHand")
	times.append([0.8])
	keys.append([0.350345])

	names.append("RHipPitch")
	times.append([0.8])
	keys.append([0.160597])

	names.append("RHipRoll")
	times.append([0.8])
	keys.append([-0.100796])

	names.append("RHipYawPitch")
	times.append([0.8])
	keys.append([-0.155683])

	names.append("RKneePitch")
	times.append([0.8])
	keys.append([-0.0806737])

	names.append("RShoulderPitch")
	times.append([0.8])
	keys.append([1.48782])

	names.append("RShoulderRoll")
	times.append([0.8])
	keys.append([-0.169331])

	names.append("RWristYaw")
	times.append([0.8])
	keys.append([0.146334])

	try:
	  motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  print err

def both_h_up_closed(motion):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.84])
	keys.append([-0.17])

	names.append("HeadYaw")
	times.append([0.84])
	keys.append([0])

	names.append("LAnklePitch")
	times.append([0.84])
	keys.append([0.0794489])

	names.append("LAnkleRoll")
	times.append([0.84])
	keys.append([-0.101617])

	names.append("LElbowRoll")
	times.append([0.84])
	keys.append([-0.582494])

	names.append("LElbowYaw")
	times.append([0.84])
	keys.append([-1.20675])

	names.append("LHand")
	times.append([0.84])
	keys.append([0.327578])

	names.append("LHipPitch")
	times.append([0.84])
	keys.append([0.170857])

	names.append("LHipRoll")
	times.append([0.84])
	keys.append([0.0991299])

	names.append("LHipYawPitch")
	times.append([0.84])
	keys.append([-0.163917])

	names.append("LKneePitch")
	times.append([0.84])
	keys.append([-0.0914416])

	names.append("LShoulderPitch")
	times.append([0.84])
	keys.append([0.218468])

	names.append("LShoulderRoll")
	times.append([0.84])
	keys.append([0.204639])

	names.append("LWristYaw")
	times.append([0.84])
	keys.append([1.17271])

	names.append("RAnklePitch")
	times.append([0.84])
	keys.append([0.0794488])

	names.append("RAnkleRoll")
	times.append([0.84])
	keys.append([0.0904404])

	names.append("RElbowRoll")
	times.append([0.84])
	keys.append([0.515347])

	names.append("RElbowYaw")
	times.append([0.84])
	keys.append([1.30961])

	names.append("RHand")
	times.append([0.84])
	keys.append([0.342786])

	names.append("RHipPitch")
	times.append([0.84])
	keys.append([0.152362])

	names.append("RHipRoll")
	times.append([0.84])
	keys.append([-0.109374])

	names.append("RHipYawPitch")
	times.append([0.84])
	keys.append([-0.163917])

	names.append("RKneePitch")
	times.append([0.84])
	keys.append([-0.081])

	names.append("RShoulderPitch")
	times.append([0.84])
	keys.append([0.188978])

	names.append("RShoulderRoll")
	times.append([0.84])
	keys.append([-0.177182])

	names.append("RWristYaw")
	times.append([0.84])
	keys.append([-1.28334])

	try:
	  motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  print err

def both_h_up_open(motion):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.96])
	keys.append([-0.17])

	names.append("HeadYaw")
	times.append([0.96])
	keys.append([0])

	names.append("LAnklePitch")
	times.append([0.96])
	keys.append([0.0794489])

	names.append("LAnkleRoll")
	times.append([0.96])
	keys.append([-0.101617])

	names.append("LElbowRoll")
	times.append([0.96])
	keys.append([-0.582313])

	names.append("LElbowYaw")
	times.append([0.96])
	keys.append([-1.20259])

	names.append("LHand")
	times.append([0.96])
	keys.append([0.999407])

	names.append("LHipPitch")
	times.append([0.96])
	keys.append([0.170857])

	names.append("LHipRoll")
	times.append([0.96])
	keys.append([0.0991299])

	names.append("LHipYawPitch")
	times.append([0.96])
	keys.append([-0.163917])

	names.append("LKneePitch")
	times.append([0.96])
	keys.append([-0.0914416])

	names.append("LShoulderPitch")
	times.append([0.96])
	keys.append([0.226562])

	names.append("LShoulderRoll")
	times.append([0.96])
	keys.append([0.20568])

	names.append("LWristYaw")
	times.append([0.96])
	keys.append([1.16975])

	names.append("RAnklePitch")
	times.append([0.96])
	keys.append([0.0794488])

	names.append("RAnkleRoll")
	times.append([0.96])
	keys.append([0.0904404])

	names.append("RElbowRoll")
	times.append([0.96])
	keys.append([0.515182])

	names.append("RElbowYaw")
	times.append([0.96])
	keys.append([1.30812])

	names.append("RHand")
	times.append([0.96])
	keys.append([0.998124])

	names.append("RHipPitch")
	times.append([0.96])
	keys.append([0.152362])

	names.append("RHipRoll")
	times.append([0.96])
	keys.append([-0.109374])

	names.append("RHipYawPitch")
	times.append([0.96])
	keys.append([-0.163917])

	names.append("RKneePitch")
	times.append([0.96])
	keys.append([-0.081])

	names.append("RShoulderPitch")
	times.append([0.96])
	keys.append([0.197153])

	names.append("RShoulderRoll")
	times.append([0.96])
	keys.append([-0.179905])

	names.append("RWristYaw")
	times.append([0.96])
	keys.append([-1.27435])

	try:
	  motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  print err



