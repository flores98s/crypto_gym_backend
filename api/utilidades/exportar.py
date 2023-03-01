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
import tablib
from fpdf import FPDF
from django.apps import apps

def generar_pdf(request, modelo_nombre):
    modelo = apps.get_model(app_label='api', model_name=modelo_nombre)
    queryset = modelo.objects.all()
    fields = [field.name for field in modelo._meta.fields]
    data = tablib.Dataset(headers=fields)
    for obj in queryset:
        row = [getattr(obj, field) for field in fields]
        data.append(row)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mi_archivo.pdf"'

    # Crear el PDF y establecer la fuente
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    # Ajustar el ancho de las columnas al contenido
    col_widths = []
    for col in data.headers:
        # Obtener el ancho máximo de la columna
        max_width = pdf.get_string_width(col)
        for row in data:
            cell_width = pdf.get_string_width(str(row[col]))
            if cell_width > max_width:
                max_width = cell_width
        col_widths.append(max_width + 6) # agregar un margen

    # Crear la tabla y agregar los encabezados
    pdf.set_fill_color(230, 230, 230)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', 'B', 12)
    for i, col in enumerate(data.headers):
        pdf.cell(col_widths[i], 10, col, 1, 0, 'C', True)
    pdf.ln()

    # Agregar los datos de la tabla
    pdf.set_font('Arial', '', 12)
    for row in data:
        for i, col in enumerate(data.headers):
            if isinstance(row[col], str) and len(row[col]) > 50:
                # Agregar un salto de línea para ajustar el texto largo
                pdf.multi_cell(col_widths[i], 10, row[col], 1)
            else:
                pdf.cell(col_widths[i], 10, str(row[col]), 1)
        pdf.ln()

    pdf.output(response, 'F')
    return response
