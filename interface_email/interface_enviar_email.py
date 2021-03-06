import sys
from email_class.email_class import EmailClass
from interface_email.interface import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class Interface_Enviar_Email(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnImagem.clicked.connect(self.anexar_imagem)
        self.btnAudio.clicked.connect(self.anexar_audio)
        self.btnDocumentos.clicked.connect(self.anexar_documento)
        self.btnTemplate.clicked.connect(self.anexar_template)
        self.btnEnviar.clicked.connect(self.enviar)
        self.btnPara.clicked.connect(self.anexar_emails_para)
        self.msg = EmailClass()
        self.emails_para = []

    def name_input(self, name_path):
        name = ''
        for n in name_path:
            name_aux = n.split(sep='/')
            name += name_aux[-1]
            name += ' | '
        return name[:-2]

    def anexar_imagem(self):
        imagem, _ = QFileDialog.getOpenFileNames(
            self.centralwidget,
            'Anexar Imagem',
            '/home/Downloads/',
        )
        for v in imagem:
            try:
                self.msg.anexar_imagem(v)
            except Exception as e:
                print(e)
                self.inputImagem.setText('Formato de imagem invalido!')
                return
        name = self.name_input(imagem)
        self.inputImagem.setText(name)

    def anexar_audio(self):
        audio, _ = QFileDialog.getOpenFileNames(
            self.centralwidget,
            'Anexar Áudio',
            '/home/Downloads/',
        )
        for v in audio:
            try:
                self.msg.anexar_audio(v)
            except Exception as e:
                print(e)
                self.inputAudio.setText('Formato de audio invalido!')
                return

        name = self.name_input(audio)
        self.inputAudio.setText(name)

    def anexar_documento(self):
        documento, _ = QFileDialog.getOpenFileNames(
            self.centralwidget,
            'Anexar Documento',
            '/home/Downloads/',
        )
        for v in documento:
            try:
                self.msg.anexar_documento(v)
            except Exception as e:
                print(e)
                self.inputDocumentos.setText('Formato de documento invalido!')
                return
        name = self.name_input(documento)
        self.inputDocumentos.setText(name)

    def anexar_template(self):
        template, _ = QFileDialog.getOpenFileNames(
            self.centralwidget,
            'Anexar Template',
            '/home/Downloads/',
        )
        for v in template:
            try:
                self.msg.anexar_template(v, nome='Gabriel Alexandre')
            except Exception as e:
                print(e)
                self.inputTemplate.setText('Formato de template invalido!')
                return
        name = self.name_input(template)
        self.inputTemplate.setText(name)

    def anexar_emails_para(self):
        emails, _ = QFileDialog.getOpenFileNames(
            self.centralwidget,
            'Anexar Template',
            '/home/Downloads/',
        )

        if len(emails) > 1:
            self.inputPara.setText('Anexe apenas um arquivo!')
            return

        name_aux = emails[0].split(sep='/')
        name = name_aux[-1]

        if name[-3::] != 'txt':
            self.inputPara.setText('Anexe um arquivo de texto!')
            return

        with open(emails[0], 'r') as arq:
            email = arq.read()

        aux = ''
        email_aux = email.split(sep=',')
        for c, v in enumerate(email_aux):
            self.emails_para.append(v.strip().replace('\n', ''))
            if c < len(email_aux) - 1:
                aux += v + ' | '
            else:
                aux += v
        self.inputPara.setText(aux)


    def enviar(self):
        self.msg.email = self.inputEmail.text()
        self.msg.senha = self.inputSenha.text()

        if len(self.emails_para) < 0 or len(self.inputPara.text()) == 0:
            try:
                self.msg.enviar_email(self.inputDe.text(), self.inputPara.text(), self.inputAssunto.text())
                self.resposta.setText('Email enviado com sucesso!')
            except Exception as e:
                print(e)
                self.resposta.setText('Erro ao enviar Email!')
                return
        else:
            for v in self.emails_para:
                try:
                    self.msg.enviar_email(self.inputDe.text(), v, self.inputAssunto.text())
                    self.resposta.setText('Emails enviado com sucesso!')
                except Exception as e:
                    print(e)
                    self.resposta.setText(f'Erro ao enviar para o email: {v}')
                    return


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    interface_enviar_email = Interface_Enviar_Email()
    interface_enviar_email.show()
    qt.exec_()

'''
- Proxímos passos:

- Melhorar anexo do template.
- Fazer melhoria para que funcione tanto no linux quanto no windows.
- Revisão da V.1 do projeto.
- Fazer um executável e testar.
- Organizar estrutura de pastas do projeto.
- Organizar respositório remoto.
- Escrever readme.

-> Depois disso a V.1 do projeto vai está concluida, a partir daí é bom adicionar novas funcionalidades e melhorar
o layout.

- Adicionar função para enviar para vários emails.
- Adicionar banco de dados para controle.
- Melhorar layout.
- Fazer com que cada envio de email trabalhe em uma thread.
- Tentar adicionar uma navegação.
'''