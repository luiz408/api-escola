from webbrowser import get

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixture = ['prototype_banco.json']
    def setUp(self):

        #self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.usuario = User.objects.get(username='yes')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        #self.estudante_01 = Estudante.objects.create(
        #    nome="João da Silva",
        #    email="joao.silva@example.com",
        #    cpf="68195899056",
        #    data_nascimento="2000-01-01",
        #    numero_celular="86 99999-9999")
        self.estudante_01 = Estudante.objects.get(pk=1)

        #self.estudante_02 = Estudante.objects.create(
        #            nome="João da Silva",
        #            nome="João da Silva",
        #            email="joao.silva@example.com",
        #            cpf="12345678900",
        #            data_nascimento="2000-01-01",
        #            numero_celular="86 99999-9999"
                    
        #        )

        self.estudante_02 = Estudante.objects.get(pk=2)

        
        
        def test_requisicao_get_para_lista_estudantes(self):
            """Teste para verificar a requisição GET da lista de estudantes."""
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            #print(dados_estudantes_serializados) 
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

        def test_requisicao_Delete_um_estudante(self):
                    """Teste para requisição DELETE  um estudante."""

                    response = self.client.delete(f"{self.url}1/")
                    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Verifica se o estudante foi deletado com sucesso

        def test_requisicao_Put_para_atualizar_um_estudante(self):
                    """Teste para requisição PUT para atualizar um estudante."""
                    dados = {
                        "nome": "João da Silva Atualizado",
                        "email": "joao.silva.atualizado@example.com",
                        "cpf": "68195899056",
                        "data_nascimento": "2000-01-01",
                        "numero_celular": "86 99999-9999"
                    }
                    response = self.client.put(f"{self.url}1/", data=dados)
                    self.assertEqual(response.status_code, status.HTTP_200_OK)  # Verifica se o estudante foi atualizado com sucesso