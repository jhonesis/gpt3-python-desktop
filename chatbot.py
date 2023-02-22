# utf-8 encoded

# Importar la biblioteca PyQt5
from PyQt5 import QtWidgets

# Importar la biblioteca openai
import openai

# Establecer la clave de API de GPT-3
openai.api_key = "aqui va tu api key"


class GPT3Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Crear un cuadro de texto donde el usuario pueda escribir una pregunta
        self.question_input = QtWidgets.QLineEdit(self)
        # Crear un boton para enviar la pregunta a GPT-3
        self.submit_button = QtWidgets.QPushButton("Enviar", self)
        # Crear un cuadro de texto donde se mostrara la respuesta de GPT-3
        self.answer_output = QtWidgets.QTextEdit(self)

        # Conectar el evento de hacer clic en el bot�n con una funci�n para enviar la pregunta a GPT-3
        self.submit_button.clicked.connect(self.submit_question)

        # Crear un diseno para organizar los widgets en la ventana
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.question_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.answer_output)
        self.setLayout(layout)

        # Establecer el titulo de la ventana y mostrarla
        self.setWindowTitle("GPT-3 Chat")
        self.resize(500, 300)
        self.show()

    def submit_question(self):
        # Obtener la pregunta del cuadro de texto de entrada
        question = self.question_input.text()

        # Enviar la pregunta a GPT-3 y obtener una respuesta
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=["?"],
        )

        # Mostrar la respuesta de GPT-3 en el cuadro de texto de salida
        self.answer_output.setText(response["choices"][0]["text"])


# Crear una instancia de la ventana y ejecutar el script
app = QtWidgets.QApplication([])
window = GPT3Window()
app.exec_()