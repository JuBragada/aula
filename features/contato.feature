#language: pt
Funcionalidade: Envio de dados ao formulário
    Cenário: Envio de dados com assunto "Quero ser Facilitador"

    Como Usuário do site do Instituto Joga Junto
    Preciso preencher o formulário de contato
    Para enviar o formulário preenchido

    Dado que estou na página do Instituto Joga Junto
    Quando preenchido o formulário
    E aperto o botão para enviar
    Então o dado é recebido com sucesso
