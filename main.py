import pygame 

#pygame initialization
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

gameOver = False

while not gameOver:

	screen.fill("white")
	pygame.draw.circle(screen, "red", (0,0), 40)

	#required parameters
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver = True
	
	#rendering
	pygame.display.flip();
	clock.tick(60)

pygame.quit()

# TODO
# -Study underlying structure 
# -Make a UI, Game engine, Physics engine, Renderer 