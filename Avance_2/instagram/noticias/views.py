from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

noticias = [
	{
		'titulo': 'Politica 2019',
		'usuario': {
			'nombre': 'Alvaro Uribe Velez',
			'foto': 'https://picsum.photos/60/60/?image=1027',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'imagen': 'https://picsum.photos/200/200/?image=1036',
	},
	{
		'titulo': 'Universo 2020',
		'usuario': {
			'nombre': 'Nasa',
			'foto': 'https://picsum.photos/60/60/?image=1005',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'imagen': 'https://picsum.photos/200/200/?image=903',
	},
	{
		'titulo': 'Infraestructura 2020',
		'usuario': {
			'nombre': 'Charles Chaplin',
			'foto': 'https://picsum.photos/60/60/?image=883',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'imagen': 'https://picsum.photos/200/200/?image=1076',
	},
]

# Create your views here.}
@login_required
def listar_noticias(request):
	return render(request, 'noticias/noticias.html', {'noticias':noticias})
