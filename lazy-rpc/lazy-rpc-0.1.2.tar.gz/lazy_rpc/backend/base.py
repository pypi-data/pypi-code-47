from abc import abstractmethod

class Sender:

  @abstractmethod
  def setup_sender(self):
    pass

  @abstractmethod
  def send(self):
    pass

class Receiver:

  @abstractmethod
  def setup_receiver(self):
    pass

  @abstractmethod
  def receive(self):
    pass

