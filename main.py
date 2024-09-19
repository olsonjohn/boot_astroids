#!/usr/bin/env python

import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    player = Player(x, y)
    asteroid_field = AsteroidField()
    updatable.add(player)
    updatable.add(asteroid_field)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        
        pygame.display.flip()
        for item in asteroids:
            if player.collides_with(item):
                print("Game Over")
                return
            
        for bullet in shots:
            for asteroid in asteroids:
                if bullet.collides_with(asteroid):
                    asteroid.split()
                    bullet.kill()
                    break


        time_called = clock_object.tick(60)
        dt = time_called / 1000


if __name__ == "__main__":
    main()
