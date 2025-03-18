from flask import Flask, render_template, request, redirect, url_for
from fpdf import FPDF
import os

app = Flask(__name__, template_folder="project/templates")  # Explicitly set templates folder


# Ensure PDF folder exists
PDF_FOLDER = "static/pdfs/"
if not os.path.exists(PDF_FOLDER):
    os.makedirs(PDF_FOLDER)

@app.route('/')
def home():
    return render_template('home.html')

# Thesis Approval Form Route
@app.route('/form_submit/thesis', methods=['GET', 'POST'])
def form_submit_thesis():
    if request.method == 'POST':
        student_name = request.form['student_name']
        uh_id = request.form['uh_id']
        student_email = request.form['student_email']
        degree = request.form['degree']
        program = request.form['program']
        defense_date = request.form['defense_date']
        graduation_date = request.form['graduation_date']
        thesis_title = request.form['thesis_title']
        date = request.form['date']

        # Generate Thesis PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "Written Thesis Approval Form", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, f"Student Name: {student_name}", ln=True)
        pdf.cell(200, 10, f"UH ID: {uh_id}", ln=True)
        pdf.cell(200, 10, f"Student Email: {student_email}", ln=True)
        pdf.cell(200, 10, f"Degree: {degree}", ln=True)
        pdf.cell(200, 10, f"Program: {program}", ln=True)
        pdf.cell(200, 10, f"Defense Date: {defense_date}", ln=True)
        pdf.cell(200, 10, f"Anticipated Graduation Date: {graduation_date}", ln=True)
        pdf.cell(200, 10, f"Thesis Title: {thesis_title}", ln=True)
        pdf.cell(200, 10, f"Submission Date: {date}", ln=True)

        # Save PDF
        pdf_path = os.path.join(PDF_FOLDER, f"{uh_id}_thesis_approval.pdf")
        pdf.output(pdf_path)

        return f"Form submitted! <a href='/{pdf_path}'>Download PDF</a>"

    return render_template('form_submit_thesis.html')

# Instructor Drop Form Route
@app.route('/form_submit/drop', methods=['GET', 'POST'])
def form_submit_drop():
    if request.method == 'POST':
        student_name = request.form['student_name']
        uh_id = request.form['uh_id']
        course_subject = request.form['course_subject']
        course_number = request.form['course_number']
        semester = request.form['semester']
        year = request.form['year']
        date = request.form['date']

        # Generate Drop Form PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "Instructor-Initiated Drop Form", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, f"Student Name: {student_name}", ln=True)
        pdf.cell(200, 10, f"UH ID: {uh_id}", ln=True)
        pdf.cell(200, 10, f"Course Subject: {course_subject}", ln=True)
        pdf.cell(200, 10, f"Course Number: {course_number}", ln=True)
        pdf.cell(200, 10, f"Semester: {semester} {year}", ln=True)
        pdf.cell(200, 10, f"Submission Date: {date}", ln=True)

        # Save PDF
        pdf_path = os.path.join(PDF_FOLDER, f"{uh_id}_drop_form.pdf")
        pdf.output(pdf_path)

        return f"Form submitted! <a href='/{pdf_path}'>Download PDF</a>"

    return render_template('form_submit_drop.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
