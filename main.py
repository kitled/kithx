from dataclasses import dataclass
from fasthtml.common import *
from fasthtml.js import MarkdownJS, SortableJS

# 𝚔𝚒𝚝 custom CSS
#       - fonts: sauceCodeProNerd, sourceSansPro
fontlink = Link(rel="stylesheet", href="/main.css", type="text/css")

db = database('db/logs-test-001.db')
logs = db.t.logs
if logs not in db.t:
    logs.create(id=int, title=str, done=bool, name=str, details=str, priority=int, pk='id')
Log = logs.dataclass()

app = FastHTML(hdrs=(picolink, fontlink,
                     Style(':root { --pico-font-size: 100%; }'),
                     SortableJS('.sortable', 'todo-list'),
                     MarkdownJS('.markdown')))
rt = app.route

def render(log):
    return Li(A(log.title, href=f"/log/{log.id}"))

# Home page (Cover page)
@rt("/")
def get():
    return Title("Hello, World!"), H1("kit.gdn"), P("TEST le thing")
    # logs_list = Ul(*map(render, logs()))
    # return Page("kit's home", 
    # P("Check out my super log!"), 
    # A("Kit's Log", href="/log"),
    # H3("List of links"),
    # logs_list,
    # )

# Logs page
@rt("/log")
def get():
    logs_list = Ul(*map(render, logs()))
    card = Card(logs_list, header="hd", footer="ft")
    return Title("Logs"), Main(card, cls='container')

# Per Log page
@rt("/log/{id}")
def get(id:int):
    log = logs[id]
    return Page(
        log.title, 
        P(log.done), 
        A("Go back", href="/log"),
        )
