'''
banana_player is a simple python script that works with a USB button 
that send the command 'h' followed by Return to play a song 
it is loaded in the profile/etc file on a raspberry pi that boots to CLI
'''
import pygame 
from datetime import datetime #for data-logging 

def play_rap(): # loads the music player
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/banana-final-clean.ogg") #link to the song
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True: # stops the program doing anything else while the music is playing
        continue

def log_play():
	now = datetime.now().strftime('%Y/%m/%d %H:%M:%S') #generates timestamp
	tracking_file = open('RoyalSocietyTrackingData.txt', 'a')
	tracking_file.write(now + '\n')

def main():
    print("Welcome to the Banana Player.\nTo play the song, please press 'h' followed by Enter. To continute loading up the raspberry pi, please press any other key")
    while True:
        spam = input(">")
        if spam == 'h':
        	log_play()
        	print('playing song and logging timestamp')        	
            play_rap()
            print('song done playing')
        spam = None

    else:
    	exit()

if __name__ == '__main__':
	main()
    
