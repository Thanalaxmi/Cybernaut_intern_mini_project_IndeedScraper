from flask import Flask, render_template, request
import json

app = Flask(__name__)

def load_jobs():
    with open('jobs.json', 'r') as f:
        jobs = json.load(f)
    return jobs

@app.route("/")
def index():
    query = request.args.get('q', '')
    location = request.args.get('location', '')
    jobs = load_jobs()
    if query:
        jobs = [job for job in jobs if query.lower() in job['title'].lower()]
    if location:
        jobs = [job for job in jobs if location.lower() in job['location'].lower()]
    return render_template("jobs-1.html", jobs=jobs, query=query, location=location)

if __name__ == "__main__":
    app.run(debug=True)
