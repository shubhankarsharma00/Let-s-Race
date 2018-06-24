import pygame
import time
import random
def make_objects(thing_startx,thing_starty,thing_height,level):
	thingcount=random.randint(1,level)
	if thingcount>6:
		thingcount=5
	else:
		pass
	a=[]
	thing_starty_backup=thing_starty
	for z in range(thingcount):
		if d_height-thing_starty-thing_height>100:
			new_thingy=50*int(random.randint(100,(d_height-thing_starty-thing_height))/50)
			a.append(new_thingy)
			thing_starty+=new_thingy
		if thing_starty_backup>100:
			new_thingy=50*int((random.randint(100,thing_starty))/50)
			a.append(new_thingy)
			thing_starty=new_thingy
	return a

def show_pause():
	global d_width
	font =pygame.font.SysFont(None,25)
	text=font.render("Pause",True,black)
	gdisplay.blit(text,(d_width-80,0))
def pause_game():
	global Pause
	Pause=True
	game_intro()
def level_show(x,level):
	font =pygame.font.SysFont(None,25)
	text=font.render("level "+str(level),True,black)
	gdisplay.blit(text,(x,0))

def score():
	global count
	font =pygame.font.SysFont(None,25)
	text=font.render("Score "+str(count),True,black)
	gdisplay.blit(text,(0,0))
def things(thingx,thingy,thingw,thingh,color):
	# pygame.draw.rect(gdisplay,color,[thingx,thingy,thingw,thingh])
	gdisplay.blit(img1,(thingx,thingy))
def car(x,y):
	gdisplay.blit(img,(x,y))


def game_intro():
	global Pause
	global Crash
	global count
	# print Pause,Crash,count
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			# print event
		gdisplay.fill(black)
		gdisplay.blit(bgimg,(0,0))

		if Pause==True:
			largeText=pygame.font.SysFont('freesansbold.ttf',85)
			surf,rect=text_objects("Score: "+str(count),largeText)
			rect.center = ((d_width/2),(d_height*0.5))
			gdisplay.blit(surf,rect)

		smallText=pygame.font.SysFont('freesansbold.ttf',18)
		textsurf,textrect=text_objects("Let's Race",smallText)
		textrect.center = (200,475)

		textsurf2,textrect2=text_objects("Quit",smallText)
		textrect2.center = (600,475)


		largeText=pygame.font.SysFont('freesansbold.ttf',85)
		TextSurf,TextRect=text_objects("Let's Race",largeText)
		TextRect.center = ((d_width/2),(d_height*0.2))
		gdisplay.blit(TextSurf,TextRect)

		mouse=pygame.mouse.get_pos()
		click=pygame.mouse.get_pressed()
		# print click
		if 150+100> mouse[0] > 150 and 450 + 50 > mouse[1] >450:
			pygame.draw.rect(gdisplay,green,(150,450,100,50))
			if click[0]==1:
				Pause=False
				game_loop()
		else:
			pygame.draw.rect(gdisplay,b_green,(150,450,100,50))	
		if 550+100> mouse[0] > 550 and 450 + 50 > mouse[1] >450:
			pygame.draw.rect(gdisplay,red,(550,450,100,50))
			if click[0]==1:
				pygame.quit()
				quit()
		else:
			pygame.draw.rect(gdisplay,b_red,(550,450,100,50))

		gdisplay.blit(textsurf,textrect)
		gdisplay.blit(textsurf2,textrect2)
		pygame.display.update()
		clock.tick(15)



def game_loop():
	global Crash
	global Pause
	global count
	if Crash==True:
		count=0
		Crash=False
	pygame.mixer.music.play(-1)
	x=(d_width*0.1)
	y=(d_height*0.40)
	y_change=0
	car_height=78
	car_width =228
	thing_startx=800
	thing_starty=50*(random.randrange(0,d_height)/50)
	thing_speed = 7
	thing_width = 100
	thing_height = 90
	level=1
	a=make_objects(thing_startx,thing_starty,thing_height,level)
	crashed=False

	while not crashed:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_change+=-5
				elif event.key == pygame.K_DOWN:
					y_change+=5
			if event.type==pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change=0
		y+=y_change
		mouse2=pygame.mouse.get_pos()
		click2=pygame.mouse.get_pressed()
		# print  d_width-100,mouse2[0],d_width,click2[0]

		if d_width-100<mouse2[0]<d_width and 20>mouse2[1]>0:
			# print "ok"
			if click2[0]==1:
				# print "yeah"
				pause_game()
		gdisplay.fill(white)
		gdisplay.blit(bgimg,(0,0))




		for n in range(len(a)):
			things(thing_startx,a[n],thing_width,thing_height,red)
		thing_startx-=thing_speed	
		score()
		level_show(x,level)
		show_pause()
		car(x,y)

		if y>d_height-car_height or y<0:
			crash()

		for n in range(len(a)):
			if thing_startx<0:
				thing_startx= d_width - thing_width
				a=make_objects(thing_startx,a[n],thing_height,level)
				count+=1
				if count%10==0:
					level+=1
					thing_speed+=1
				# print a
				break
				# thing_speed+=1
				# thing_height+=10
				# thing_width+=10
			else:
				# print a,n
				if a[n]+thing_height>y and a[n]+thing_height<y+car_height and thing_startx<x+car_width:
					# print thing_startx,a[n],y,y+car_height
					crash()
					break

				if a[n]<y+car_height and a[n]+thing_height>y+car_height and thing_startx<x+car_width:
					# print thing_startx,a[n],y,y+car_height
					crash()
					break

				if a[n]<y+car_height and a[n]+thing_height>y+car_height and thing_startx<x+car_width:
					# print thing_startx,a[n],y,y+car_height
					crash()
					break


		pygame.display.update()
		clock.tick(60)


def text_objects(text,font):
	textSurface=font.render(text,True,white)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText=pygame.font.SysFont('freesansbold.ttf',85)
	TextSurf,TextRect=text_objects(text,largeText)
	TextRect.center = ((d_width/2),(d_height*0.2))
	gdisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(2)

def crash():
	global Crash
	global count
	global Pause
	Pause=True
	Crash=True
	# print Pause,count
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)
	message_display("you are dead!!")
	game_intro()
	pygame.display.update()

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("jazz.wav")

d_width=800
d_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
b_red=(200,0,0)
b_green=(0,200,0)
count=0
gdisplay=pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption("Let's Race")
clock = pygame.time.Clock()

img=pygame.image.load('img.png')
img1=pygame.image.load('img1.png')
bgimg=pygame.image.load('bgimg.png')

pygame.display.set_icon(img)

Pause=False
Crash=False
game_intro()
# game_loop()
pygame.quit()
quit()
