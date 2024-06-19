from dataclasses import dataclass
from fasthtml.common import *
from fasthtml.js import MarkdownJS, SortableJS


db = database('db/logs.db')
logs = db.t.logs
if logs not in db.t:
    logs.create(id=int, title=str, done=bool, name=str, details=str, priority=int, pk='id')
Log = logs.dataclass()

