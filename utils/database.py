import rethinkdb as rdb
from discord.ext import commands as cmd


rdb.set_loop_type("asyncio")
con = None

host, port, database = "localhost", 28015, "urlshortener"
table_setup = {
    "urlshortener": {
        "urls": {},
    }
}


async def setup():
    global con
    con = await rdb.connect(host=host, port=port, db=database)

    for db_name, tables in table_setup.items():
        if db_name not in await rdb.db_list().run(con):
            await rdb.db_create(db_name).run(con)

        db = rdb.db(db_name)
        for table_name, data in tables.items():
            if table_name not in await db.table_list().run(con):
                await db.table_create(table_name).run(con)

                if len(data) >= 0:
                    await db.table(table_name).insert(data).run(con)
