# -*- coding: utf-8 -*-

from flask import Flask, render_template_string

# Inicializa a aplicação Flask
app = Flask(__name__)


PORTFOLIO_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kirlian | Portfólio em Flask </title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0a192f;
            color: #ccd6f6;
        }
        .glass-effect {
            background: rgba(23, 49, 85, 0.4);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .highlight {
            color: #64ffda;
        }
        .section-heading {
            color: #ccd6f6;
        }
    </style>
</head>
<body class="antialiased">
    <div class="container mx-auto max-w-4xl px-6 py-12">

        <!-- Seção de Introdução -->
        <header class="mb-16 md:mb-24 text-center md:text-left">
            <span class="text-2xl highlight font-mono mb-1 block">Olá, meu nome é Kirlian Kitzinger d'Avila</span>
            <h6 class="text-1xl md:text-1xl font-bold text-slate-400 mt-2">Eu sou estudante de Engenharia de Controle e Automação, pelo Instituto Federal de São Paulo, e interessado em contribuir com a inovação.</h6>
            <p class="mt-6 max-w-xl mx-auto md:mx-0 text-slate-400">
                Sou um desenvolvedor Python apaixonado por criar tecnologia eficiente, escalável e animado para contribuir com a inovação <span class="font-bold">Projeto Alpha</span>.
            </p>
            <a href="#projects" class="mt-8 inline-block bg-transparent border-2 border-[#64ffda] text-[#64ffda] font-medium py-3 px-8 rounded-md hover:bg-[#64ffda] hover:text-[#0a192f] transition-all duration-300">
                Veja meus projetos
            </a>
        </header>

        <main>
            <!-- Seção "Por que a CodeLeap?" -->
            <section id="why-codeleap" class="mb-16 md:mb-24">
                <div class="glass-effect p-6 rounded-lg">
                    <p class="text-slate-400 leading-relaxed">
                        Meu Nome é Kirlian, e sou um desenvolvedor Python/java com conhecimento em Django, Flask e React. Tenho uma paixão por criar soluções eficientes e escaláveis para a web. 
                        Sou Interessado em Automação e Programação. Podendo ser programador, Analista de Dados ou Engenharia de Automação.
                    </p>
                </div>
            </section>

            <!-- Seção de Habilidades -->
            <section id="skills" class="mb-16 md:mb-24">
                <h2 class="text-2xl md:text-3xl font-bold section-heading mb-6 flex items-center">
                    <span class="text-xl md:text-2xl highlight font-mono mr-3">02.</span> Minhas Habilidades
                    <span class="flex-grow h-px bg-slate-700 ml-4"></span>
                </h2>
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 font-mono text-sm">
                    <div class="flex items-center space-x-2 p-2 rounded"><span class="highlight">✓</span><span>Python</span></div>
                    <div class="flex items-center space-x-2 p-2 rounded"><span class="highlight">✓</span><span>Django</span></div>
                    <div class="flex items-center space-x-2 p-2 rounded"><span class="highlight">✓</span><span>Flask</span></div>
                    <div class="flex items-center space-x-2 p-2 rounded"><span class="highlight">✓</span><span>APIs</span></div>
                    <div class="flex items-center space-x-2 p-2 rounded"><span class="highlight">✓</span><span>Git & GitHub</span></div>
                    <div class="flex items-center space-x-2 p-2 rounded"><span class="highlight">✓</span><span>SQL (PostgreSQL)</span></div>
                    <div class="flex items-center space-x-2 p-2 rounded"><span class="highlight">✓</span><span>Java</span></div>
                    <div class="flex items-center space-x-2 p-2 rounded"><span class="highlight">✓</span><span>AWS (básico)</span></div>
                </div>
            </section>

            <!-- Seção de Projetos -->
            <section id="projects" class="mb-16 md:mb-24">
                 <h2 class="text-2xl md:text-3xl font-bold section-heading mb-8 flex items-center">
                    <span class="text-xl md:text-2xl highlight font-mono mr-3">03.</span> Projetos Relevantes
                    <span class="flex-grow h-px bg-slate-700 ml-4"></span>
                </h2>
                <div class="space-y-12">
                    <!-- Projeto 1 -->
                    <div class="grid grid-cols-1 md:grid-cols-5 gap-6 items-center">
                        <div class="md:col-span-3 text-left">
                            <h3 class="text-xl font-bold text-slate-200 hover:text-highlight transition-colors"><a href="LINK_PARA_SEU_PROJETO_1" target="_blank">Teste</a></h3>
                            <div class="glass-effect my-4 p-6 rounded-lg shadow-lg">
                                <p class="text-slate-400">
                                    Uma API RESTful construída com Django e Django REST Framework. Permite criar, listar, atualizar e deletar tarefas.
                                    Ideal para demonstrar conhecimento em desenvolvimento de backend, modelagem de dados e criação de endpoints.
                                </p>
                            </div>
                            <div class="flex flex-wrap gap-2 font-mono text-xs">
                                <span class="bg-slate-800 text-highlight px-2 py-1 rounded-full">Python</span>
                                <span class="bg-slate-800 text-highlight px-2 py-1 rounded-full">Django</span>
                                <span class="bg-slate-800 text-highlight px-2 py-1 rounded-full">DRF</span>
                                <span class="bg-slate-800 text-highlight px-2 py-1 rounded-full">PostgreSQL</span>
                            </div>
                        </div>
                        <div class="md:col-span-2">
                             <a href="LINK_PARA_SEU_PROJETO_1" target="_blank" class="block bg-slate-800 rounded-lg p-4 border-2 border-slate-700 hover:border-highlight transition-all">
                                <img src="https://placehold.co/600x400/0a192f/64ffda?text=API+Project" alt="Preview do Projeto 1" class="rounded-md w-full">
                            </a>
                        </div>
                    </div>

                    <!-- Projeto 2 -->
                    <div class="grid grid-cols-1 md:grid-cols-5 gap-6 items-center">
                         <div class="md:col-span-2">
                             <a href="LINK_PARA_SEU_PROJETO_2" target="_blank" class="block bg-slate-800 rounded-lg p-4 border-2 border-slate-700 hover:border-highlight transition-all">
                                <img src="https://placehold.co/600x400/0a192f/64ffda?text=AI+Chatbot" alt="Preview do Projeto 2" class="rounded-md w-full">
                            </a>
                        </div>
                        <div class="md:col-span-3 text-right">
                            <h3 class="text-xl font-bold text-slate-200 hover:text-highlight transition-colors"><a href="LINK_PARA_SEU_PROJETO_2" target="_blank">Teste</a></h3>
                             <div class="glass-effect my-4 p-6 rounded-lg shadow-lg">
                                <p class="text-slate-400">
                                    Um bot para Slack que utiliza processamento de linguagem natural (NPL) para agendar reuniões e criar lembretes. Inspirado no Projeto Alpha, demonstra habilidade com integrações de API e um mindset orientado a soluções.
                                </p>
                            </div>
                            <div class="flex flex-wrap gap-2 justify-end font-mono text-xs">
                                <span class="bg-slate-800 text-highlight px-2 py-1 rounded-full">Python</span>
                                <span class="bg-slate-800 text-highlight px-2 py-1 rounded-full">Slack API</span>
                                <span class="bg-slate-800 text-highlight px-2 py-1 rounded-full">NLTK</span>
                                <span class="bg-slate-800 text-highlight px-2 py-1 rounded-full">AWS Lambda</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Seção de Contato -->
            <section id="contact" class="text-center mt-16 md:mt-24">
                <h2 class="text-2xl font-bold section-heading mb-2">Entre em Contato</h2>
                <p class="text-slate-400 max-w-lg mx-auto mb-8">
                    Estou sempre aberto a novos desafios e oportunidades.
                    Seja para falar sobre a vaga ou qualquer outra coisa, meu inbox está sempre aberto!
                    <p>email: kirliankitzinger@gmail.com</p>
                    <p>Phone/Whatsapp: +55 11 98436-1909</p>

                <div class="flex justify-center space-x-6">
                    <a href="mailto:seu-email@dominio.com" class="bg-highlight text-[#0a192f] font-bold py-3 px-8 rounded-md hover:opacity-90 transition-opacity">
                        Enviar E-mail
                    </a>
                    <a href="https://github.com/seu-usuario" target="_blank" class="text-highlight py-3 px-4 rounded-md hover:bg-slate-800 transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                    </a>
                     <a href="https://linkedin.com/in/seu-usuario" target="_blank" class="text-highlight py-3 px-4 rounded-md hover:bg-slate-800 transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                    </a>
                </div>
            </section>
        </main>

        <footer class="text-center mt-20 text-slate-500 text-sm font-mono">
            <p>Desenvolvido com Python & Flask.</p>
        </footer>

    </div>
</body>
</html>
"""

# Define a rota principal da aplicação
@app.route('/')
def portfolio():
    # Renderiza o template HTML diretamente da string
    return render_template_string(PORTFOLIO_TEMPLATE)


