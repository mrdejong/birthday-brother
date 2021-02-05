import pyttsx3
from time import sleep
import json


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[7].id) # voice 7 is a brithish male voice.

    def speak(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()


class Line:
    line = ""
    reaction = ""
    interval = 0
    debug_interval = 0
    debug = True
    debug_no_voice = True
    last_line = False
    previous = None

    def __init__(self, line, last_line):
        self.line = line['jarvis']
        self.reaction = line['reaction']
        self.interval = line['interval']
        self.debug_interval = line['debug_interval']
        self.speaker = Speaker()
        self.last_line = last_line

    def start_after_interval(self):
        if self.previous != None:
            print("Self: %s" % self.previous.reaction)

        if self.debug == True:
            sleep(self.debug_interval/2)
        else:
            sleep(self.interval)
        if self.debug_no_voice == False:
            self.speaker.speak(self.line)
        else:
            print("Jarvis: %s" % self.line)

        if self.last_line == True:
            print("Self: %s" % self.reaction)


class Jarvis:
    lines = []

    def __init__(self, script_file):
        with open(script_file) as f:
            self.parse(json.loads(f.read()))

    def parse(self, sets):
        last = None
        i = 0
        for line in sets:
            i = i + 1
            print(bool(len(sets) == i))
            l = Line(line, bool(len(sets) == i))
            l.previous = last
            last = l
            self.lines.append(l)

    def run(self):
        for line in self.lines:
            line.start_after_interval()


jar = Jarvis('./lines.json')
jar.run()

