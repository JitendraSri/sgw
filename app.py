from flask import Flask, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

# Generate PDF Function
def generate_pdf(student_name, course, university, enrollment_id):
    pdf_path = f"confirmation_{enrollment_id}.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(100, 750, "Global Students Abroad Council")
    c.drawString(100, 730, "Enrollment Confirmation Letter")
    c.drawString(100, 700, f"Student Name: {student_name}")
    c.drawString(100, 680, f"Selected Course: {course}")
    c.drawString(100, 660, f"University: {university}")
    c.drawString(100, 640, f"Enrollment ID: {enrollment_id}")
    c.drawString(100, 600, "Congratulations! Your enrollment is confirmed.")
    
    c.save()
    return pdf_path

# API Route to Generate and Download PDF
@app.route('/download_confirmation', methods=['POST'])
def download_confirmation():
    data = request.json
    student_name = data.get("student_name")
    course = data.get("course")
    university = data.get("university")
    enrollment_id = data.get("enrollment_id")

    pdf_path = generate_pdf(student_name, course, university, enrollment_id)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
