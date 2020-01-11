import logging
from typing import Any, Callable, List, Optional, Type, TypeVar, Union

from discord import Guild, Member, Message, User
from discord.ext import commands
from discord.ext.commands import (
    BadArgument,
    CommandError,
    CommandInvokeError,
    CommandNotFound,
    ExtensionAlreadyLoaded,
    MissingRequiredArgument,
    NotOwner,
    UnexpectedQuoteError,
)
from environs import Env

from .abc import AbstractCog, IAlias, IPerm, IUseCase
from .exceptions import NoPerm

core_logger = logging.getLogger("snek.bot")
logger = logging.getLogger("snek.bot.log")

TCog = TypeVar("TCog", bound=AbstractCog, covariant=True)


class SNEKContext(commands.Context):
    bot: "SNEK"

    def __repr__(self) -> str:
        return f"<SNEKContext message.content={self.message.content!r} message={self.message!r}>"

    async def check_perm(self, perm: str) -> Optional[bool]:
        return await self.bot.check_perm(perm, self.guild, self.author)

    async def mod(self) -> bool:
        if not self.guild:
            return False

        if await self.bot.is_owner(self.author):
            return True

        p_cog: IPerm = self.bot.find_typed_cog(IPerm)
        if p_cog is None:
            return False

        mod = p_cog.get_pgroup("mod")
        if mod is None:
            return False

        roles = {self.guild.get_role(role) for role in mod.roles}

        has_role = len(roles.intersection(set(self.author.roles))) > 0
        is_g_owner = self.guild.owner == self.author

        return has_role or is_g_owner

    async def send(
        self,
        content: Union[List[str], str] = None,
        *,
        no_code: bool = False,
        lang: Optional[str] = None,
        **kwargs: Any,
    ) -> Message:
        return await super(SNEKContext, self).send(
            content=SNEK.send_wrapper(content=content, no_code=no_code, lang=lang),
            **kwargs,
        )

    async def get_user(self, uid: Union[str, int]) -> Optional[User]:
        user = self.guild.get_member(uid)

        if user is None:
            user = self.bot.get_user(uid)

        if user is None:
            user = await self.bot.fetch_user(uid)

        return user


