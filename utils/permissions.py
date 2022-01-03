import time
import json
import traceback
import timeago as timesince
from collections import namedtuple

def get(file):
    try:
        with open(file, encoding='utf8') as data:
            return json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    except AttributeError:
        raise AttributeError("Unknown argument")
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")

def traceback_maker(err, advance: bool = True):
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = ('```py\n{1}{0}: {2}\n```').format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"

def timetext(name):
    return f"{name}_{int(time.time())}.txt"

def timeago(target):
    return timesince.format(target)

def date(target, clock=True):
    if clock is False:
        return target.strftime("%d %B %Y")
    return target.strftime("%d %B %Y, %H:%M")

def has_voted(ctx, bot):
    if ctx.author.id in bot.owner_ids or ctx.author.id in bot.developers:
        return True
    voted = await bot.session.get(
        url=f"https://top.gg/api/bots/732119152885497867/check?userId={ctx.author.id}",
        headers={"Authorization": bot.topgg_token}
        )
    voted = await voted.json()["voted"]
    if voted == 1:
        return True
    return False