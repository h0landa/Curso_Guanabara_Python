#Programa em python que abra e reproduza arquivo MP3

from playsound import playsound

music = input("Digite o nome da musica: ")

playsound("{}".format(music))
