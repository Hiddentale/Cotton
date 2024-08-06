from fasthtml.common import *
from starlette.staticfiles import StaticFiles

stylesheet_link = Link(rel="stylesheet", href="static/css/styles.css")

app = FastHTML(hdrs=(picolink, stylesheet_link))

app.mount("/static", StaticFiles(directory="src/static"), name="static")

rt = app.route

@rt("/")
def get():
    return Head(Title("Seloria")), \
           Body(
               Header(Div(Img(src="/static/images/IMG_2414.jpg", cls="profile-pic")), "Welcome to Seloria's Emporia!", style="font-family: Lodeh Regular"),
               Nav(Ul(
                   Li(A("Access my blog", href="/Blog")),
                   Li(A('The Cotton Boardgame', href='/Cotton')),
                   Li(A('About', href='/About')),
                   Li(A('Contact me', href='/Contact'))
               )),
               Main(
                   Section(
                       H2("About me"),
                       P("This is a brief introduction about me."),
                       Img(src="/static/images/IMG_2414.jpg", cls="profile-pic")
                   ),
               ),
               Footer(P("2024, Seloria"))
           )

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
    return Header("Collection of random stuff that crosses my mind"), \
           Section(Li(A("Here goes my first blogpost", href="/Blog-1")), style="text-align: center"), \
           Section(Li(A("Here goes my second blogpost", href="/Blog-2")), style="text-align: center")

@rt("/Blog-1")
def get():
    return H1("Work in progress", style="text-align: center")

@rt("/Blog-2")
def get():
    return H1("Work in progress", style="text-align: center")


@rt("/About")
def get():
    return H1("Work in progress", style="text-align: center")

@rt("/Contact")
def get():
    return H1("Work in progress", style="text-align: center")


serve()