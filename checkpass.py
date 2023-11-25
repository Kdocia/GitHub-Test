from hashlib import sha256

#Abre e realiza a leitura do arquivo txt fornecido pelo usuário
with open('pass.txt', 'r') as datapass:
    senha = datapass.read()

#Abre e realiza a leitura do arquivo txt que contem a hash da senha do usuário
with open('criptoPass.txt', 'r') as datahash:
    cripto_senha = datahash.read()

#Pegar a hash em hexadecinaml da senha informada no txt
hash_senha = sha256(senha.encode()).hexdigest()


#Comparar a senha fornecida pelo usuário com a senha armazenada:
'''if hash_senha == cripto_senha:
    print(f'A senha {senha} está correta ')
else:
    print(f'ERRO: A senha {senha} está incorreta')'''


#teste realizado pelo pytest
def test_answer():
    assert hash_senha == cripto_senha