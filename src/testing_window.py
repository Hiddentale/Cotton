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
''')

app = FastHTML(hdrs=(picolink, css))

messages = []

rt = app.route

@rt("/")
def get():
    return Head(Title("Seloria's blog")), Body(Div(H1("Welcome to my Blog!")), Div(A('The Cotton Boardgame', href='/Cotton', style="text-align: center;")), Img(src="https://placehold.co/200"))

@rt("/Cotton")
def get():
    return Div(main(), id="grid")

#Main(H1("Welcome to Cotton"),
                #H3("the boardgame"),
                #Div(Button(A("Exit game", href="/" )), cls="container")) # Need to understand and then fix this, only temporary solution

@rt("/Cotton")
def put():
    print("Memes")

@rt("/message")
def get():
    return Main(P("Previous messages:"),
                *[P(msg) for msg in messages]
                )


serve()