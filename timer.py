import time, os, sys


class Timer:
     def __init__(self) -> None:
          self.h = 0
          self.m = 0
          self.s = 0

          sys.stdout.write("\033[?25l")
          sys.stdout.flush()

     def __str__(self) -> str:
          hours = str(self.h).zfill(2)
          minutes = str(self.m).zfill(2)
          seconds = str(self.s).zfill(2)
          width = os.get_terminal_size().columns
          heigth = os.get_terminal_size().lines//2
          x = '\n'*heigth
          result_string = x + f"{hours}:{minutes}:{seconds}".center(width, ' ')
          return result_string

     def update_time(self) -> None:
          os.system("clear")
          print(self)
          self.s += 1
          if self.s == 60:
               self.s = 0
               self.m += 1
          if self.m == 60:
               self.m = 0
               self.h += 1
          time.sleep(0.5)


     def run(self):
          while True:
               self.update_time()
