from datetime import datetime, timedelta


class SimulationClock:
    def __init__(self,
                 epoch: datetime,
                 ):
        self.epoch = epoch
        self.t = 0.0

    def step(self, dt):
        self.t += dt

    def datetime(self):
        return self.epoch + timedelta(seconds=self.t)
