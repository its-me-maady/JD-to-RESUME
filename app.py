from flask import Flask

app = Flask(__name__)

@app.get("/")
def main():
    print("Hello from jd-to-resume!")
    return "Hello from jd-to-resume!" ,200

@app.post("/details")
def details():
    return ""

@app.get("/progress/<id:int>")
def progress(id):
    return ""

@app.post('/download/<id:int>')
def download(id):
    return ""


if __name__ == "__main__":
    main()
