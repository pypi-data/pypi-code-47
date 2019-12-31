import glob
import inspect
import hashlib
import importlib
from importlib.machinery import SourceFileLoader
from os.path import dirname, basename, isfile, join

MIGRATION_TABLE = "_gs_migrations"


class Migration:
    def __init__(self, number, commands):
        self.number = number
        self.commands = commands

    def get_hash(self):
        hash_ = hashlib.sha3_256()
        for c in self.commands:
            if isinstance(c, str):
                hash_.update(c.encode('utf-8'))
            elif callable(c):
                hash_.update(inspect.getsource(c).encode('utf-8'))
            else:
                raise Exception(
                    "Migration command must be a string or callable."
                )
        return hash_.hexdigest()

    async def already_run(self, pg, migration_table):
        hash_digest = self.get_hash()
        row = await pg.fetchrow(
            f"SELECT * FROM {migration_table} WHERE id = $1",
            self.number,
        )
        if not row:
            return False
        elif row["hash"] != hash_digest:
            raise Exception(
                f"Migration hash mismatch. "
                f"Table contains {row['hash']} but migration is {hash_digest}"
            )
        return True

    async def run(self, pg, migration_table):
        if await self.already_run(pg, migration_table):
            return
        async with pg.transaction():
            for c in self.commands:
                if isinstance(c, str):
                    await pg.execute(c)
                elif callable(c):
                    await c(pg)
                else:
                    raise Exception(
                        "Migration command must be a string or callable"
                    )
            await pg.execute(
                f"INSERT INTO {migration_table} (id, hash) VALUES ($1, $2)",
                self.number,
                self.get_hash(),
            )


async def create_migration_table(pg, name):
    await pg.execute(f"""
        CREATE TABLE {name} (
            id INT NOT NULL PRIMARY KEY,
            hash TEXT NOT NULL,
            run_at TIME NOT NULL DEFAULT NOW()
        )    
    """)


async def does_migration_table_exist(pg, name):
    row = await pg.fetchrow("SELECT to_regclass($1)", name)
    return row["to_regclass"] == name


async def run_migrations(migration_folder, pg, *, migration_table=MIGRATION_TABLE):
    if not await does_migration_table_exist(pg, migration_table):
        await create_migration_table(pg, migration_table)
    modules = glob.glob(join(migration_folder, "*.py"))
    migrations = [(f, basename(f)[:-3]) for f in modules if isfile(f) and not f.endswith('__init__.py')]
    async with pg.transaction():
        for path, name in migrations:
            # importlib.import_module()
            mod = SourceFileLoader(f"GiantSquid.migrations.{name}", path).load_module()
            await mod.migration.run(pg, migration_table)
