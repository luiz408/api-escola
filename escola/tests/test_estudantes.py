from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome="João da Silva",
            email="joao.silva@example.com",
            cpf="68195899056",
            data_nascimento="2000-01-01",
            numero_celular="86 99999-9999"
            
        )
        self.estudante_02 = Estudante.objects.create(
                    nome="João da Silva",
                    email="joao.silva@example.com",
                    cpf="12345678900",
                    data_nascimento="2000-01-01",
                    numero_celular="86 99999-9999"
                    
                )
        
        def test_requisicao_get_para_lista_estudantes(self):
            """Teste para verificar a requisição GET da lista de estudantes."""
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 2)  # Verifica se há 2 estudantes na resposta
            
        def test_requisicao_get_para_lista__um_estudante(self):
                """Teste para requisição GET 1 estudante."""
                response = self.client.get(self.url + '1/')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                dados_estudante = Estudante.objects.get(id=1)
                dados_serializados = EstudanteSerializer(dados_estudante).data
                self.assertEqual(response.data, dados_serializados)  # Verifica se os dados do estudante estão corretos
        def test_requisicao_Post_para_criar__um_estudante(self):
                """Teste para requisição POST para criar um estudante."""
                dados = {
                    "nome": "Maria da Silva",
                    "email": "maria.silva@example.com",
                    "cpf": "12345678901",
                    "data_nascimento": "2000-01-01",
                    "numero_celular": "86 99999-9999"
                }
                response = self.client.post(self.url, data=dados)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Verifica se o estudante foi criado com sucesso