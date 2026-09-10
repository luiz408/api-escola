from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):
    fixture = ['prototype_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='yes')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.get(pk=1)
        self.curso_02 = Curso.objects.get(pk=2)

    def test_requisicao_Delete_um_curso(self):
                        """Teste para requisição DELETE  um curso."""
    
                        response = self.client.delete(f"{self.url}1/")
                        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Verifica se o curso foi deletado com sucesso