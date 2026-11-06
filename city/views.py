
from django.http import HttpResponse


def page(title, content):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1">
        <title>{title}</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f0fbfa;
                color: #163c40;
            }}

            header {{
                background: linear-gradient(
                    120deg, #007f86, #25c6bd
                );
                color: white;
                text-align: center;
                padding: 55px 20px;
            }}

            header h1 {{
                font-size: 38px;
                margin-bottom: 12px;
            }}

            nav {{
                background: white;
                padding: 20px;
                text-align: center;
                box-shadow: 0 3px 12px #00000012;
            }}

            nav a {{
                display: inline-block;
                margin: 7px 12px;
                color: #007f86;
                text-decoration: none;
                font-weight: bold;
            }}

            nav a:hover {{
                color: #ff9800;
            }}

            main {{
                max-width: 1100px;
                margin: 45px auto;
                padding: 0 20px;
                text-align: center;
            }}

            .cards {{
                display: grid;
                grid-template-columns:
                    repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                margin-top: 35px;
            }}

            .card {{
                background: white;
                padding: 30px 20px;
                border-radius: 16px;
                box-shadow: 0 5px 20px #00000010;
                transition: 0.3s;
            }}

            .card:hover {{
                transform: translateY(-5px);
            }}

            .card h3 {{
                color: #008b8b;
            }}

            .button {{
                display: inline-block;
                background: #009d9d;
                color: white;
                padding: 12px 22px;
                border-radius: 9px;
                text-decoration: none;
            }}

            footer {{
                background: #07565c;
                color: white;
                text-align: center;
                padding: 25px;
                margin-top: 60px;
            }}
        </style>
    </head>

    <body>
        <header>
            <h1>Моє місто — Дніпро</h1>
            <p>Відкрий красу, історію та життя міста</p>
        </header>

        <nav>
            <a href="/">Головна</a>
            <a href="/news/">Новини</a>
            <a href="/management/">Керівництво</a>
            <a href="/facts/">Факти</a>
            <a href="/contacts/">Контакти</a>
            <a href="/history/">Історія</a>
            <a href="/history/people/">Відомі люди</a>
            <a href="/history/photos/">Фото</a>
        </nav>

        <main>
            <h2>{title}</h2>
            <p>{content}</p>

            <div class="cards">
                <div class="card">
                    <h3>📰 Новини</h3>
                    <p>Останні події нашого міста</p>
                    <a class="button" href="/news/">
                        Переглянути
                    </a>
                </div>

                <div class="card">
                    <h3>🏛️ Історія</h3>
                    <p>Дізнайся більше про минуле Дніпра</p>
                    <a class="button" href="/history/">
                        Переглянути
                    </a>
                </div>

                <div class="card">
                    <h3>📸 Фотографії</h3>
                    <p>Історичні світлини міста</p>
                    <a class="button" href="/history/photos/">
                        Переглянути
                    </a>
                </div>
            </div>
        </main>

        <footer>
            © 2026 Моє місто — Дніпро
        </footer>
    </body>
    </html>
    """)


def home(request):
    return page(
        "Ласкаво просимо!",
        "Дніпро — красиве місто з багатою історією."
    )


def news(request):
    return page(
        "Новини міста",
        "Тут розміщуватимуться новини Дніпра."
    )


def management(request):
    return page(
        "Керівництво міста",
        "Інформація про керівництво Дніпра."
    )


def facts(request):
    return page(
        "Цікаві факти",
        "Дніпро — велике місто на берегах річки Дніпро."
    )


def contacts(request):
    return page(
        "Контактні телефони",
        "Пожежна охорона — 101. "
        "Поліція — 102. Швидка допомога — 103."
    )


def history(request):
    return page(
        "Історія Дніпра",
        "Місто має багату історичну спадщину."
    )


def people(request):
    return page(
        "Відомі мешканці",
        "Тут буде інформація про відомих людей міста."
    )


def photos(request):
    return page(
        "Історичні фотографії",
        "Тут будуть історичні фотографії Дніпра."
    )
