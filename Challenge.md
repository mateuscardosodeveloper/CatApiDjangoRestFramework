1. Levante um projeto usando FastAPI para construir uma API que tenha end-points para um
CRUD simples de raça gatos, com os seguintes atributos:
- Breed
- Location of origin
- Coat length
- Body type
- Pattern
2. A listagem de gatos deve ter a possibilidade de ser filtrada pelos atributos anteriores
3. Alguns casos de borda a serem testados (existem mais):
- Filtro de tamanho com valor negativo
- PATCH mudando a raça para um outro valor já existente
4. Documentação é importante, faça um README explicando sobre o seu projeto e como
funciona;
5. Faça com que seja possível inserir dados iniciais de 3 gatos utilizando apenas 1 comando;
6. (Opcional) Faça com que todo evento que aconteça na API, (como criação de uma raça de
gato);
seja publicado em um log. Alguns tipos podem ser: INFO, WARNING, ERROR, FATAL.
7. (Opcional) Se tiver background com docker e docker-compose, dickerize as aplicações e
crie um docker-compose que levante o serviço. Crie também um docker-compose específico
para rodar os testes;
8. (Opcional) O uso do Poetry é muito bem-vindo;
9. (Opcional) Commits atômicos e com mensagens significativas são um bom diferencial;
10. (Opcional) Aconselhamos o uso do pytest para os testes unitários pela sua facilidade de uso
e configuração. Lembrando que testes automatizados são obrigatórios;