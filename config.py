import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'YEWLFkHYu%k4WkQoUKzi*ouhp45CgBmH'
