from django.test import TestCase
from escola.models import Estudante
from escola.serializers import EstudanteSerializer
class EstudanteSerializerTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome="João da Silva",
            email="joao.silva@example.com",
            cpf="68195899056",
            data_nascimento="2000-01-01",
            numero_celular="86 99999-9999"
        )
        self.serializer = EstudanteSerializer(instance=self.estudante)  
        
    def test_serializer_fields(self):
        """Teste para verificar os campos do serializer EstudanteSerializer."""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_celular']))
        