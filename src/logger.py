import logging
from colorama import Fore, Style, init

init(autoreset=True)

def setup_logger():
    logger = logging.getLogger("ObfuscaX")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    class ColorFormatter(logging.Formatter):
        FORMATS = {
            logging.DEBUG: Fore.CYAN + "%(message)s" + Style.RESET_ALL,
            logging.INFO: Fore.GREEN + "%(message)s" + Style.RESET_ALL,
            logging.WARNING: Fore.YELLOW + "%(message)s" + Style.RESET_ALL,
            logging.ERROR: Fore.RED + "%(message)s" + Style.RESET_ALL,
            logging.CRITICAL: Fore.RED + Style.BRIGHT + "%(message)s" + Style.RESET_ALL,
        }
        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            return formatter.format(record)

    ch.setFormatter(ColorFormatter())
    logger.addHandler(ch)
    return logger
