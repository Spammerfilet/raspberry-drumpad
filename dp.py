#volume up/down
#shutdown/reboot
#auostart

import pygame
import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(29, GPIO.RISING)
GPIO.add_event_detect(31, GPIO.RISING)
GPIO.add_event_detect(7, GPIO.RISING)
GPIO.add_event_detect(8, GPIO.RISING)
GPIO.add_event_detect(10, GPIO.RISING)
GPIO.add_event_detect(11, GPIO.RISING)
GPIO.add_event_detect(12, GPIO.RISING)
GPIO.add_event_detect(13, GPIO.RISING)
GPIO.add_event_detect(15, GPIO.RISING)
GPIO.add_event_detect(16, GPIO.RISING)
GPIO.add_event_detect(18, GPIO.RISING)
GPIO.add_event_detect(19, GPIO.RISING)
GPIO.add_event_detect(21, GPIO.RISING)
GPIO.add_event_detect(22, GPIO.RISING)
GPIO.add_event_detect(23, GPIO.RISING)
GPIO.add_event_detect(24, GPIO.RISING)

GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #shutdown/reboot

GPIO.setup(37, GPIO.OUT)    #red
GPIO.setup(35, GPIO.OUT)    #green
GPIO.setup(33, GPIO.OUT)    #blue

GPIO.output(37, 0)
GPIO.output(35, 1)
GPIO.output(33, 0)

pygame.mixer.pre_init(48000, -16, 12, 512)
pygame.init()

#sound1.set_volume(1)

sound1 = pygame.mixer.Sound('spanishtag/subkick.wav')
sound1.set_volume(.85)
sound2 = pygame.mixer.Sound('spanishtag/descentrise.wav')
sound2.set_volume(.65)
sound3 = pygame.mixer.Sound('spanishtag/snareroom.ogg')
sound3.set_volume(.65)
sound4 = pygame.mixer.Sound('spanishtag/flamenco2.wav')
sound4.set_volume(.65)
sound5 = pygame.mixer.Sound('spanishtag/guitarancientbackwards.ogg')
sound5.set_volume(.65)
sound6 = pygame.mixer.Sound('spanishtag/brushes.wav')
sound6.set_volume(.65)
sound7 = pygame.mixer.Sound('spanishtag/paddawn2.wav')
sound7.set_volume(.65)
sound8 = pygame.mixer.Sound('spanishtag/paddawn.wav')
sound8.set_volume(.65)
sound9 = pygame.mixer.Sound('spanishtag/hooverbass1.wav')
sound9.set_volume(.65)
sound10 = pygame.mixer.Sound('spanishtag/spanishtag2.wav')
sound10.set_volume(.65)
sound11 = pygame.mixer.Sound('spanishtag/spanishtag1.wav')
sound11.set_volume(.65)
sound12 = pygame.mixer.Sound('spanishtag/spanishtag3.wav')
sound12.set_volume(.65)
sound13 = pygame.mixer.Sound('spanishtag/hooverbass2.wav')
sound13.set_volume(.65)
sound14 = pygame.mixer.Sound('spanishtag/clapbig.ogg')
sound14.set_volume(.65)
sound15 = pygame.mixer.Sound('spanishtag/hisubkick.wav')
sound15.set_volume(.65)
sound16 = pygame.mixer.Sound('spanishtag/flamenco1.wav')
sound16.set_volume(.65)

x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y = [0,0,0]

