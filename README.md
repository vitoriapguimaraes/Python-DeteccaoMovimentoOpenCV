# Detecção e Contagem de veículos com OpenCV

> Projeto de visão computacional para detecção e contagem automática de veículos em vídeos de tráfego, utilizando técnicas de subtração de fundo e processamento de imagens com OpenCV.

![Demonstração do sistema](https://github.com/vitoriapguimaraes/Python-DeteccaoMovimentoOpenCV/blob/main/results/display.gif)

## Funcionalidades Principais

- Detecção automática de veículos em movimento em vídeos.
- Contagem de veículos que cruzam uma linha de interesse (ROI).
- Suporte a múltiplos algoritmos de subtração de fundo (KNN, MOG, MOG2, GMG, CNT).
- Visualização em tempo real dos resultados com marcação dos veículos detectados.

## Tecnologias Utilizadas

- Python 3
- OpenCV (opencv-python, opencv-contrib-python)
- Numpy

## Como Executar

1. Clone o repositório:
2. Instale as dependências:
   ```
   pip install opencv-contrib-python numpy
   ```
3. Execute o projeto:
   ```
   python scripts/main.py
   ```

## Como Usar

- Certifique-se de que o vídeo desejado está na pasta `dataset/`.
- Por padrão, o script utiliza o vídeo `Ponte.mp4`. Para trocar, altere a variável `VIDEO_PATH` em `scripts/main.py`.
- O resultado será exibido em uma janela, mostrando a contagem de veículos em tempo real.
- Pressione `ESC` para encerrar a execução.

## Estrutura de Diretórios

```
/Python-VisaoComputacionalDeteccaoMovimentoOpenCV
├── class_files/         # Scripts das aulas e imagens geradas
├── dataset/             # Vídeos de entrada
├── scripts/             # Código principal do projeto
│   └── main.py
└── README.md
```

## Status

- ✅ Concluído

> Veja as [issues abertas](https://github.com/vitoriapguimaraes/Python-DeteccaoMovimentoOpenCV/issues) para sugestões de melhorias e próximos passos.

## Mais Sobre Mim

Acesse os arquivos disponíveis na [Pasta Documentos](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.
