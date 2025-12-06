from flask import Flask, render_template_string, jsonify
app = Flask(__name__)

TEMPLATE = '''
<h2>Digital KYC — Admin Dashboard (Stub)</h2>
<p>List of recent KYC jobs (simulated)</p>
<ul>
  <li>job_1 - <strong>needs_review</strong></li>
  <li>job_2 - <strong>approved</strong></li>
</ul>
'''
@app.route("/")
def index():
    return render_template_string(TEMPLATE)

@app.route("/api/jobs")
def jobs():
    return jsonify([{"id":"job_1","status":"needs_review"},{"id":"job_2","status":"approved"}])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
