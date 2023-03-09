import csv
import os
from datetime import datetime
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

from cryptoGym import settings


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
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from fpdf import FPDF

from django.http import HttpResponse
from django.apps import apps
from tablib import Dataset
from fpdf import FPDF
import os
import datetime


def agregar_numero_pagina(pdf, numero_pagina):
    pdf.set_y(-15)
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0, 10, f'Página {numero_pagina}', align='C')
    pdf.alias_nb_pages()


def generar_pdf(request, modelo_nombre):
    modelo = apps.get_model(app_label='api', model_name=modelo_nombre)
    queryset = modelo.objects.all()
    fields = [field.name for field in modelo._meta.fields if field.name != 'clave']
    data = Dataset(headers=fields)
    for obj in queryset:
        row = [getattr(obj, field) for field in fields]
        data.append(row)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{modelo_nombre}.pdf"'

    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.alias_nb_pages()
    pdf.add_page()

    # Agregar logo
    current_path = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_path, 'gym-crypto.png')
    pdf.image(logo_path, x=200, y=10, w=20)

    pdf.set_font('Arial', 'B', 12)
    row_height = pdf.font_size * 2
    pdf.cell(0, row_height, "Crypto Gym", ln=1, align='C')
    pdf.ln(10)

    # Agregar fecha y hora en el encabezado
    now = datetime.datetime.now()
    pdf.cell(0, row_height, f"Fecha: {now.date()}", ln=1, align='L')
    pdf.cell(0, row_height, f"Hora: {now.time()}", ln=1, align='L')
    pdf.ln(10)
    pdf.cell(0, row_height, f"Total de registros: {len(data)}", ln=1, align='L')
    pdf.ln(10)
    # creado por
    pdf.cell(0, row_height, f"Creado por: ", ln=1, align='L')

    pdf.set_font('Arial', '', 12)

    # Calcular el ancho máximo de cada columna
    max_widths = [pdf.get_string_width(str(header)) for header in fields]
    for row in data:
        for i in range(len(fields)):
            cell_width = pdf.get_string_width(str(row[i]))
            if cell_width > max_widths[i]:
                max_widths[i] = cell_width

    # Agregar encabezados de columna
    for i in range(len(fields)):
        pdf.cell(max_widths[i], row_height, str(fields[i]), border=1)
    pdf.ln()

    # Agregar datos a la tabla
    page_num = pdf.page_no()
    for row in data:
        if pdf.page_no() != page_num:
            pdf.set_y(-15)
            pdf.set_font('Arial', 'I', 8)
            pdf.cell(0, 10, f'Página {page_num}', align='C')
            pdf.add_page()
            for i in range(len(fields)):
                pdf.cell(max_widths[i], row_height, str(fields[i]), border=1)
            pdf.ln()
        for i in range(len(fields)):
            pdf.cell(max_widths[i], row_height, str(row[i]), border=1, )
        pdf.ln()

    # Agregar numeración de página en el pie de página
    pdf.set_y(-15)
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0, 10, f'Página {pdf.page_no()}', align='R')


    response.write(pdf.output(dest='S').encode('latin-1'))
    return response
