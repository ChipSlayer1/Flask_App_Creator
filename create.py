import os

print("Select app location:")
directory = input()

print("Select app name:")
name = input()

os.chdir(directory)
os.system("mkdir {}".format(name))
os.chdir("{}/{}".format(directory, name))
os.system("touch {}.py".format(name))
os.system("touch {}.sh".format(name))
os.system("chmod +x {}.sh".format(name))
os.system("mkdir templates")
os.system("mkdir static")
os.chdir("{}/{}/templates".format(directory, name))
os.system("touch index.html")
os.chdir("{}/{}/static".format(directory, name))
os.system("mkdir js_files")
os.system("mkdir css_files")
os.chdir("{}/{}/static/js_files".format(directory, name))
os.system("touch index.js")
os.chdir("{}/{}/static/css_files".format(directory, name))
os.system("touch index.css")
os.chdir("{}/{}".format(directory, name))

f = open("templates/index.html", "w")
f.write('<html>\n\
        <head>\n\
            <title>INDEX.html</title>\n\
            <meta charset="utf-8">\n\
            <link rel="stylesheet" href="{}">\n\
        </head>\n\
        <body>\n\
            <script src="{}"></script>\n\
        </body>\n\
    </html>'.format("{{url_for('static', filename='index.css')}}", "{{url_for('static', filename='index.js')}}"))
f.close()

f = open("{}.py".format(name), "w")
f.write('from flask import Flask, render_template, request, jsonify, redirect\n\
\n\
app = Flask(__name__)\n\
\n\
@app.route("/")\n\
def index():\n\
    return render_template("index.html")\n\
\n\
@app.route("/receiver", methods=["GET", "POST"])\n\
def receiver():\n\
    data = request.get_json()\n\
    return jsonify(data)\n\
\n\
if __name__ == "__main__":\n\
    app.run(debug=False, host="0.0.0.0")')
f.close()

f = open("{}.sh".format(name), "w")
f.write("python3 {}.py".format(name))
f.close()

print("Created. :)")

os.system("code -a .")
