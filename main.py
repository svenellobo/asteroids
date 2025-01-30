import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():  
  pygame.init
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Shot.containers = (shots, updatable, drawable)
  
  
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()

  
  Player.containers = (updatable, drawable)
  player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


  
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    updatable.update(dt)
    for object in asteroids:
      if object.collision(player) == True:
        print("Game over!")
        sys.exit()
      
    screen.fill(color="black")

    for object in drawable:
      object.draw(screen)
    
    for ast in asteroids:
      for bullet in shots:
        if ast.collision(bullet) == True:
          ast.split()
          bullet.kill()

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000     
  


if __name__ == "__main__":
  main()