from dataclasses import dataclass
from fasthtml.common import *
from fasthtml.js import MarkdownJS, SortableJS



# 𝚔𝚒𝚝 custom CSS
#       - fonts: sauceCodeProNerd, sourceSansPro
fontlink = Link(rel="stylesheet", href="/style/fonts.css", type="text/css")
picocdn = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.pumpkin.min.css", type="text/css")
css = Style(':root {--pico-font-size: 100%; }')

db = database('db/logs-test-001.db')
logs = db.t.logs
if logs not in db.t:
    logs.create(id=int, title=str, done=bool, name=str, details=str, priority=int, pk='id')
Log = logs.dataclass()

app = FastHTML(hdrs=(picocdn,
                     css,
                     fontlink,
                     SortableJS('.sortable', 'todo-list'),
                     MarkdownJS('.markdown')))
rt = app.route


# This line ensures that the static files are served from the static folder.
# (req. for favicon, CSS etc.)
@rt("/{fname:path}.{ext:static}")
async def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

def render(log):
    return Li(A(log.title, href=f"/log/{log.id}"))


a_home = A("kit.gdn", href="/", cls='contrast')
title = "☕ kit.gdn"
title_a = H1(A(title, href="/"))


# Constants
pico_docs = A("Pico CSS Docs", href="https://picocss.com/docs") 
contrast = Button("Dark|Light", cls='contrast', hx_post="/", target_id='', hx_swap="afterbegin")
# <a class="contrast" aria-label="Turn off dark mode" href="/docs/colors"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 32 32" fill="currentColor" class="icon-theme-toggle  moon"><clipPath id="theme-toggle-cutout"><path d="M0-11h25a1 1 0 0017 13v30H0Z"></path></clipPath><g clip-path="url(#theme-toggle-cutout)"><circle cx="16" cy="16" r="8.4"></circle><path d="M18.3 3.2c0 1.3-1 2.3-2.3 2.3s-2.3-1-2.3-2.3S14.7.9 16 .9s2.3 1 2.3 2.3zm-4.6 25.6c0-1.3 1-2.3 2.3-2.3s2.3 1 2.3 2.3-1 2.3-2.3 2.3-2.3-1-2.3-2.3zm15.1-10.5c-1.3 0-2.3-1-2.3-2.3s1-2.3 2.3-2.3 2.3 1 2.3 2.3-1 2.3-2.3 2.3zM3.2 13.7c1.3 0 2.3 1 2.3 2.3s-1 2.3-2.3 2.3S.9 17.3.9 16s1-2.3 2.3-2.3zm5.8-7C9 7.9 7.9 9 6.7 9S4.4 8 4.4 6.7s1-2.3 2.3-2.3S9 5.4 9 6.7zm16.3 21c-1.3 0-2.3-1-2.3-2.3s1-2.3 2.3-2.3 2.3 1 2.3 2.3-1 2.3-2.3 2.3zm2.4-21c0 1.3-1 2.3-2.3 2.3S23 7.9 23 6.7s1-2.3 2.3-2.3 2.4 1 2.4 2.3zM6.7 23C8 23 9 24 9 25.3s-1 2.3-2.3 2.3-2.3-1-2.3-2.3 1-2.3 2.3-2.3z"></path></g></svg></a>
# <article aria-label="Theme switcher" id="theme-switcher"><button class="contrast"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 32 32" fill="currentColor" class="icon-theme-toggle theme-toggle moon"><clipPath id="theme-toggle-cutout"><path d="M0-11h25a1 1 0 0017 13v30H0Z"></path></clipPath><g clip-path="url(#theme-toggle-cutout)"><circle cx="16" cy="16" r="8.4"></circle><path d="M18.3 3.2c0 1.3-1 2.3-2.3 2.3s-2.3-1-2.3-2.3S14.7.9 16 .9s2.3 1 2.3 2.3zm-4.6 25.6c0-1.3 1-2.3 2.3-2.3s2.3 1 2.3 2.3-1 2.3-2.3 2.3-2.3-1-2.3-2.3zm15.1-10.5c-1.3 0-2.3-1-2.3-2.3s1-2.3 2.3-2.3 2.3 1 2.3 2.3-1 2.3-2.3 2.3zM3.2 13.7c1.3 0 2.3 1 2.3 2.3s-1 2.3-2.3 2.3S.9 17.3.9 16s1-2.3 2.3-2.3zm5.8-7C9 7.9 7.9 9 6.7 9S4.4 8 4.4 6.7s1-2.3 2.3-2.3S9 5.4 9 6.7zm16.3 21c-1.3 0-2.3-1-2.3-2.3s1-2.3 2.3-2.3 2.3 1 2.3 2.3-1 2.3-2.3 2.3zm2.4-21c0 1.3-1 2.3-2.3 2.3S23 7.9 23 6.7s1-2.3 2.3-2.3 2.4 1 2.4 2.3zM6.7 23C8 23 9 24 9 25.3s-1 2.3-2.3 2.3-2.3-1-2.3-2.3 1-2.3 2.3-2.3z"></path></g></svg>Turn off dark mode</button></article>


hd = Header(title_a, cls='hd')
ft = Footer(contrast, P(Span("© 2024"), Span(a_home)), cls='ft')

menu = Div(P(A("Notes", href="/log")), P(A("Demos", href="/llm")), cls='grid')

body = Body(Code("""We'll def test():"""), P("https://picocss.com/docs"))


# Home page (Cover page)
@rt("/")
def get():
    return Title("Hello, World!"), hd, Main(menu, cls='container'), ft
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
    return Title("Logs"), Header(H2("Notes"), P("Browse my notes")), Main(card, cls='container')

# Per Log page
@rt("/log/{id}")
def get(id:int):
    log = logs[id]
    return Main(
        log.title, 
        P(log.done), 
        A("Go back", href="/log"),
        )
