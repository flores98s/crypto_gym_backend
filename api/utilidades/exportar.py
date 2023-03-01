import csv
from io import BytesIO
from django.http import HttpResponse
import tablib
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.apps import apps
from fpdf import FPDF
from tablib import Dataset

def generar_csv(request, modelo_nombre):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mi_archivo.csv"'
    writer = csv.writer(response)
    modelo = apps.get_model(app_label='api', model_name=modelo_nombre)
    fields = [field.name for field in modelo._meta.fields]
    writer.writerow(fields)
    for obj in modelo.objects.all():
        row = [getattr(obj, field) for field in fields]
        writer.writerow(row)
    return response

# def generar_pdf(request, modelo_nombre):
#     modelo = apps.get_model(app_label='api', model_name=modelo_nombre)
#     queryset = modelo.objects.all()
#     fields = [field.name for field in modelo._meta.fields if isinstance(field.name, str)]
#     data = tablib.Dataset(headers=fields)
#     for obj in queryset:
#         row = [str(getattr(obj, field)) for field in fields]
#         data.append(row)
#     print(data.dict)

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="mi_archivo.pdf"'

#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter)
#     styles = getSampleStyleSheet()
#     elements = []
#     t = Table(data, style=TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('FONTSIZE', (0, 0), (-1, 0), 14),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
#         ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
#         ('FONTSIZE', (0, 1), (-1, -1), 12),
#         ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
#     ]))
#     elements.append(t)
#     doc.build(elements)
#     response.write(buffer.getvalue())
#     buffer.close()
#     return response

from django.http import HttpResponse
from django.apps import apps
from io import BytesIO
from tablib import Dataset
from fpdf import FPDF

def generar_pdf(request, modelo_nombre):
    modelo = apps.get_model(app_label='api', model_name=modelo_nombre)
    queryset = modelo.objects.all()
    fields = [field.name for field in modelo._meta.fields]
    data = Dataset(headers=fields)
    for obj in queryset:
        row = [getattr(obj, field) for field in fields]
        data.append(row)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mi_archivo.pdf"'

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Datos del modelo ' + modelo_nombre)
    pdf.ln()
    pdf.set_font('Arial', 'B', 12)
    col_width = pdf.w / len(fields)
    row_height = pdf.font_size * 2
    for field in fields:
        pdf.cell(col_width, row_height, str(field), border=1)
    pdf.ln()
    pdf.set_font('Arial', '', 12)
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height, str(item), border=1)
        pdf.ln()

    response.write(pdf.output(dest='S').encode('latin-1'))
    return response
