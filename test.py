# Choregraphe beziner export in Python.
from naoqi import ALProxy
import cv2
import argparse
import pyopenpose as op



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
    parser.add_argument("--image_path",
                        default="~/Documents/hci-project/openpose/build/examples/media/COCO_val2014_000000000192.jpg",
                        help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
    args = parser.parse_known_args()

    # Custom Params (refer to include/openpose/flags.hpp for more parameters)
    params = dict()
    params["model_folder"] = "/home/anton/Documents/hci-project/openpose/build/models"
    params["net_resolution"] = "320x176"
    params["hand"] = True
    # params["hand_detector"] = 2
    params["body"] = 1
    # params["display"] = 1
    # params["face"] =
    # params["disable_blending"] = 1

    # Add others in path?
    for i in range(0, len(args[1])):
        curr_item = args[1][i]
        if i != len(args[1]) - 1:
            next_item = args[1][i + 1]
        else:
            next_item = "1"
        if "--" in curr_item and "--" in next_item:
            key = curr_item.replace('-', '')
            if key not in params:  params[key] = "1"
        elif "--" in curr_item and "--" not in next_item:
            key = curr_item.replace('-', '')
            if key not in params: params[key] = next_item

    # Construct it from system arguments Fixed the handRectangles to only 1 person and 1 big rectangle, don't have to
    # keep changing rectangle handRectangles = [[op.Rectangle(100.0, 100.0, 320.0, 320.0),op.Rectangle(0., 0., 0.,
    # 0.)], [op.Rectangle(325.0, 100.0, 320.0, 320.0),op.Rectangle(0., 0., 0., 0.)]]

    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    poseModel = op.PoseModel.BODY_25
    print(op.getPoseBodyPartMapping(poseModel))

    x = True
    # while x==True:
    #	motion = ALProxy("ALMotion", "localhost", 46309)
    #	motion.angleInterpolationBezier(names, times, keys)

    font = cv2.FONT_HERSHEY_SIMPLEX
    datum = op.Datum()
    # datum.handRectangles = handRectangles
    cam = cv2.VideoCapture(0)  # modify here for camera number
    while (cv2.waitKey(1) != 27):
        # Get camera frame
        ret, frame = cam.read()
        datum.cvInputData = frame
        opWrapper.emplaceAndPop([datum])
        frame = datum.cvOutputData
        print('Number of people: ', datum.poseKeypoints)


        # print('Number of bodyparts: ', datum.poseKeypoints.getSize(1))

        # cv2.rectangle(frame, (100,100), (320,320), (0, 255, 0), 1, 1)
        # cv2.rectangle(frame, (325,100), (545,320), (0, 0, 255), 1, 1)
        cv2.imshow("Webcam", frame)  # datum.cvOutputData)
    # Always clean up
    cam.release()
    cv2.destroyAllWindows()


main()
