# PDI-2023.01
Primeiro Projeto da disciplina PDI

### Dependências
É necessário ter as seguintes dependencias:

opencv
matplotlib
Para isso, basta rodar no prompt os seguintes comandos:

pip install opencv-python
pip install matplotlib


## O que se espera
1. Conversão RGB-HSB-RGB (cuidado com os limites de R, G e B na volta!). Utilize
as conversões RGB->HSB e HSB->RGB descritas em
https://www.codeproject.com/Articles/19045/Manipulating-colors-in-NET-Part-1.
2. Alteração de matiz e saturação no HSB, com posterior conversão a RGB.
3. Negativo. Duas formas de aplicação devem ser testadas: em RGB (banda a banda) e
na banda V do HSV, com posterior conversão para RGB.
4. Correlação m x n com stride (passo), sobre R, G e B, com m, n, stride e filtro definidos
em um arquivo (txt) a parte. Teste com filtros Box e Sobel, e explicar os resultados.
Não utilize nenhum tipo de extensão. Compare Box15x1(Box1x15(imagem)) com
Box15x15(imagem), em termos de resultado e tempo de processamento. Para
visualização do Sobel, aplique valor absoluto seguido por expansão de histograma
para [0, 255].

### Informações importantes para executar o projeto
- Do 1 ao 3 esta no arquivo `main.py`. Ao executar o arquivo vai solicitar o nome do arquivo que deseja aplicar os filtros e o formato, lembrando que o arquivo precisa esta na pasta `/img`. Os resultados serão salvos nas pastas `output/q1`, `output/q2` ou `output/q3` de acordo com o numero da atividade.

- Na questão 2 pede "Alteração de matiz e saturação no HSB", têm duas maneiras de aplicar a alteração: alterando todo o valor da matiz, ou fazendo o grau da matiz "deslizar" de acordo com o parametro informado. O mesmo vale para a saturação.

- A questão 4 trata-se de correlação m x n com stride, para executar rode o arquivo `mainCorrelation.py`, vai solicitar o nome do arquivo que deseja aplicar as correlações e o formato. Esse código executa a correlação do filtro Box(média) e filtro Sobel informados nos arquivos `/kernel` nos formatos txt. Você pode alterar os valores deste arquivo se quiser mudar a dimensão da mascara ou do stride.



