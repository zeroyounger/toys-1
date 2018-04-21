import pygame as py
py.init()
while True:
	for event in py.event.get():
	    if event.type== py.QUIT:
	        sys.exit()
	    elif event.type==py.KEYDOWN:
	        if event.key==py.K_ESCAPE:
	            print "exit"
	            sys.exit()
	            py.quit()
	        elif event.key==py.K_UP:
	            print "up"
	        elif event.key==py.K_LEFT:
	            print "left"
	        elif event.key==py.K_DOWN:
	            print "down"
	        elif event.key==py.K_RIGHT:
	            print "right"