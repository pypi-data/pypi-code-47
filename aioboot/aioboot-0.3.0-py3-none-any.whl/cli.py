from dataclasses import dataclass, field
from typing import Callable, List, Optional


@dataclass
class Command:
    cmd: Callable
    name: Optional[str] = None
    lifespan: bool = True


@dataclass
class CommandGroup:
    name: str
    commands: List = field(default_factory=list)

    def add_command(
        self, cmd: Callable, *, name: Optional[str] = None, lifespan: bool = True
    ):
        self.commands.append(Command(cmd=cmd, name=name, lifespan=lifespan))

    def command(self, name: Optional[str] = None, *, lifespan: bool = True) -> Callable:
        def decorator(cmd: Callable) -> Callable:
            self.add_command(cmd=cmd, name=name, lifespan=lifespan)
            return cmd

        return decorator
