#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use wakeUp Method"""

import qi
import argparse
import sys
import time


def main(session,action):
    """
    This example uses the wakeUp method.
    """
    # Get the service ALMotion.

    motion_service  = session.service("ALMotion")
    if action =="wakeup":
        motion_service.wakeUp()

    # # print motion state
    # print motion_service.getSummary()
    # time.sleep(4.0)

    # Go to rest position
    else:
        motion_service.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.43",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    parser.add_argument('--action', type=str, default="wakeup",
                        help="whether Pepper should wakeup or rest")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session, args.action)
