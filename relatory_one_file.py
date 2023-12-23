import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from jinja2 import Environment, Template
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

# HTML Template como string
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Relatório de Vendas</title>
</head>
<body>
    <h1>Relatório de Vendas</h1>
    <p>Este é um exemplo de relatório que mostra o total de vendas por dia.</p>
    <img src="{img_tag}" alt="Total Bill by Day">
</body>
</html>
"""

# Renderizando o template HTML
html_out = html_template

# Salvando o relatório como PDF
pdfkit.from_string(html_out, "report.pdf")
