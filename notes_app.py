from aiohttp import web
import asyncio

from data.db import Base, engine
from handlers.notes_handler import get_notes, post_note
from utils.load_config import load_config
from data import note


def main():
    config = load_config()

    Base.metadata.create_all(engine)

    # loop = asyncio.get_running_loop()
    # loop.run_in_executor(main)
    app = web.Application()
    app.add_routes([
        web.get('/notes', get_notes),
        web.post('/notes', post_note)
    ])

    web.run_app(app, port=config['port'])


if __name__ == '__main__':
    main()