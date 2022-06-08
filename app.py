import dash
from dash import Dash, html

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
    "https://www.googletagmanager.com/gtag/js?id=G-4PJELX1C4W",
]

app = Dash(
    __name__,
    # suppress_callback_exceptions=True,
    # plugins=[dl.plugins.pages],
    # external_scripts=scripts,
    # update_title=None,
)

app.layout = html.Div("this is where my site will go")

server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
