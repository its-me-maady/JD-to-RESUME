from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'docx', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get("/")
def main():
    return render_template("home.html") ,200

@app.post("/generate_resume")
def details():
    file=request.files["resume_file"]
    job_description=request.form["job_description"]
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
            # Process the file and job description here
            return render_template("result.html", job_description=job_description), 200
    flash('Invalid file type')
    return redirect(request.url)




if __name__ == "__main__":
    main()
