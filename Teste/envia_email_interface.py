import sys
from PyQt5.QtWidgets import QApplication
from interface_email.interface_enviar_email import Interface_Enviar_Email

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    interface_enviar_email = Interface_Enviar_Email()
    interface_enviar_email.show()
    qt.exec_()
