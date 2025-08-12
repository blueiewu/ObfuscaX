import random
import base64
import logging

logger = logging.getLogger("ObfuscaX")

def random_variable_name(length=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(chars) for _ in range(length))

def base64_encode(data):
    if isinstance(data, bytes):
        data = data.decode(errors='ignore')
    encoded = base64.b64encode(data.encode()).decode()
    logger.debug("Base64 encoding applied.")
    return encoded

def xor_encode(data, key=0x42):
    if isinstance(data, bytes):
        data = data.decode(errors='ignore')
    encoded = ''.join(chr(ord(c) ^ key) for c in data)
    logger.debug(f"XOR encoding applied with key {key}.")
    return encoded

def insert_junk_code_ps1(script):
    junk_statements = [
        'Write-Verbose "Junk statement..."',
        '$junkVar = Get-Date',
        'Start-Sleep -Milliseconds 10',
        'For ($i=0; $i -lt 5; $i++) { $null = $i }',
        '# Random comment'
    ]
    junk_code = '\n'.join(random.choices(junk_statements, k=3))
    logger.debug("Inserted junk PowerShell code.")
    return junk_code + "\n" + script

def static_obfuscate(payload):
    logger.info("Starting static obfuscation...")
    # Assuming payload is PowerShell script as string
    if isinstance(payload, bytes):
        payload = payload.decode(errors='ignore')
    
    # Rename variables - simplistic approach
    # For demo, replace $payloadVar with a random name
    old_var = "$payloadVar"
    new_var = "$" + random_variable_name()
    payload = payload.replace(old_var, new_var)

    # Base64 encode payload
    payload = base64_encode(payload)

    # Wrap with powershell base64 execution wrapper
    obf_script = f"powershell -EncodedCommand {payload}"

    # Add junk code (only if Powershell)
    obf_script = insert_junk_code_ps1(obf_script)

    logger.info("Static obfuscation complete.")
    return obf_script.encode()
