<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Portfólio Pastel Amarelo</title>
  <style>
    /* Cores pastéis amarelas e decoração lilás */
    :root {
      --amarelo-pastel: #fff9db;
      --amarelo-pastel-escuro: #f7efb2;
      --texto-preto: #1a1a1a;
      --decoracao-lilas: #d9caff;
    }

    body {
      margin: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: var(--amarelo-pastel);
      color: var(--texto-preto);
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
      min-height: 100vh;
      box-sizing: border-box;
    }

    header {
      text-align: center;
      margin-bottom: 2rem;
      position: relative;
      max-width: 900px;
      width: 100%;
    }

    header h1 {
      font-size: 2.5rem;
      margin: 0.5rem 0 0 0;
      position: relative;
      display: inline-block;
      padding-bottom: 0.5rem;
    }

    /* Pequena decoração lilás clara embaixo do título */
    header h1::after {
      content: "";
      display: block;
      width: 60px;
      height: 5px;
      background-color: var(--decoracao-lilas);
      border-radius: 3px;
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
    }

    /* Mensagem de boas-vindas */
    #boas-vindas {
      font-size: 1.3rem;
      font-weight: 600;
      margin-bottom: 0.5rem;
    }

    #apresentacao {
      font-size: 1.1rem;
      margin-bottom: 2rem;
      max-width: 900px;
      width: 100%;
      text-align: center;
    }

    section {
      width: 100%;
      max-width: 900px;
      background-color: var(--amarelo-pastel-escuro);
      border-radius: 12px;
      padding: 2rem;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      margin-bottom: 2rem;
    }

    h2 {
      color: var(--texto-preto);
      margin-top: 0;
      margin-bottom: 1rem;
    }

    .projeto {
      background-color: var(--amarelo-pastel);
      border-radius: 8px;
      padding: 1rem;
      margin-bottom: 1.5rem;
      box-shadow: 0 2px 5px rgba(0,0,0,0.05);
      transition: transform 0.3s ease;
      cursor: pointer;
    }

    .projeto:hover {
      transform: scale(1.05);
      box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }

    .projeto h3 {
      margin: 0 0 0.5rem 0;
    }

    .projeto p {
      margin: 0;
    }

    /* Botão para mostrar/ocultar detalhes do projeto */
    .detalhes {
      margin-top: 0.5rem;
      font-size: 0.9rem;
      color: #333;
      display: none;
    }

    button {
      background-color: var(--decoracao-lilas);
      border: none;
      color: var(--texto-preto);
      padding: 0.4rem 0.8rem;
      border-radius: 5px;
      cursor: pointer;
      font-weight: 600;
      margin-top: 0.5rem;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #b3a3ff;
    }

    footer {
      margin-top: auto;
      font-size: 1rem;
      color: #555;
      text-align: center;
      max-width: 900px;
      width: 100%;
      padding: 1.5rem 0;
      border-top: 1px solid #ddd;
    }

    footer .redes {
      margin-bottom: 1rem;
    }

    footer .redes a {
      text-decoration: none;
      color: var(--texto-preto);
      font-weight: 600;
      margin: 0 1rem;
      transition: color 0.3s ease;
    }

    footer .redes a:hover {
      color: var(--decoracao-lilas);
    }

    #agradecimento {
      margin-top: 2rem;
      font-style: italic;
      font-weight: 600;
      color: var(--texto-preto);
      text-align: center;
    }

  </style>
</head>
<body>

  <header>
    <div id="boas-vindas">Seja bem vindo/a!</div>
    <h1>Meu Portfólio</h1>
  </header>

  <div id="apresentacao">
    <p>Oie, meu nome é Stefany, sou estudante de Python, e eu tenho 15.</p>
  </div>

  <section>
    <h2>Projetos</h2>

    <div class="projeto" onclick="toggleDetalhes(this)">
      <h3>Projeto 1: pyautogui</h3>
      <button>Mostrar detalhes</button>
      <p class="detalhes">O PyAutoGUI é uma biblioteca em Python usada para automação de interface gráfica (GUI). Com ela, você pode controlar o mouse e o teclado programaticamente, permitindo que scripts executem tarefas repetitivas, como clicar em botões, digitar texto, tirar screenshots, mover o cursor, entre outras ações.</p>
    </div>

    <div class="projeto" onclick="toggleDetalhes(this)">
      <h3>Projeto 2: API</h3>
      <button>Mostrar detalhes</button>
      <p class="detalhes">API é um conjunto de regras que permite que diferentes softwares se comuniquem entre si.</p>
    </div>

    <div class="projeto" onclick="toggleDetalhes(this)">
      <h3>Projeto 3: json</h3>
      <button>Mostrar detalhes</button>
      <p class="detalhes">JSON é um formato leve de texto para armazenar e trocar dados de forma simples e legível.</p>
    </div>
  </section>

  <div id="agradecimento">
    Obrigada por ter entrado no meu portfólio, beijoss e tchauuu!
  </div>

  <footer>
    <div class="redes">
      <a href="https://instagram.com/eu_stefany22" target="_blank" rel="noopener noreferrer" aria-label="Instagram">Instagram</a> |
      <a href="https://github.com/eustefany2" target="_blank" rel="noopener noreferrer" aria-label="GitHub">GitHub</a>
    </div>
    © 2025 Stefany
  </footer>

  <script>
    function toggleDetalhes(projetoDiv) {
      const detalhes = projetoDiv.querySelector('.detalhes');
      const botao = projetoDiv.querySelector('button');
      if (detalhes.style.display === 'block') {
        detalhes.style.display = 'none';
        botao.textContent = 'Mostrar detalhes';
      } else {
        detalhes.style.display = 'block';
        botao.textContent = 'Ocultar detalhes';
      }
    }
  </script>
