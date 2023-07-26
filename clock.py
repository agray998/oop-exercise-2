'''
Task: create a clock class. Each clock should have the attributes hours, minutes and seconds.
The class should have methods to:
 - initialise these attributes upon instance creation
 - update the clock's time by one second when called (remembering to wrap appropriately after every 60 seconds)
 - return a string representation of the current clock time
 Create a subclas of this class for 12-hour clocks, and override the methods appropriately
'''
class Clock():
  def __init__(self, hours = 0, minutes = 0, seconds = 0):
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds

  def tick(self):
    self.seconds += 1
    if self.seconds > 60:
     self.minutes += 1
    if self.minutes > 60:
     self.hours += 1
    self.seconds %= 60
    self.minutes %= 60
    self.hours %= 24

  def __str__(self):
    return f"{'0' if self.hours < 10 else ''}{self.hours}:{'0' if self.minutes < 10 else ''}{self.minutes}:{'0' if self.seconds < 10 else ''}{self.seconds}"

class TwelveHourClock(Clock):
  ...

if __name__ == '__main__':
  clock = Clock(0, 0, 0)
  while True:
    clock.tick()
    print(clock)
    sleep(1000)
