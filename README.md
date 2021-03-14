# Scanner
Um scanner de rede simples. Ele está em uma versão bem nova, então não espere muito dele

## To-do
1. Listar IPs na rede
2. Comentar todo o código
3. Adicionar opção de regras (longo prazo)
4. Arrumar os erros
5. Adicionar a opção de instalar

## Como usar
```
$ python3 scanner.py help
```
Esse código mostrará a página de ajuda

```
$ python3 scanner.py install
```
Esse código instalará as dependências necessárias

## Exemplos
```
$ python3 scanner.py -a -p4 -h 127.0.0.1
```
Esse código realizará um scan em todas as portas do IP(v4) 127.0.0.1

```
$ python3 scanner.py -p4 -d 50 1 -h 127.0.0.1
```
Esse código realizará um scan nas primeiras 1000 portas do IP 127.0.0.1, pausando por 1 segundo a cada 50 portas
