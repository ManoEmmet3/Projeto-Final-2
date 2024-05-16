from django.http import HttpResponse

def index(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Academia</title>
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            <h1 class="mt-5">Bem-vindo à Academia</h1>
            <div class="mt-3">
                <a href="/instrutor" class="btn btn-primary btn-lg btn-block">Instrutores</a>
            </div>
            <div class="mt-3">
                <a href="/alunos" class="btn btn-success btn-lg btn-block">Alunos</a>
            </div>
            <div class="mt-3">
                <a href="/atividades" class="btn btn-danger btn-lg btn-block">Atividades</a>
            </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    </body>
    </html>
    """
    return HttpResponse(html_content)
