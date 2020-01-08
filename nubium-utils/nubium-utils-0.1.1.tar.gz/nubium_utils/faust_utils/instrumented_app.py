import faust


class InstrumentedApp(faust.App):
    """
    Faust app with metric of number of agent exceptions
    """

    async def _on_agent_error(self, agent: faust.agents.AgentT, exc: BaseException) -> None:
        self.wrapper.agent_exception(exc)
        await super(InstrumentedApp, self)._on_agent_error(agent, exc)
