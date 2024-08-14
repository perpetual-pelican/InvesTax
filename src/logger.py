import logging
import sys

log = logging.getLogger()
log.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
log.addHandler(console_handler)
