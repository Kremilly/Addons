from apis.qrcode import QRCode
from apis.sci_hub import SciHub
from apis.pdf_info import PDFInfo
from apis.pdf_thumb import PDFThumb
from apis.wikipedia import Wikipedia
from apis.pdf_scrape import PDFScrape

from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://scibun.com')

@app.route('/qrcode', methods=['GET'])
def qrcode():
    return QRCode({
        'url': request.args.get('url')
    }).get()

@app.route('/pdfthumb', methods=['GET'])
def pdfthumb():
    return PDFThumb({
        'pdf': request.args.get('pdf'),
        'page': request.args.get('page'),
        'width': request.args.get('width'),
        'height': request.args.get('height'),
    }).get()

@app.route('/wikipedia', methods=['GET'])
def wikipedia():
    return Wikipedia({
        'term': request.args.get('term'),
        'location': request.args.get('location'),
        'thumb_size': request.args.get('thumb_size'),
        'short_summary': request.args.get('short_summary'),
    }).get()

@app.route('/scihub', methods=['GET'])
def scihub():
    return SciHub({
        'paper': request.args.get('paper')
    }).get()
    
@app.route('/pdfscrape', methods=['GET'])
def pdfscrape():
    return PDFScrape({
        'url': request.args.get('url')
    }).get()

@app.route('/pdfinfo', methods=['GET'])
def pdfinfo():
    return PDFInfo({
        'pdf': request.args.get('pdf')
    }).get()

if __name__ == '__main__':
    app.run(debug=True)