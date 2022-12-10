from flask import Flask,render_template,request, send_file
from downloader import download_song
from createzip import create_zip

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def main_page():
    if request.method == "POST":
        keyword = request.form['keyword'].replace(' ','').lower()
        limit = int(request.form['limit'])
        download_song(keyword,limit)
        create_zip()
        # send_mail(emailid)
        # email sending is not working due to some issues using google sign in for 3rd party apps.
        # print(keyword,emailid,limit)
    return render_template("index.html")

@app.route("/download")
def download_file():
    path = "final.zip"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True,port=8000)