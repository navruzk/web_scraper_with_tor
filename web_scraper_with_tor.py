import requests
import os
import socket
import stem.process
import socks
from datetime import datetime


class Tor:
    @staticmethod
    def print_bootstrap_lines(line):
        if "Bootstrapped " in line:
            print(term.format(line, term.Color.BLUE))

    @classmethod
    def start_tor(cls):

        TOR_HOST = "127.0.0.1"
        TOR_SOCKS_PORT = 9050
        TOR_CONTROL_PORT = 9051

        tor_path = os.path.join(
            "C:\\Users\\Tor Browser\\Browser\\TorBrowser\\Tor", "tor.exe"
        )

        tor = stem.process.launch_tor_with_config(
            tor_cmd=tor_path,
            config={
                "SocksPort": str(TOR_SOCKS_PORT),
                "ControlPort": str(TOR_CONTROL_PORT),
            },
            init_msg_handler=cls.print_bootstrap_lines,
        )

        return True


if __name__ == "__main__":

    ## if tor is on, script closes it
    cmd = "taskkill /IM tor.exe /F"
    os.system(cmd)

    ## now it starts it again
    tor = Tor.start_tor()
    print("Tor started")

    ## sets default socket to 9050 port
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

    ## checks current IP
    print(requests.get("http://checkip.amazonaws.com/").text)

    ## imaginary scraper is working on some url
    url = ""
    scraper(url)
    ## scraper is not defined here
    ## any type of scraper can be constructed and replaced
