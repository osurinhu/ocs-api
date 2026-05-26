# Api ocs

## Como rodar o projeto
- Entre na vpn do chefe
- Encaminhe a porta 3306 do servidor do banco a porta 3333 do seu pc 
```
ssh -L 127.0.0.1:3333 usuario@ipbanco:3306
```
- Crie o venv
```
python -m venv ./venv
```
- Instale as dependencias
```
pip install -r requirements.txt
```
- Entre na pasta app
```
cd app
```
- Inicie a api
```
flask run
```

## Swagger
O swagger esta no endpoint 
``
/api/v1/
``
