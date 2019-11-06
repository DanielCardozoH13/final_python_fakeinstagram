from django.shortcuts import render

noticias = [
	{
		'titulo' : 'Universo 2020',
		'foto' : 'https://picsum.photos/200/200',
	},
	{
		'titulo' : 'Infraestructura 2020',
		'foto' : 'https://picsum.photos/200/200',
	},

]

# Create your views here.
def listar_noticias(request):
	return render(request,
	 'index.html', 
	 {'noticias': noticias})