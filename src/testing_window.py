from fasthtml.common import *
from main import main

css = Style('''
    body, html { height: 100%; margin: 0; }
    body { display: flex; flex-direction: column; }
    main { flex: 1 0 auto; }
    footer { flex-shrink: 0; padding: 10px; text-align: center; background-color: #333; color: white; }
    footer a { color: #9cf; }
    #grid { display: grid; grid-template-columns: repeat(20, 20px); grid-template-rows: repeat(20, 20px);gap: 1px; }
    .cell { width: 20px; height: 20px; border: 1px solid black; }
    .alive { background-color: green; }
    .dead { background-color: white; }
    .arcade-footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #000;
    color: #fff;
    padding: 10px 0;
    text-align: center;
  }
    .center-button {
    padding: 10px 20px;
    font-size: 40px; 
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  
}

''')

app = FastHTML(hdrs=(picolink, css))

messages = []

rt = app.route

@rt("/")
def get():
    return Head(Title("Seloria(Johan Voskamp's) side of the web")), Body(Div(A("Access my blog", href="/Blog")), Div(A('The Cotton Boardgame', href='/Cotton', style="text-align: center;")), Img(src="/IMG_2414.jpg"))

@rt("/Cotton")
def get():
    return Main(H1("Welcome to Cotton", style="text-align: center;"),
                H3("the boardgame"),
                Button("Start game", hx_get="/Cotton/Start-Game", hx_swap="outerHTML", cls="center-button"),
                Footer(
                        A(Button("Exit game"), href="/"), cls="arcade-footer"), cls="container", style="text-align: center;")

@rt("/message")
def get():
    return Main(P("Previous messages:"),
                *[P(msg) for msg in messages]
                )

@rt("/Cotton/Start-Game")
def get():
    return H1("Just imagine there is a working game here")

@rt("/Blog")
def get():
    return H1("Work in progress")


serve()