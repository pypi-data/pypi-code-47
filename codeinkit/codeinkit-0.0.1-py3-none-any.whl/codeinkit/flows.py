
class Flows():
  __flows = {}

  def register(self, flowName, actions):
    self.__flows[flowName] = actions

  def execute(self, flowName, initData):
    flow = self.__flows.get(flowName)
    data = initData.copy();

    for action in flow:
      data = action(data.copy());