t = 0
try:
    while(True):
        if GPIO.event_detected(29) & (x[0] == 0):
            sound1.stop()
            pygame.mixer.find_channel()
            sound1.play()
            x[0] = 1
        elif (GPIO.input(29) == 0) & (x[0] == 1):
            #sound1.stop()
            x[0] = 0
        if GPIO.event_detected(31) & (x[1] == 0):
            sound2.stop()
            pygame.mixer.find_channel()
            sound2.play()
            x[1] = 1
        elif (GPIO.input(31) == 0):
            time.sleep(0.01)
            #sound2.stop()
            x[1] = 0
        if GPIO.event_detected(7) & (x[2] == 0):
            sound3.stop()
            pygame.mixer.find_channel()
            sound3.play()
            x[2] = 1
        elif (GPIO.input(7) == 0):
            time.sleep(0.01)
            #sound3.stop()
            x[2] = 0
	if GPIO.event_detected(8) & (x[3] == 0):
            sound4.stop()
            pygame.mixer.find_channel()
            sound4.play()
            x[3] = 1
        elif (GPIO.input(8) == 0):
            time.sleep(0.01)
            #sound4.stop()
            x[3] = 0
	if GPIO.event_detected(10) & (x[4] == 0):
            sound5.stop()
            pygame.mixer.find_channel()
            sound5.play()
            x[4] = 1
        elif (GPIO.input(10) == 0):
            time.sleep(0.01)
            #sound5.stop()
            x[4] = 0
	if GPIO.event_detected(11) & (x[5] == 0):
            sound6.stop()
            pygame.mixer.find_channel()
            sound6.play()
            x[5] = 1
        elif (GPIO.input(11) == 0):
            time.sleep(0.01)
            #sound6.stop()
            x[5] =  0
	if GPIO.event_detected(12) & (x[6] == 0):
            sound7.stop()
            pygame.mixer.find_channel()
            sound7.play()
            x[6] = 1
        elif (GPIO.input(12) == 0):
            time.sleep(0.01)
            #sound7.stop()
            x[6] = 0
	if GPIO.event_detected(13) & (x[7] == 0):
            sound8.stop()
            pygame.mixer.find_channel()
            sound8.play()
            x[7] = 1
        elif (GPIO.input(13) == 0):
            time.sleep(0.01)
            #sound8.stop()
            x[7] = 0
	if GPIO.event_detected(15) & (x[8] == 0):
            sound9.stop()
            pygame.mixer.find_channel()
            sound9.play()
            x[8] = 1
        elif (GPIO.input(15) == 0):
            time.sleep(0.01)
            sound9.stop()
            x[8] = 0
	if GPIO.event_detected(16) & (x[9] == 0):
            sound10.stop()
            pygame.mixer.find_channel()
            sound10.play()
            x[9] = 1
        elif (GPIO.input(16) == 0):
            time.sleep(0.01)
            #sound10.stop()
            x[9] = 0
	if GPIO.event_detected(18) & (x[10] == 0):
            sound11.stop()
            pygame.mixer.find_channel()
            sound11.play()
            x[10] = 1
        elif (GPIO.input(18) == 0):
            time.sleep(0.01)
            #sound11.stop()
            x[10] = 0
	if GPIO.event_detected(19) & (x[11] == 0):
            sound12.stop()
            pygame.mixer.find_channel()
            sound12.play()
            x[11] = 1
        elif (GPIO.input(19) == 0):
            time.sleep(0.01)
            #sound12.stop()
            x[11] = 0
	if GPIO.event_detected(21) & (x[12] == 0):
            sound13.stop()
            pygame.mixer.find_channel()
            sound13.play()
            x[12] = 1
        elif (GPIO.input(21) == 0):
            time.sleep(0.01)
            sound13.stop()
            x[12] = 0
	if GPIO.event_detected(22) & (x[13] == 0):
            sound14.stop()
            pygame.mixer.find_channel()
            sound14.play()
            x[13] = 1
        elif (GPIO.input(22) == 0):
            time.sleep(0.01)
            #sound14.stop()
            x[13] = 0
	if GPIO.event_detected(23) & (x[14] == 0):
            sound15.stop()
            pygame.mixer.find_channel()
            sound15.play()
            x[14] = 1
        elif (GPIO.input(23) == 0):
            time.sleep(0.01)
            #sound15.stop()
            x[14] = 0
	if GPIO.event_detected(24) & (x[15] == 0):
            sound16.stop()
            pygame.mixer.find_channel()
            sound16.play()
            x[15] = 1
        elif (GPIO.input(24) == 0):
            time.sleep(0.01)
            #sound16.stop()
            x[15] = 0
#-------------------------------------------------------------------------
        if (GPIO.input(40) == 1):
            print (t)
            time.sleep(1)
            t += 1
            if (t == 10):
                GPIO.output(37, 1)
                GPIO.output(35, 1)
                GPIO.output(33, 0)
                time.sleep(0.2)
                GPIO.output(37, 0)
                GPIO.output(35, 0)
                time.sleep(0.2)
                GPIO.output(37, 1)
                GPIO.output(35, 1)
                time.sleep(0.2)
                GPIO.output(37, 0)
                GPIO.output(35, 0)
                time.sleep(0.2)
                GPIO.output(37, 1)
                GPIO.output(35, 1)
                time.sleep(0.2)
                GPIO.output(37, 0)
                GPIO.output(35, 0)
                time.sleep(0.2)
                GPIO.output(37, 1)
                GPIO.output(35, 1)
                time.sleep(0.2)
                GPIO.output(37, 0)
                GPIO.output(35, 0)
                time.sleep(0.2)
                GPIO.output(37, 1)
                GPIO.output(35, 1)
                os.system("sudo reboot -h now")
                t = 0
        elif (GPIO.input(40) == 0) & (t > 0):
            if (t > 2):
                GPIO.output(37, 1)
                GPIO.output(35, 0)
                GPIO.output(33, 0)
                time.sleep(0.2)
                GPIO.output(37, 0)
                time.sleep(0.2)
                GPIO.output(37, 1)
                time.sleep(0.2)
                GPIO.output(37, 0)
                time.sleep(0.2)
                GPIO.output(37, 1)
                time.sleep(0.2)
                GPIO.output(37, 0)
                time.sleep(0.2)
                GPIO.output(37, 1)
                time.sleep(0.2)
                GPIO.output(37, 0)
                time.sleep(0.2)
                GPIO.output(37, 1)
                os.system("sudo shutdown -h now")
            t = 0
#-------------------------------------------------------------------------        
#    if (GPIO.input(40) == 1) & (y[0] == 0):
 #       sound1 = pygame.mixer.Sound('Drumpad/bloom.wav')
  #      sound2 = pygame.mixer.Sound('Drumpad/vocal.wav')
   #     sound3 = pygame.mixer.Sound('Drumpad/skank1.wav')
    #    y[0] = 1
     #   y[1] = 0
      #  y[2] = 0

except KeyboardInterrupt:
        GPIO.cleanup()
