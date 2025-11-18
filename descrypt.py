import os
from cryptography.fernet import Fernet

# 1. LER a chave gerada anteriormente
# Nota: Diferente do ransomware, aqui a gente só LÊ (rb), não gera uma nova.
with open("chave.key", "rb") as key_file:
    key = key_file.read()

# 2. Definir quais arquivos vamos resgatar
files = []
for file in os.listdir():
    # Ignorar os scripts e a chave
    if file == "ransomware.py" or file == "chave.key" or file == "decrypt.py":
        continue 
    if os.path.isfile(file):
        files.append(file)

print(f"Arquivos para descriptografar: {files}")

# 3. Descriptografar (O Resgate)
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    
    # A mágica acontece aqui: .decrypt em vez de .encrypt
    contents_decrypted = Fernet(key).decrypt(contents)
    
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

print("SEUS ARQUIVOS FORAM RESTAURADOS COM SUCESSO!")
