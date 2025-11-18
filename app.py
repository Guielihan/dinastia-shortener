from flask import Flask, redirect, abort
import os

app = Flask(__name__)

# dicionario de atalhos
# aqui você cadastra os slugs curtinhos e os links gigantes
ROUTES = {
    # exemplos — depois você troca pelos seus links reais
    "band": "https://d1muf25xa11so8hp18.s27-usa-cloudfront-net.online/token/1db75a7d7fb3eeaaf22a079198f420d2/bandsports.m3u8",
    "bandsports": "https://d1muf25xa11so8hp19.s27-usa-cloudfront-net.online/token/0a94c62ae45689449a6e274478a85e4d/bandsports.m3u8",
    "globo": "https://d1muf25xa11so8hp19.s27-usa-cloudfront-net.online/token/2039005d79208152fa61a23f926c5290/globosp.m3u8",
    "premiere": "https://d1muf25xa11so8hp18.s27-usa-cloudfront-net.online/token/ef32b84bc6f5fa1592ab2ac6b136574c/premiere.m3u8",
    "hbo": "https://d1muf25xa11so8hp18.s27-usa-cloudfront-net.online/token/626d8059f664cdac988f8d72418dfd2f/hbo.m3u8",
    "record": "https://d1muf25xa11so8hp18.s27-usa-cloudfront-net.online/token/d70dae28f1d1cb2b0d295d120a6234fc/record.m3u8",
    "cinemax": "https://d1muf25xa11so8hp18.s27-usa-cloudfront-net.online/token/e7a8e2a2ca667c51e9e81ff6c4c66ca6/cinemax.m3u8"
    # "mouseboat": "https://SEU-LINK-GIGANTE-DO-MOUSEBOAT.m3u8",
}


@app.route("/")
def home():
    return (
        "<h1>Encutador de Link do Dinastia </h1>"
        "<p>chame o @guielihan no telegram para obter mais informações de como acessar a mídia ao vivo que deseja <br>"
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
