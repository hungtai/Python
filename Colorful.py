#!/usr/bin/python3
class color:
   PURPLE = '\033[95m'
   DARKPURPLE = '\033[35m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   DARKBLUE = '\033[34m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   BWYB = '\033[30;43m'
   END = '\033[0m'

print color.BOLD + 'Hello World !' + color.END
