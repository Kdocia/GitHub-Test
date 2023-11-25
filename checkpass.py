from hashlib import sha256

with open('pass.txt', 'r') as datapass:
    senha = datapass.read()


with open('criptoPass.txt', 'r') as datahash:
    cripto_senha = datahash.read()

#Pegar a hash em hexadecinaml da senha informada no txt
hash_senha = sha256(senha.encode()).hexdigest()

#Comparar as senhas:
if hash_senha == cripto_senha:
    print(f'A senha {senha} está correta ')
else:
    print(f'ERRO: A senha {senha} está incorreta')