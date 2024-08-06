from fasthtml.common import *
from starlette.staticfiles import StaticFiles

css = Style('''
            test
            ''')

app = FastHTML(hdrs=(picolink, css))

app.mount("/static", StaticFiles(directory="src"), name="static")

rt = app.route

@rt("/")
def get():
    return Head(Title("Seloria")), Body((A("Access my blog", href="/Blog"), A('The Cotton Boardgame', href='/Cotton'), Img(src="/static/IMG_2414.jpg")), style="text-align: center;")
    
@rt("/test-image")
async def get():
    return FileResponse("src/static/IMG_2414.jpg")

@rt("/Cotton")
def get():
    return Main(H1("Welcome to Cotton", style="text-align: center;"),
                H3("the boardgame"),
                Button("Start game", hx_get="/Cotton/Start-Game", hx_swap="outerHTML", cls="center-button"),
                Footer(
                        A(Button("Exit game"), href="/"), cls="arcade-footer"), cls="container", style="text-align: center;")


@rt("/Cotton/Start-Game")
def get():
    return H1("Just imagine there is a working game here")

@rt("/Blog")
def get():
    return H1("Work in progress", style="text-align: center")


serve()