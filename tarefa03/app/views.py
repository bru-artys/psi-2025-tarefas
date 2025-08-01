from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    lista_usuarios = [
        {'nome': 'Ana Silva', 'matricula': '20230001', 'idade': 22, 'cidade': 'São Paulo'},
        {'nome': 'Carlos Oliveira', 'matricula': '20230002', 'idade': 25, 'cidade': 'Rio de Janeiro'},
        {'nome': 'Mariana Santos', 'matricula': '20230003', 'idade': 20, 'cidade': 'Belo Horizonte'},
        {'nome': 'Pedro Costa', 'matricula': '20230004', 'idade': 23, 'cidade': 'Porto Alegre'},
        {'nome': 'Julia Pereira', 'matricula': '20230005', 'idade': 21, 'cidade': 'Recife'},
    ]
    return render(request, 'usuarios.html', {'usuarios': lista_usuarios})
