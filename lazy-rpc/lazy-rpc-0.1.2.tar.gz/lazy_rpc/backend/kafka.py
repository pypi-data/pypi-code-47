from lazy_rpc.backend.base import Sender, Receiver
from lazy_rpc.utils import pack, unpack, build_uniq_name
from lazy_rpc.decolators import FUNCTIONS

from kafka import KafkaConsumer, KafkaProducer
from multiprocessing import Process

class Kafka(Sender, Receiver):

  def __init__(self, servers=[]):
    self.servers = servers

  def setup_sender(self):
    self.producer = KafkaProducer(bootstrap_servers=self.servers)

  def setup_receiver(self):
    self.consumers = []

  def send(self, fn, *args, **kwargs):
    uniq_name = build_uniq_name(fn)
    value = pack(fn, *args, **kwargs)
    future = self.producer.send(uniq_name, value)
    result = future.get(timeout=60)

  def receive(self):
    plist = []
    for topic in FUNCTIONS.keys():
      fn = self.__build_process_fn(topic)
      p = Process(target=fn)
      plist.append(p)
      p.start()

    for p in plist:
      p.join()


  def __build_process_fn(self, topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=self.servers)
    func = FUNCTIONS[topic]
    self.consumers.append(consumer)
    def __fn():
      for msg in consumer:
        Process(target=__unpack, args=[msg.value]).start()

    def __unpack(msg):
      value = unpack(msg)
      args = value['args']
      kwargs = value['kwargs']
      func(*args, **kwargs)

    return __fn


