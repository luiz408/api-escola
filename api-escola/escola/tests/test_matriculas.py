from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class MatriculasTestCase(APITestCase):
    fixture = ['prototype_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='yes')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.get(pk=1)
        self.curso = Curso.objects.get(pk=1)
        self.matricula = Matricula.objects.get(pk=1)
            

    def test_requisicao_Delete_uma_matricula(self):
        """Teste para requisição DELETE  uma matrícula."""
        response = self.client.delete(f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED) 