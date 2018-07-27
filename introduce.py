# Choregraphe simplified export in Python.
from naoqi import ALProxy
import argparse
import qi
import numpy as np

def introduce():
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.68, 2.72])
    keys.append([[-0.368264, [3, -0.24, 0], [3, 0.68, 0]], [-0.230569, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.68, 2.72])
    keys.append([[-0.79587, [3, -0.24, 0], [3, 0.68, 0]], [-0.930466, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([5])
    keys.append([[0.56, [3, -1.68, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0, 0.68, 2.72, 4.64, 5])
    keys.append([[1.5865, [3, -0.0133333, 0], [3, 0.226667, 0]], [1.40324, [3, -0.226667, 0], [3, 0.68, 0]], [1.54094, [3, -0.68, 0], [3, 0.64, 0]], [1.17955, [3, -0.64, 0], [3, 0.12, 0]], [1.54736, [3, -0.12, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0, 0.68, 2.72])
    keys.append([[0.0366519, [3, -0.0133333, 0], [3, 0.226667, 0]], [0.207694, [3, -0.226667, 0], [3, 0.68, 0]], [0.0929366, [3, -0.68, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0, 0.68, 4.64, 5])
    keys.append([[-0.659734, [3, -0.0133333, 0], [3, 0.226667, 0]], [-1.26711, [3, -0.226667, 0.043987], [3, 1.32, -0.256159]], [-1.5666, [3, -1.32, 0], [3, 0.12, 0]], [-1.10846, [3, -0.12, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0, 0.68, 1.04, 2.04, 2.72])
    keys.append([[0.115021, [3, -0.0133333, 0], [3, 0.226667, 0]], [0.545106, [3, -0.226667, -0.349663], [3, 0.12, 0.185116]], [1.71936, [3, -0.12, -2.39684e-07], [3, 0.333333, 6.6579e-07]], [1.71936, [3, -0.333333, 0], [3, 0.226667, 0]], [0.440472, [3, -0.226667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0, 0.68, 1.04, 2.04, 2.72])
    keys.append([[0.229076, [3, -0.0133333, 0], [3, 0.226667, 0]], [1.43117, [3, -0.226667, 0], [3, 0.12, 0]], [0.929199, [3, -0.12, 0], [3, 0.333333, 0]], [0.929199, [3, -0.333333, 0], [3, 0.226667, 0]], [0.0889619, [3, -0.226667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0, 0.68, 1.04, 2.04, 2.72])
    keys.append([[0.56, [3, -0.0133333, 0], [3, 0.226667, 0]], [0.73, [3, -0.226667, 0], [3, 0.12, 0]], [0.32, [3, -0.12, 0], [3, 0.333333, 0]], [0.32, [3, -0.333333, 0], [3, 0.226667, 0]], [0.69, [3, -0.226667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0, 0.68, 1.04, 2.04, 2.72])
    keys.append([[1.36023, [3, -0.0133333, 0], [3, 0.226667, 0]], [1.37183, [3, -0.226667, 0], [3, 0.12, 0]], [0.840732, [3, -0.12, 0], [3, 0.333333, 0]], [0.840732, [3, -0.333333, 0], [3, 0.226667, 0]], [1.35023, [3, -0.226667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0, 0.68, 1.04, 2.04, 2.72])
    keys.append([[0.104898, [3, -0.0133333, 0], [3, 0.226667, 0]], [-0.333358, [3, -0.226667, 0.162407], [3, 0.12, -0.08598]], [-0.640262, [3, -0.12, 2.87621e-07], [3, 0.333333, -7.98948e-07]], [-0.640263, [3, -0.333333, 0], [3, 0.226667, 0]], [-0.140883, [3, -0.226667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1.04, 2.04])
    keys.append([[0.759059, [3, -0.36, 0], [3, 0.333333, 0]], [0.759059, [3, -0.333333, 0], [3, 0, 0]]])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", "192.168.1.43", 9559)
      tts = ALProxy("ALTextToSpeech", "192.168.1.43", 9559)
      #motion = ALProxy("ALMotion")
      id = motion.post.angleInterpolationBezier(names, times, keys)
      #motion.wait(id,0)
      tts.say("\\rspd=80\\ \\emph=1\\ Hello \\eos=1\\  \\pau=350\\  \\rspd=80\\ \\mrk=0\\ \\emph=0\\ \\rspd=70\\ My \\emph=2\\ \\rspd=80\\ name is \\rspd=70\\ Pepper  \\pau=700\\ \\rspd=70\\ It is \\emph=1\\ nice \\rspd=85\\ to meet you!")
    except BaseException, err:
      print err

def escapeRoom():
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.24, 0.44, 0.68, 1.68])
    keys.append([[-0.206645, [3, -0.0933333, 0], [3, 0.0666667, 0]], [-0.0952972, [2, -0.08, 0.0270976], [2, 0.096, -0.0325171]], [-0.27168, [3, -0.08, 0], [3, 0.333333, 0]], [-0.27168, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("HipPitch")
    times.append([0.76, 1.4])
    keys.append([[-0.110514, [3, -0.266667, 0], [3, 0.213333, 0]], [-0.04043, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("HipRoll")
    times.append([0.76, 1.4])
    keys.append([[-0.0243873, [3, -0.266667, 0], [3, 0.213333, 0]], [-0.0564659, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("KneePitch")
    times.append([0.76, 1.4])
    keys.append([[0.0437812, [3, -0.266667, 0], [3, 0.213333, 0]], [-0.00637515, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.56, 1.04, 1.44, 1.60])
    keys.append([[-1.21387, [3, -0.2, 0], [3, 0.16, 0]], [-0.946839, [3, -0.16, 0], [3, 0.133333, 0]],
                [-1.18497, [3, -0.133333, 0], [3, 0, 0]], [-0.116583, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([1.04, 1.44, 1.60])
    keys.append([[-1.34689, [3, -0.36, 0], [3, 0.133333, 0]], [-1.17815, [3, -0.133333, 0], [3, 0, 0]],
                [-1.71039, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1.04, 1.44, 1.60])
    keys.append([[0.3036, [3, -0.36, 0], [3, 0.133333, 0]], [0.3036, [3, -0.133333, 0], [3, 0, 0]],
                [0.679262, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([1.04, 1.44, 1.60])
    keys.append([[1.54623, [3, -0.36, 0], [3, 0.133333, 0]], [1.54623, [3, -0.133333, 0], [3, 0, 0]],
                [1.76561, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.56, 1.04, 1.44, 1.60])
    keys.append([[0.66748, [3, -0.2, 0], [3, 0.16, 0]], [0.349811, [3, -0.16, 0], [3, 0.133333, 0]], [0.388161, [3, -0.133333, 0], [3, 0, 0]],
                [0.076699, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1.04, 1.44, 1.60])
    keys.append([[-0.550747, [3, -0.36, 0], [3, 0.133333, 0]], [-0.227074, [3, -0.133333, 0], [3, 0, 0]],
                [0.05058, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.52, 1.28, 1.56, 1.60])
    keys.append([[1.13022, [3, -0.186667, 0], [3, 0.253333, 0]], [0.652003, [3, -0.253333, 0], [3, 0.0933333, 0]], [1.13022, [3, -0.0933333, 0], [3, 0, 0]],
                [0.0966408, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.92, 1.56, 1.60])
    keys.append([[2.02404, [3, -0.32, 0], [3, 0.213333, 0]], [1.16366, [3, -0.213333, 0], [3, 0, 0]],
                [1.70272, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.52, 0.92, 1.28, 1.56, 1.60])
    keys.append([[0.25, [3, -0.186667, 0], [3, 0.133333, 0]], [1, [3, -0.133333, 0], [3, 0.12, 0]], [0.37, [3, -0.12, 0.151875], [3, 0.0933333, -0.118125]], [0.19, [3, -0.0933333, 0], [3, 0, 0]],
                [0.675747, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.52, 1.56, 1.60])
    keys.append([[1.06465, [3, -0.186667, 0], [3, 0.346667, 0]], [1.55398, [3, -0.346667, 0], [3, 0, 0]],
                [1.7472, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.92, 1.56, 1.60])
    keys.append([[-0.485688, [3, -0.32, 0], [3, 0.213333, 0]], [-0.25431, [3, -0.213333, 0], [3, 0, 0]],
                [-0.081301, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.92, 1.56, 1.60])
    keys.append([[1.66588, [3, -0.32, 0], [3, 0.213333, 0]], [0.0506146, [3, -0.213333, 0], [3, 0, 0]],
                [-0.024586, [3, -0.0133333, 0], [3, 0, 0]]])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      # motion = ALProxy("ALMotion", IP, 9559)
      motion = ALProxy("ALMotion", "192.168.1.43", 9559)
      postureProxy = ALProxy("ALRobotPosture", "192.168.1.43", 9559)
      tts = ALProxy("ALTextToSpeech", "192.168.1.43", 9559)
      #motion = ALProxy("ALMotion")
      id = motion.post.angleInterpolationBezier(names, times, keys)
      #motion.wait(id,0)
      tts.say("\\rspd=80\\ Have \\emph=1\\ you played an escape room before?")
      postureProxy.goToPosture("Stand", 0.8)
    except BaseException, err:
      print err

escapeRoom()


# names = list()
# times = list()
# keys = list()
#
# names.append("LElbowRoll")
# times.append([0])
# keys.append([[-0.116583, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("LElbowYaw")
# times.append([0])
# keys.append([[-1.71039, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("LHand")
# times.append([0])
# keys.append([[0.679262, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("LShoulderPitch")
# times.append([0])
# keys.append([[1.76561, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("LShoulderRoll")
# times.append([0])
# keys.append([[0.076699, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("LWristYaw")
# times.append([0])
# keys.append([[0.05058, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("RElbowRoll")
# times.append([0])
# keys.append([[0.0966408, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("RElbowYaw")
# times.append([0])
# keys.append([[1.70272, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("RHand")
# times.append([0])
# keys.append([[0.675747, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("RShoulderPitch")
# times.append([0])
# keys.append([[1.7472, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("RShoulderRoll")
# times.append([0])
# keys.append([[-0.081301, [3, -0.0133333, 0], [3, 0, 0]]])
#
# names.append("RWristYaw")
# times.append([0])
# keys.append([[-0.024586, [3, -0.0133333, 0], [3, 0, 0]]])
#
# try:
#   # uncomment the following line and modify the IP if you use this script outside Choregraphe.
#   # motion = ALProxy("ALMotion", IP, 9559)
#   motion = ALProxy("ALMotion")
#   motion.angleInterpolationBezier(names, times, keys)
# except BaseException, err:
#   print err
