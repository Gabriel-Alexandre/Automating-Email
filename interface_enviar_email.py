import sys
from email_class_teste import EmailClass
from interface import Ui_MainWindow
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
        self.msg = EmailClass()

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

    def enviar(self):
        self.msg.email = self.inputEmail.text()
        self.msg.senha = self.inputSenha.text()
        try:
            self.msg.enviar_email(self.inputDe.text(), self.inputPara.text(), self.inputAssunto.text())
            self.resposta.setText('Enviado com sucesso!')
        except Exception as e:
            print(e)
            self.resposta.setText('Erro ao enviar Email!')
            return


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    interface_enviar_email = Interface_Enviar_Email()
    interface_enviar_email.show()
    qt.exec_()

'''
- Proxímos passos:

- Adicionar a funcionalidade possibilitando manda para diferente emails e suas implicações.
-> (Resolver problema de quando a lista de emails é adicionada, ele manda apenas para um email).
- Fazer a preparação usando o "requiriments.txt".
- Escrever documentação, possibilitando execução no linux e no windows.
'''