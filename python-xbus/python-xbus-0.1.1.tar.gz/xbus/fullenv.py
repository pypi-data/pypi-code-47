# utilities to setup a full testing environment.

import asyncio
import os.path
import sys
from asyncio import subprocess

import yaml

import xbus.client


class Error(RuntimeError):
    pass


class FullenvRunContext:
    def __init__(self, env):
        self.env = env

    async def __aenter__(self):
        await self.env.startup()

    async def __aexit__(self, exc_type, exc, tb):
        await self.env.shutdown()


class Fullenv:
    def __init__(self, config, loop=None):
        self.config = config
        self.process = None
        self.loop = None

    async def _read_stderr(self):
        while True:
            line = await self.process.stderr.readline()
            if not line:
                return
            sys.stderr.buffer.write(line)

    async def _next_output(self):
        while True:
            line = await self.process.stdout.readline()
            if not line:
                raise Error("Unexpected EOF")
            line = line.decode("utf-8").strip("\n")
            if not line.startswith("< "):
                continue
            if line.startswith("< OK: "):
                return line[6:]
            if line == "< OK":
                return None
            if line.startswith("< ERR: "):
                raise Error(line[7:])
            raise Error("Unexpected reply: %s" % line)

    async def _run_command(self, *args):
        cmd = " ".join(args) + "\n"
        self.process.stdin.write(cmd.encode("utf-8"))
        await self.process.stdin.drain()
        return await self._next_output()

    async def init(self):
        self.process = await asyncio.create_subprocess_exec(
            "xbus-fullenv",
            "run",
            "--no-prompt",
            self.config,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        _ = asyncio.ensure_future(self._read_stderr())
        self.workdir = await self._next_output()

    async def close(self):
        try:
            await self._run_command("quit")
        except Exception:
            pass
        await self.process.wait()
        self.process = None

    async def __aenter__(self):
        await self.init()

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def startup(self):
        await self._run_command("startup")

    async def shutdown(self):
        await self._run_command("shutdown")

    def up(self):
        return FullenvRunContext(self)

    async def client_config(self, clientname):
        return await self._run_command("client-config", clientname)

    def ctl_config(self):
        return os.path.join(self.workdir, "xbusctl", "xbusctl.yaml")

    async def wd(self):
        return await self._run_command("wd")

    async def load_client(self, clientname):
        filename = await self.client_config(clientname)
        confdict = yaml.load(open(filename, "rb"))
        return xbus.client.Client(
            confdict, os.path.dirname(filename), self.loop
        )

    async def ctl(self, *cmd):
        p = await asyncio.create_subprocess_exec(
            "xbusctl",
            "--config",
            self.ctl_config(),
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await p.communicate()
        if len(stderr) != 0:
            raise RuntimeError(str(stderr))

        return stdout