class SNEK(commands.Bot):
    def __init__(
        self,
        command_prefix: str = "!",
        ignore_unknown_commands: bool = False,
        debug: bool = False,
        initial_extensions: Optional[List[str]] = None,
        **kwargs: Any,
    ):
        super().__init__(command_prefix, **kwargs)

        self.debug = debug
        self.ignore_unknown_commands = ignore_unknown_commands
        self.initial_extensions = initial_extensions or []
        self.env = Env()
        self.env.read_env()

        if debug or self.env.bool("_DEBUG", False):
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

    async def start(self, *args: Any, **kwargs: Any) -> None:
        self.load_initial_extensions()

        try:
            self.load_extension("snek.cogs.database")
        except ExtensionAlreadyLoaded as e:
            core_logger.warning(
                "SNEK Database cog already loaded (please do not load this cog manually)",
                exc_info=e,
            )

        from snek.cogs.database import DataBaseCog

        c: DataBaseCog = self.find_typed_cog(DataBaseCog)
        await c.map_db()

        self.dispatch("database_init")

        return await super().start(*args, **kwargs)

    def load_initial_extensions(self) -> None:
        for m in self.initial_extensions:
            try:
                self.load_extension(m)
                logger.debug(f"Loaded extension {m!r}")
            except Exception as e:
                logger.warning(f"Failed to load extension extension {m!r}:", exc_info=e)

    async def login(self, token: Optional[str] = None, *, bot: bool = True) -> None:

        if token is None:
            token = self.env.str("DISCORD_TOKEN", None)
            if token is None:
                logger.critical(
                    "No token supplied, and no DISCORD_TOKEN in environment variables."
                )
                import sys

                sys.exit(1)
            else:
                logger.debug("Using DISCORD_TOKEN from env.")

        return await super().login(token, bot=bot)

    async def log(
        self,
        *args: str,
        no_code: bool = False,
        _for: str = "LOG",
        _server: Optional[int] = None,
        _level: int = logging.INFO,
    ) -> None:
        mess = f"[{_for}] {' '.join(str(a) for a in args)}"

        logger.log(level=_level, msg=mess)

        if self.usecase:
            log_channel = self.usecase.log_channel(_server)

            if log_channel is not None:
                await log_channel.send(self.send_wrapper(mess, no_code=no_code))

    async def check_perm(
        self, perm: str, guild: Guild, member: Member
    ) -> Optional[bool]:
        p_cog: IPerm = self.find_typed_cog(IPerm)

        return (
            await p_cog.check_perm(perm, guild, member) if p_cog is not None else None
        )

    async def try_get_alias(self, name: str) -> Optional[str]:
        alias: IAlias = self.find_typed_cog(IAlias)

        return alias and alias.get(name)

    async def owner(self) -> Optional[User]:
        if self.owner_id is None:
            ai = await self.application_info()
            self.owner_id: int = ai.owner.id
            return ai.owner

        return await self.fetch_user(self.owner_id)

    def find_typed_cog(self, cog_type: Type[AbstractCog]) -> Optional[TCog]:
        try:
            return next(cog for cog in self.cogs.values() if isinstance(cog, cog_type))
        except StopIteration:
            return None

    @property
    def usecase(self) -> Optional[IUseCase]:
        return self.find_typed_cog(IUseCase)

    async def invoke(self, ctx: SNEKContext) -> None:
        if ctx.command is not None:
            self.dispatch("command", ctx)
            try:
                if await self.can_run(ctx, call_once=True):
                    await ctx.command.invoke(ctx)
            except Exception as exc:
                await ctx.command.dispatch_error(ctx, exc)
            else:
                self.dispatch("command_completion", ctx)

        elif ctx.invoked_with:
            alias = await self.try_get_alias(ctx.invoked_with)
            if alias:
                await ctx.send(alias, no_code=True)
                await self.log(
                    f'{ctx.author} issues alias "{ctx.invoked_with}" in #{ctx.channel}',
                    _for="CMD",
                )
                return

            if not self.ignore_unknown_commands:
                self.dispatch(
                    "command_error",
                    ctx,
                    commands.errors.CommandNotFound(
                        f"Command {ctx.invoked_with!r} is not found"
                    ),
                )
            else:
                logging.debug(f"Ignored unknown command {ctx.invoked_with!r}")

    @staticmethod
    def send_wrapper(
        content: Union[List[str], str] = None, no_code: bool = False, lang: str = None
    ) -> str:
        c = ""
        if content:
            if isinstance(content, list):
                content = " ".join(content)

            c = str(content)
            if not no_code and content:
                if "\n" in c:
                    c = f"```{lang or ''}\n{c}\n```"
                else:
                    c = f"`{c}`"
        return c

    @staticmethod
    def is_mod() -> Callable[[SNEKContext], bool]:
        async def is_mod_checker(ctx: SNEKContext) -> bool:
            if await ctx.mod():
                return True
            else:
                raise NoPerm("Not authorized")

        return commands.check(is_mod_checker)

    async def report_traceback(
        self, e: Exception, ctx: Optional[SNEKContext] = None
    ) -> None:
        import traceback as tb

        traceback: str = "\n".join(
            a for a in tb.format_list(tb.extract_tb(e.__traceback__))
        )
        owner = await self.owner()

        await owner.send(f"`[EXCEPTION] ctx: {ctx or '(no context)'}`")
        await owner.send(f"```\n{type(e)!r}: {e!s}\n{traceback}\n```")

    async def on_command_error(self, ctx: SNEKContext, error: Exception) -> None:
        if not isinstance(error, CommandError):
            await ctx.send("Whoops, something went wrong!")
            await self.report_traceback(error, ctx)

        elif isinstance(error, CommandInvokeError):
            await ctx.send("An error occurred when processing the command.")
            await self.report_traceback(error.original, ctx)
        elif isinstance(error, CommandNotFound):
            await ctx.send(list(error.args))
        elif isinstance(error, NoPerm):
            await ctx.send("You are not allowed to use that command.")
        elif isinstance(error, BadArgument):
            await ctx.send(["Bad argument:", *error.args])
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(["Malformed command:", *error.args])
        elif isinstance(error, UnexpectedQuoteError):
            await ctx.send(["Unexpected quote:", *error.args])
        elif isinstance(error, NotOwner):
            await ctx.send(["Cannot run command:", *error.args])
        else:
            await ctx.send("An error occurred when processing the command.")
            await self.report_traceback(error, ctx)

    async def on_command_completion(self, ctx: SNEKContext) -> None:
        await self.log(
            f"{ctx.author} issued command '{ctx.message.content}' in #{ctx.channel}",
            _for="CMD",
        )

    async def on_ready(self) -> None:
        core_logger.info(f"Logged in as;\n@{self.user!s}\n#{self.user.id}")

        await self.log("Ready.", _for="BOOT")

    async def get_context(
        self, message: Message, *, cls: Type[Any] = None
    ) -> SNEKContext:
        return await super(SNEK, self).get_context(message, cls=SNEKContext)
