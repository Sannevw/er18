row=2# import all the good stuff
import sys
from naoqi import ALProxy
import argparse
import qi
import paramiko
import socket
import logging
import datetime
import os

from Tkinter import *
import tkMessageBox

width = 20
# def createButton(xpos =0, ypos =0, width = 100, height = 20):
#         button = pygame.Rect(xpos, ypos, width, height)
#         return button
#
# def drawButton(screen, button, color = [183,181,181], font = 'arial', text = "Hello World", textCol = [0,0,0], xpos =0, ypos =0):
#         font_ = pygame.font.SysFont('None', 16)
#         pygame.draw.rect(screen, color, button)  # draw button
#         label = font_.render(text, True, textCol)
#         screen.blit(label, (xpos, ypos))


class WOZGUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1200x768")
        self.history = []
        self.action = ''
        self.var = StringVar()
        self.UDP_IP = "192.168.1.223"
        self.UDP_PORT = 9930
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            self.motion = ALProxy("ALMotion", "192.168.1.43", 9559)
            self.motion.setOrthogonalSecurityDistance(0.08)
            self.al = ALProxy("ALAutonomousLife", "192.168.1.43", 9559)
            self.tts = ALProxy("ALTextToSpeech", "192.168.1.43", 9559)
            self.postureProxy = ALProxy("ALRobotPosture", "192.168.1.43", 9559)
            self.postureProxy = ALProxy("ALRobotPosture", "192.168.1.43", 9559)

            print self.al.getState()
            if self.al.getState() != "disabled":
                print("turn autonomous life off")
                self.al.setState("disabled")
            print(self.motion.robotIsWakeUp())
            if not self.motion.robotIsWakeUp():
                print("wake the robot up")
                self.motion.wakeUp()
                    #al.setState("disabled")
                    #motion.wakeUp()
        except BaseException, err:
            print err

    # create some functions so that the robot can exhibit super intelligent social behaviors and be awesome

    """
    Q: Have you played an escape room before (accompanied with some gestures)
    """
    def escapeRoom(self):
        logging.info("[ACTION] escapeRoom")
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.24, 0.44, 0.68, 1.68])
        keys.append([[-0.206645, [3, -0.0933333, 0], [3, 0.0666667, 0]], [-0.0952972, [2, -0.08, 0.0270976], [2, 0.096, -0.0325171]], [-0.27168, [3, -0.08, 0], [3, 0.333333, 0]],
                    [-0.27168, [3, -0.333333, 0], [3, 0, 0]]])

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
        times.append([0.56, 1.04, 1.44, 1.80])
        keys.append([[-1.21387, [3, -0.2, 0], [3, 0.16, 0]], [-0.946839, [3, -0.16, 0], [3, 0.133333, 0]],
                    [-1.18497, [3, -0.133333, 0], [3, 0, 0]], [-0.116583, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([1.04, 1.44, 1.80])
        keys.append([[-1.34689, [3, -0.36, 0], [3, 0.133333, 0]], [-1.17815, [3, -0.133333, 0], [3, 0, 0]],
                    [-1.71039, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([1.04, 1.44, 1.80])
        keys.append([[0.3036, [3, -0.36, 0], [3, 0.133333, 0]], [0.3036, [3, -0.133333, 0], [3, 0, 0]],
                    [0.679262, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([1.04, 1.44, 1.80])
        keys.append([[1.54623, [3, -0.36, 0], [3, 0.133333, 0]], [1.54623, [3, -0.133333, 0], [3, 0, 0]],
                    [1.76561, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.56, 1.04, 1.44, 2.20])
        keys.append([[0.66748, [3, -0.2, 0], [3, 0.16, 0]], [0.349811, [3, -0.16, 0], [3, 0.133333, 0]], [0.388161, [3, -0.133333, 0], [3, 0, 0]],
                    [0.076699, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([1.04, 1.44, 1.80])
        keys.append([[-0.550747, [3, -0.36, 0], [3, 0.133333, 0]], [-0.227074, [3, -0.133333, 0], [3, 0, 0]],
                    [0.05058, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.52, 1.28, 1.56, 2.00])
        keys.append([[1.13022, [3, -0.186667, 0], [3, 0.253333, 0]], [0.652003, [3, -0.253333, 0], [3, 0.0933333, 0]], [1.13022, [3, -0.0933333, 0], [3, 0, 0]],
                    [0.0966408, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.92, 1.56, 1.80])
        keys.append([[2.02404, [3, -0.32, 0], [3, 0.213333, 0]], [1.16366, [3, -0.213333, 0], [3, 0, 0]],
                    [1.70272, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.52, 0.92, 1.28, 1.56, 1.80])
        keys.append([[0.25, [3, -0.186667, 0], [3, 0.133333, 0]], [1, [3, -0.133333, 0], [3, 0.12, 0]], [0.37, [3, -0.12, 0.151875], [3, 0.0933333, -0.118125]], [0.19, [3, -0.0933333, 0], [3, 0, 0]],
                    [0.675747, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.52, 1.56, 1.80])
        keys.append([[1.06465, [3, -0.186667, 0], [3, 0.346667, 0]], [1.55398, [3, -0.346667, 0], [3, 0, 0]],
                    [1.7472, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.92, 1.56, 1.80])
        keys.append([[-0.485688, [3, -0.32, 0], [3, 0.213333, 0]], [-0.25431, [3, -0.213333, 0], [3, 0, 0]],
                    [-0.081301, [3, -0.0133333, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.92, 1.56, 1.60])
        keys.append([[1.66588, [3, -0.32, 0], [3, 0.213333, 0]], [0.0506146, [3, -0.213333, 0], [3, 0, 0]],
                    [-0.024586, [3, -0.0133333, 0], [3, 0, 0]]])

        try:
          #self.motion = ALProxy("ALself.motion")
          id = self.motion.post.angleInterpolationBezier(names, times, keys)
          #self.motion.wait(id,0)
          self.tts.say("\\rspd=80\\ Have \\emph=1\\ you played an escape room before?")
          #self.postureProxy.goToPosture("Stand", 0.8)
        except BaseException, err:
          print err

    """
    This function returns the names of the joints, the time steps and the keys needed to make the robot
    wave with its right arms.

    """
    def wave_goodbye(self):
        logging.info("[ACTION] wave_goodbye")
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.72, 1.56, 8.56])
        keys.append([[-0.17209, [3, -0.253333, 0], [3, 0.28, 0]], [-0.210756, [3, -0.28, 0], [3, 2.33333, 0]], [0.0127584, [3, -2.33333, 0], [3, 0, 0]]])

        names.append("HeadYaw")
        times.append([1.56])
        keys.append([[-0.0423813, [3, -0.533333, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([0.72, 1.56, 3.04, 4.28, 4.92, 5.56])
        keys.append([[-0.00872665, [3, -0.253333, 0], [3, 0.28, 0]], [-1.29852, [3, -0.28, 0], [3, 0.493333, 0]], [-0.841249, [3, -0.493333, -0.186767], [3, 0.413333, 0.156481]], [-0.268781, [3, -0.413333, 0], [3, 0.213333, 0]], [-0.605629, [3, -0.213333, 0], [3, 0.213333, 0]], [-0.244346, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.72, 1.56, 3.04, 4.28, 4.92, 5.56])
        keys.append([[-0.895354, [3, -0.253333, 0], [3, 0.28, 0]], [-1.78024, [3, -0.28, 0], [3, 0.493333, 0]], [-1.65108, [3, -0.493333, -0.0664765], [3, 0.413333, 0.0556966]], [-1.41372, [3, -0.413333, 0], [3, 0.213333, 0]], [-1.82911, [3, -0.213333, 0], [3, 0.213333, 0]], [-0.719076, [3, -0.213333, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([4.28, 5.56])
        keys.append([[0.64, [3, -1.44, 0], [3, 0.426667, 0]], [0.5, [3, -0.426667, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([1.56, 4.28])
        keys.append([[-1.02974, [3, -0.533333, 0], [3, 0.906667, 0]], [-0.858702, [3, -0.906667, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([3.04, 4.28, 4.92, 5.56, 6.6, 8.56])
        keys.append([[1.06291, [3, -1.02667, 0], [3, 0.413333, 0]], [1.56207, [3, -0.413333, 0], [3, 0.213333, 0]], [0.598648, [3, -0.213333, 0], [3, 0.213333, 0]], [1.56207, [3, -0.213333, 0], [3, 0.346667, 0]], [0.598648, [3, -0.346667, 0], [3, 0.653333, 0]], [0.619592, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([3.04, 4.28, 4.92, 5.56, 6.6, 8.56])
        keys.append([[1.29503, [3, -1.02667, 0], [3, 0.413333, 0]], [1.29503, [3, -0.413333, 0], [3, 0.213333, 0]], [1.29503, [3, -0.213333, 0], [3, 0.213333, 0]], [1.29503, [3, -0.213333, 0], [3, 0.346667, 0]], [1.29503, [3, -0.346667, 0], [3, 0.653333, 0]], [1.12225, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([3.04, 4.28, 4.92, 5.56, 6.6, 8.56])
        keys.append([[0.97, [3, -1.02667, 0], [3, 0.413333, 0]], [0.97, [3, -0.413333, 0], [3, 0.213333, 0]], [0.97, [3, -0.213333, 0], [3, 0.213333, 0]], [0.97, [3, -0.213333, 0], [3, 0.346667, 0]], [0.97, [3, -0.346667, 0], [3, 0.653333, 0]], [0.66, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([3.04, 4.28, 4.92, 5.56, 6.6, 8.56])
        keys.append([[0.0174533, [3, -1.02667, 0], [3, 0.413333, 0]], [0.0174533, [3, -0.413333, 0], [3, 0.213333, 0]], [0.0174533, [3, -0.213333, 0], [3, 0.213333, 0]], [0.0174533, [3, -0.213333, 0], [3, 0.346667, 0]], [0.0174533, [3, -0.346667, 0], [3, 0.653333, 0]], [1.56731, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([3.04, 4.28, 4.92, 5.56, 6.6, 8.56])
        keys.append([[-0.825541, [3, -1.02667, 0], [3, 0.413333, 0]], [-0.825541, [3, -0.413333, 0], [3, 0.213333, 0]], [-0.825541, [3, -0.213333, 0], [3, 0.213333, 0]], [-0.825541, [3, -0.213333, 0], [3, 0.346667, 0]], [-0.825541, [3, -0.346667, 0], [3, 0.653333, 0]], [-0.247837, [3, -0.653333, 0], [3, 0, 0]]])

        try:
            id = self.motion.post.angleInterpolationBezier(names, times, keys)
            self.tts.say("\\pau=800\\ It was nice to meet you. \\pau=1000\\ See you next time. Bye!")
        except BaseException, err:
            print err

    def keyup(self, e):
        if e.keycode in self.history:
            self.history.pop(self.history.index(e.keycode))

    def keydown(self, e):
        if not e.keycode in self.history:
            self.history.append(e.keycode)

    def resetKey(self, event):
        logging.info("[ACTION] resetKey reset the nao OS")
        self.motion.move(0.0,0.0,0.0)
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.1.43', username='nao', password='naonaonao')
        channel = ssh.invoke_shell()
        stdin = channel.makefile('wb')
        stdin.write('''
            plink -P 22 nao@192.168.1.43 -pw "naonaonao"
            nao restart
            ''')

    # def downKey(self,event):
    #     if not event.keycode in history:
    #         history.append(event.keycode)
    #     self.motion.move(-0.8,0.0,0.0)
    #
    # def onkeyRelease(self, event):
    #     if event.keycode in history:
    #         history.pop(history.index(event.keycode))
    #     self.motion.move(0.0,0.0,0.0)

    def quit(self):
        logging.info("[ACTION] quit")
        if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
            self.sock.close()
            self.root.destroy()


    def setAction(self, action):
        self.action = action
        self.var.set(action)

    def performAction(self, event):
        if self.input:
            self.action = 'sayInputText'
            self.input = False
        self.funcs[self.action]()

    def movementFunc(self):
        if self.history != []:
            if 38 in self.history and 37 in self.history:
                # FORWARD LEFT
                self.motion.move(0.8,0.0,0.3)
            elif 38 in self.history and 39 in self.history:
                # FORWARD RIGHT
                self.motion.move(0.8,0.0,-0.3)
            elif 40 in self.history and 37 in self.history:
                # BACK LEFT
                self.motion.move(-0.8,0.0,0.3)
            elif 40 in self.history and 39 in self.history:
                # BACK RIGHT
                self.motion.move(-0.8,0.0,-0.3)
            elif 38 in self.history:
                self.motion.move(1.0,0.0,0.0)
            elif 37 in self.history:
                # LEFT
                self.motion.move(0.0,0.0,0.78)
            elif 39 in self.history:
                # RIGHT
                self.motion.move(0.0,0.0,-0.78)
            elif 40 in self.history:
                self.motion.move(-0.8,0.0,0.0)
        else:
            self.motion.move(0.0,0.0,0.0)

        # periodic function: keep checking if key arrows are pressed.
        self.root.after(25, self.movementFunc)

    def retrieve_input(self):
        return self.textBox.get("1.0",'end-1c')

    def delete_input(self):
        self.textBox.delete('1.0', END)
        logging.info("[ACTION] text input deleted")

    def sayText(self, text):
        try:
            self.tts.say(text)
            logging.debug("[DEBUG] sayText with text: %s" % text)
        except:
            pass

    def setInput(self, event):
        self.input = True

    def sayInputText(self):
        text = self.retrieve_input()
        self.delete_input()
        self.tts.say(str(text))
        logging.debug("[DEBUG] sayText with text: %s" % text)

    def showMaze(self):
        print 'showmaze'
        msg = '[MAZE] show'
        self.sock.sendto(msg, (self.UDP_IP, self.UDP_PORT))
        logging.info("[ACTION] showMaze msg send to remote laptop")

    def startGame(self):
        msg = '[GAME] start'
        self.sock.sendto(msg, (self.UDP_IP, self.UDP_PORT))
        logging.info("[ACTION] startGame msg send to remote laptop")

    def main(self):

        a_label = Label(self.root, textvariable = self.var).grid(row=2, column=1)

        self.root.bind('f5', self.resetKey)
        self.root.bind('<KeyPress>', self.keydown)
        self.root.bind('<KeyRelease>', self.keyup)
        self.root.bind('<Return>', self.performAction)
        self.input = False
        self.funcs = {'escapeRoom': self.escapeRoom, 'wave_goodbye': self.wave_goodbye, 'sayInputText': self.sayInputText}

        # ANIMATED BEHAVIORS
        lblBeh = Label(self.root, text="ANIMATED BEHAVIORS").grid(row=2,column=0, columnspan=4, sticky=W+E)
        wavebutton = Button(self.root, height=1, width=width, text="wave_goodbye", fg="red", command=lambda: self.setAction('wave_goodbye')).grid(row=3,column=0)
        escaperoombutton = Button(self.root, height=1, width=width, text="escapeRoom", fg="red", command=lambda: self.setAction('escapeRoom')).grid(row=3,column=1,padx=(0,10))

        # UTTERANCES
        lbl = Label(self.root, text="UTTERANCES").grid(row=2,column=4,columnspan=4,sticky=W+E)

        # (DIS) AGREEMENT
        nobutton = Button(self.root, height=1, width=width, text="no", fg="blue", command=lambda: self.sayText('no')).grid(row=3, column=3,sticky=E+W)
        yesbutton = Button(self.root, height=1, width=width, text="yes", fg="blue", command=lambda: self.sayText('yes')).grid(row=4, column=3,sticky=E+W)
        agreebutton = Button(self.root, height=1, width=width, text="I agree", fg="blue", command=lambda: self.sayText("I agree")).grid(row=5, column=3,sticky=E+W)
        disagreebutton = Button(self.root, height=1, width=width, text="I do not agree", fg="blue", command=lambda: self.sayText("I do not agree")).grid(row=6, column=3,sticky=E+W)

        # UNCERTAINTY
        idkbutton = Button(self.root, height=1, width=width, text="I don't know", fg="blue", command=lambda: self.sayText("I don't know")).grid(row=3, column=4,sticky=E+W)
        maybebutton = Button(self.root, height=1, width=width, text="Maybe", fg="blue", command=lambda: self.sayText("Maybe")).grid(row=4, column=4,sticky=E+W)
        clarbutton = Button(self.root, height=1, width=width, text="What do you mean?", fg="blue", command=lambda: self.sayText("What do you mean?")).grid(row=5, column=4,sticky=E+W)
        repeatbutton = Button(self.root, height=1, width=width, text="Can you say that again?", fg="blue", command=lambda: self.sayText("Can you say that again?")).grid(row=6, column=4,sticky=E+W)
        #clarbutton = Button(self.root, height=1, width=width, text="What do you mean?", fg="blue", command=lambda: self.sayText("What do you mean?")).grid(row=5, column=4,sticky=E+W)

        # CAPABILITY
        canbutton = Button(self.root, height=1, width=width, text="I can do that", fg="blue", command=lambda: self.sayText("I can do that")).grid(row=3, column=5,sticky=E+W)
        cannotbutton = Button(self.root, height=1, width=width, text="I cannot do that", fg="blue", command=lambda: self.sayText("I cannot do that")).grid(row=4, column=5,sticky=E+W)

        # APOLOGIES
        lab = Label(self.root, width=20).grid(row=7, column=3)
        sorrybutton = Button(self.root, height=1, width=width, text="Sorry", fg="blue", command=lambda: self.sayText("Sorry")).grid(row=8, column=3,sticky=E+W)
        meannotbutton = Button(self.root, height=1, width=width, text="I did not mean that", fg="blue", command=lambda: self.sayText("I did not mean that")).grid(row=9, column=3,sticky=E+W)

        lbl = Label(self.root, text="GAME ACTIONS").grid(row=0,column=0,columnspan=4,sticky=W+E)
        startGame = Button(self.root, height=1, width=width, text="Start Game", fg="purple", command=self.startGame).grid(row=1, column=0, sticky=E+W)
        showmazebutton = Button(self.root, height=1, width=width, text="Show Maze", fg="purple", command=self.showMaze).grid(row=1, column=1, sticky=E+W)
        self.textBox = Text(self.root, height=1, width=40, padx=2)
        self.textBox.grid(row=3,column=10, sticky=E+W)
        self.textBox.bind('<Enter>', self.setInput)
        #buttonCommit = Button(self.root, height=1, width=10, text="commit", command=self.sayInputText).grid(row=4,column=10,sticky=E+W)
        quitbutton = Button(self.root, text="Quit", fg="red", command=self.quit).grid(row=1,column=5, padx=(10,1), pady=(1,30))

        # OPTIONS = [
        #     "escapeRoom",
        #     "wave goodbye"
        # ]
        # var_menu = StringVar(self.root)
        # var_menu.set(OPTIONS[0])
        # w = apply(OptionMenu, (self.root, var_menu) + tuple(OPTIONS))
        # w.grid(row=6,column=0)
        self.root.after(25,self.movementFunc)
        self.root.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.43",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    parser.add_argument("--pp_nr", type=int, required=True,
                        help="Participant number is required!")

    args = parser.parse_args()
    filename = "log_woz_interaction_"+str(datetime.datetime.now())[:10]+"_pp"+str(args.pp_nr)

    ## check if file already exists, if so ask user if they want to add to that file.
    if not os.path.isfile(filename):
        logger = logging.basicConfig(filename=filename,
                                                        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                                                        level=logging.DEBUG)
    else:
        print("This file already exists. Do you want to add to this file? [y/n]")
        ans = raw_input()
        if ans == 'y' or ans == 'yes':
            pass
        elif ans == 'n' or ans == 'no':
            print("Please enter a unique pp_nr")
            sys.exit()
        else:
            print("Please anwer with [y/n], do you want to add to this file?")

    wozgui = WOZGUI()
    wozgui.main()
