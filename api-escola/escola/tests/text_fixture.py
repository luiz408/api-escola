from django.test import TestCase
from escola.models import Estudante, Curso


class TesteFixture(TestCase):
    fixture = ['prototico_banco.json']

    def text_carremento_fixture(self):
        """Teste para verificar se os dados da fixture foram carregados corretamente."""
        estudantes = Estudante.objects.get()
        cursos = Curso.objects.get()
        self.assertEqual(estudantes.numero_celular, "86 99999-9999")
        self.assertEqual(cursos.codigo, "")