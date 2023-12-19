
import os

GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
from weasyprint import HTML

htmlStart = '<html><head><style> body { padding: 0; margin: 0; }table, th, td { border: 1px solid black; border-collapse: collapse;}th, td { padding: 5px; text-align: left;}table { width: 100%;}tr { height: 38px;}th { font-weight: normal;}</style></head><body> <p style="text-align: right;">«____» ______________ 20 ___ г.</p><p style="text-align: center;"><span style="font-size: 24px; font-weight: bold;">НАКЛАДНАЯ № </span> _____</p><p style="text-align: justify;">Кому ___________________________________________________________________________</p><p style="text-align: justify;">От кого _________________________________________________________________________</p><table> <tr> <th>№<br>п/п</th> <th>Наименование груза</th> <th>Масса груза</th> <th>ИНН</th> <th>Ответственный</th> </tr> '
htmlEnd = '</table><p style="margin-bottom: 0;">Сдал: __________ ________________ Принял: __________ ________________</p><p style="margin-top: 0; font-size: small;"><span style="margin-left: 65px;">подпись</span> <span style="margin-left: 60px;">Ф., И., О.</span> <span style="margin-left: 110px;">подпись</span> <span style="margin-left: 60px;">Ф., И., О.</span></p></body></html>'
htmlMid = ''
data = input("Введите через запятую ИНН, наименование груза, массу груза, ФИО ответственного:\n")
i = 1
while data != "":
    datalist = data.split(",")
    htmlMid += f"<tr> <th>{i}</th> <th>{datalist[1].lstrip()}</th> <th>{datalist[2].lstrip()}</th> <th>{datalist[0].lstrip()}</th> <th>{datalist[3].lstrip()}</th> </tr>"
    i += 1
    if i > 18:
        break
    data = input()

while i <= 18:
    htmlMid += "<tr> <th></th> <th></th> <th></th> <th></th> <th></th> </tr>"
    i += 1

HTML(string=htmlStart + htmlMid + htmlEnd).write_pdf('bill.pdf')
