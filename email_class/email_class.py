from string import Template
from datetime import datetime

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.audio import MIMEAudio
import smtplib


class EmailClass:
    def __init__(self, email, senha):
        self._email = email
        self._senha = senha
        self._msg = MIMEMultipart()

    @property
    def email(self):
        return self._email

    @property
    def senha(self):
        return self._senha

    @property
    def msg(self):
        return self._msg

    def anexar_documento(self, documento_path):
        with open(documento_path, 'rb') as documento:
            file = MIMEBase('application', 'octet-stream')
            file.set_payload(documento.read())
        encoders.encode_base64(file)
        file.add_header('Content-Disposition', 'attachment', filename=documento_path)
        self.msg.attach(file)

    def anexar_audio(self, audio_path):
        with open(audio_path, 'rb') as audio:
            file = MIMEAudio(audio.read(), _subtype='mp3')
        file.add_header('Content-Disposition', 'attachment', filename=audio_path)
        self.msg.attach(file)

    def anexar_imagem(self, imagem_path):
        with open(imagem_path, 'rb') as img:
            img = MIMEImage(img.read())
        img.add_header('Content-Disposition', 'attachment', filename=imagem_path)
        self.msg.attach(img)

    def anexar_template(self, template_path, **kargs):
        with open(template_path, 'r') as html:
            template = Template(html.read())
            data = datetime.now().strftime('%d/%m/%Y')
            corpo_msg = template.substitute(nome=kargs['nome'], data=data)
            corpo = MIMEText(corpo_msg, 'html')
        self.msg.attach(corpo)

    def enviar_email(self, cliente, to_email, subject):
        self.msg['to'] = to_email
        self.msg['from'] = cliente
        self.msg['subject'] = subject

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.email, self.senha)
                smtp.send_message(self.msg)
                print('E-mail enviado com sucesso.')
            except Exception as e:
                print('E-mail não enviado...')
                print('Erro:', e)
