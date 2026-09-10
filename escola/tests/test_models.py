from django.test import TestCase
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class ModelEstudanteTestCase(TestCase):
    # def test_falha(self):
    #    self.fail("Teste de falha intencional para verificar a execução dos testes.")
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome="João da Silva",
            email="joao.silva@example.com",
            cpf="68195899056",
            data_nascimento="2000-01-01",
            numero_celular='86 99999-9999'
        )
        self.serializer_estudante = EstudanteSerializer(self.estudante)
        self.serialized_estudante = EstudanteSerializer(self.estudante)
    
    def test_estudante_str(self):
        """Teste para verificar o modelo Estudante."""
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_celular']))
    def test_verificar_campos(self):
        """Teste para verificar os campos do modelo Estudante."""
        dados = self.serialized_estudante.data
        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['email'], self.estudante.email)
        self.assertEqual(dados['cpf'], self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(dados['numero_celular'], self.estudante.numero_celular)