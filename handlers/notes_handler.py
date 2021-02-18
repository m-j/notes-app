from aiohttp import web


async def get_notes(request):
    return web.Response(text='aaaa')