from flask import Flask, redirect, abort
import os

app = Flask(__name__)

# dicionario de atalhos
# aqui você cadastra os slugs curtinhos e os links gigantes
ROUTES = {
    # exemplos — depois você troca pelos seus links reais
    "avatar": "https://SEU-LINK-GIGANTE-DO-AVATAR.m3u8",
    "sportv2": "https://SEU-LINK-GIGANTE-DO-SPORTV2.m3u8",
    # "mouseboat": "https://SEU-LINK-GIGANTE-DO-MOUSEBOAT.m3u8",
}


@app.route("/")
def home():
    return (
        "<h1>Encurta Dinastia </h1>"
        "<p>Use /avatar, /sportv2, /mouseboat... <br>"
        "Edite o dicionário ROUTES no código para cadastrar novos atalhos.</p>"
    )


@app.route("/<slug>")
def redirect_slug(slug):
    url = ROUTES.get(slug)
    if not url:
        abort(404)
    return redirect(url, code=302)


if __name__ == "__main__":
    # render envia a porta em uma variável de ambiente chamada port
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
