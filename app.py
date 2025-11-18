from flask import Flask, redirect, abort
import os

app = Flask(__name__)

# dicionario de atalhos
# aqui você cadastra os slugs curtinhos e os links gigantes
ROUTES = {
    # exemplos — depois você troca pelos seus links reais
    "band": "https://d1muf25xa11so8hp18.s27-usa-cloudfront-net.online/token/1db75a7d7fb3eeaaf22a079198f420d2/bandsports.m3u8",
    "space": "https://d1muf25xa11so8hp18.s27-usa-cloudfront-net.online/token/370e7a0007e0ad9a59fdc8e7bbe7fe22/space.m3u8",
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
