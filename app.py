from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [
    {
        "id": 1,
        "job_profile": "Python Developer",
        "location": "Chennai, India",
        "salary": "7,50,000"
    },
    {
        "id": 2,
        "job_profile": "Full Stack Developer",
        "location": "Bangalore, India",
        "salary": "10,00,000"
    },
    {
        "id": 3,
        "job_profile": "Java Developer",
        "location": "Coimbatore, India",
        "salary": "8,50,000"
    }
]


@app.route('/')
def home():
    return render_template('index.html', jobs=Jobs)


@app.route('/api/jobs')
def all_jobs():
    return jsonify(Jobs)


if __name__ == "__main__":
    app.run(debug=True)