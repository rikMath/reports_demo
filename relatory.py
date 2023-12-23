import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from jinja2 import Environment, FileSystemLoader
import pdfkit

# Carregar e criar o gráfico
data = sns.load_dataset("tips")
plt.figure(figsize=(10,6))
sns.barplot(x="day", y="total_bill", data=data)
plt.title("Total Bill by Day")

# Salvar o gráfico em um buffer
img_buffer = BytesIO()
plt.savefig(img_buffer, format='png')
plt.close()
img_buffer.seek(0)
img_data = img_buffer.getvalue()

# Codificar a imagem em base64
data_uri = base64.b64encode(img_data).decode('utf-8')
img_tag = f'data:image/png;base64,{data_uri}'

# CSS
with open("style.css", "r") as file:
    css_style = file.read()

# Carregando o template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('report_template.html')

# Renderizando o template
html_out = template.render(css_style=css_style, img_tag=img_tag)

# Opções do PDF
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

# Salvando o relatório como PDF
pdfkit.from_string(html_out, "report.pdf", options=options)
