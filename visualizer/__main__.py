from logging import getLogger

import pygame

from .init_logging import init_logging

init_logging()
logger = getLogger()
logger.info('Visualizer starts')
modules_passed, modules_failed = pygame.init()
logger.debug(f'pygame initialized with {modules_failed} modules initialization passed and {modules_failed} failed')
