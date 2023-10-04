import pygame 

#pygame initialization
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

gameOver = False

while not gameOver:

	pygame.draw.circle(center=(0,0))

	#required parameters
	screen.fill("white")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver = True
	
	#rendering
	pygame.display.flip();
	clock.tick(60)

pygame.quit()