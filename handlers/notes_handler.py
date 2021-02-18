from datetime import datetime

from aiohttp import web
from aiohttp.abc import Request

from data.db import Session
from data.note import Note


async def get_notes(request):
    session = Session()
    notes = list([note.to_dict() for note in session.query(Note).order_by(Note.id)])
    session.close()

    return web.json_response(notes)


async def post_note(request: Request):
    d = await request.json()

    session = Session()
    note = Note(id=None, content=d['content'], create_date=datetime.now())
    session.add(note)
    session.commit()

    session.close()
    return web.HTTPCreated()