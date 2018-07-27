# Choregraphe simplified export in Python.
from naoqi import ALProxy
import argparse
import qi

names = list()
times = list()
keys = list()

names.append("RElbowRoll")
times.append([1.12, 2.16, 3.08, 3.92, 4.8, 5.56, 7.84])
keys.append([1.15715, 0.851721, 1.15715, 0.851721, 1.15715, 0.671952, 0.0589591])

names.append("RElbowYaw")
times.append([5.56, 6.56])
keys.append([1.41721, 1.13272])

names.append("RHand")
times.append([5.56, 6.56])
keys.append([0.75, 0.74])

names.append("RShoulderPitch")
times.append([1.12, 3.08, 4.8, 6.56])
keys.append([0.0733038, 0.0733038, 0.0733038, 1.27235])

names.append("RShoulderRoll")
times.append([1.12, 3.08, 4.8, 6.56, 7.84])
keys.append([-1.15366, -1.15366, -1.15366, -0.244346, -0.0226893])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.43",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["HumanGreeter", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", "192.168.1.43", 9559)
      #motion = ALProxy("ALMotion")
      print("times: ", times)
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err
