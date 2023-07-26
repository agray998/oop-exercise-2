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
    ...

  def tick(self):
    ...

  def __str__(self):
    ...

class TwelveHourClock(Clock):
  ...

