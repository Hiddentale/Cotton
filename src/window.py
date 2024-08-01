from fasthtml.common import *


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

gridlink = Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/flexboxgrid/6.3.1/flexboxgrid.min.css", type="text/css")
htmx_ws = Script(src="https://unpkg.com/htmx-ext-ws@2.0.0/ws.js")
app = FastHTML(hdrs=(picolink, gridlink, css, htmx_ws))
rt = app.route

game_state = {'running': False, 'grid': [[0 for _ in range(20)] for _ in range(20)]}

#@rt('/')
#def get(): return Div(P('Welcome to Cotton, press me to start the game'), hx_get="/change")
#@rt('/change')
#def get(): return P('Launching Cotton')


def Grid():
    cells = []
    for y, row in enumerate(game_state['grid']):
        for x, cell in enumerate(row):
            cell_class = 'alive' if cell else 'dead'
            cell = Div(cls=f'cell {cell_class}', hx_put='/update', hx_vals={'x': x, 'y': y}, hx_swap='none', hx_target='#gol', hx_trigger='click')
            cells.append(cell)
    return Div(*cells, id='grid')

def Home():
    gol = Div(Grid(), id='gol', cls='row center-xs')
    run_btn = Button('Run', id='run', cls='col-xs-2', hx_put='/run', hx_target='#gol', hx_swap='none')
    pause_btn = Button('Pause', id='pause', cls='col-xs-2', hx_put='/pause', hx_target='#gol', hx_swap='none')
    reset_btn = Button('Reset', id='reset', cls='col-xs-2', hx_put='/reset', hx_target='#gol', hx_swap='none')
    main = Main(gol, Div(run_btn, pause_btn, reset_btn, cls='row center-xs'), hx_ext="ws", ws_connect="/gol")
    footer = Footer(P('Made by Nathan Cooper. Check out the code', AX('here', href='https://github.com/AnswerDotAI/fasthtml-example/tree/main/game_of_life', target='_blank')))
    return Title('Game of Life'), main, footer

@rt('/')
def get(): return Home()

serve() 