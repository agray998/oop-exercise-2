from clock import Clock

def test_clock_ticks():
  clock1 = Clock(0, 0, 0)
  assert str(clock1) == "00:00:00"
  clock1.tick()
  assert str(clock1) == "00:00:01"
  clock1.tick()
  assert str(clock1) == "00:00:02"

def test_wrapping_seconds():
  clock1 = Clock(0, 0, 59)
  clock1.tick()
  assert str(clock1) == "00:01:00"
  clock1 = Clock(0, 10, 59)
  clock1.tick()
  assert str(clock1) == "00:11:00"

def test_wrapping_minutes():
  clock1 = Clock(0, 59, 0)
  for _ in range(60):
    clock1.tick()
  assert str(clock1) == "01:00:00"
  clock1 = Clock(12, 59, 0)
  for _ in range(60):
    clock1.tick()
  assert str(clock1) == "13:00:00"
