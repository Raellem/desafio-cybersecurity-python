# 🛡️ Simulação Educacional de Segurança em Python

<p align="center">
  ⚠️ <strong>AVISO: PROJETO ESTRITAMENTE EDUCACIONAL</strong> ⚠️
</p>

Este repositório contém scripts em Python que **simulam** o *comportamento* de malware (como ransomware e keyloggers) para fins de estudo e defesa.

**Nenhum código neste repositório é malicioso ou prejudicial.**

---

## 1. Propósito do Projeto

O objetivo deste projeto é **aprender e demonstrar**:
* Como a lógica de um ransomware (varredura e alteração de arquivos) funciona.
* Como um keylogger (conceitualmente) intercepta eventos.
* Como medidas de defesa (antivírus, firewalls, EDR) detectam esses comportamentos.
* A importância de práticas seguras (backups, menor privilégio, conscientização).

## 2. Sobre os Scripts

### Simulação de Ransomware (`ransomware_sim.py`)

* **O que faz:** O script percorre um diretório de *teste* específico (`/vitima_files`) e "criptografa" os arquivos.
* **O que NÃO faz (Por Segurança):**
    * Não usa criptografia real. Ele apenas **inverte o texto** dos arquivos.
    * Não se espalha pela rede.
    * Não apaga "shadow copies" ou tenta se esconder.

### Conceito do Keylogger

* (Se você incluir) Descreve a lógica de "hook" de teclado usando bibliotecas, mas foca em como o sistema operacional pode detectar essa atividade.

## 3. Como Usar com Segurança

1.  Clone este repositório.
2.  Crie um diretório de teste: `mkdir vitima_files`
3.  Adicione arquivos de texto de exemplo: `echo "teste 123" > vitima_files/doc1.txt`
4.  Execute o script de simulação: `python ransomware_sim.py`
5.  Observe os arquivos em `/vitima_files` serem alterados (texto invertido e extensão `.LOCKED`).
