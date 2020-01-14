#!/usr/bin/env python3

from cmd import Cmd
from subprocess import call

import json

from shuttle.providers.bitcoin.wallet import Wallet as BTCWallet
from shuttle.providers.bitcoin.htlc import HTLC as BTCHTLC
from shuttle.providers.bitcoin.transaction import FundTransaction as BTCFundTransaction
from shuttle.providers.bitcoin.solver import FundSolver as BTCFundSolver
from shuttle.providers.bytom.wallet import Wallet as BTMWallet
from shuttle.providers.bytom.htlc import HTLC as BTMHTLC
from shuttle.providers.bytom.transaction import FundTransaction as BTMFundTransaction
from shuttle.providers.bytom.solver import FundSolver as BTMFundSolver
from shuttle.utils import sha256


class Shell(Cmd):
    prompt = "\033[1;38m%s\033[1;0m\033[1;31m >\033[1;0m " % "shuttle"
    intro = "Welcome to the shuttle shell. Type help or ? to list commands.\n"

    def __init__(self):
        super().__init__()
        # Bitcoin and Bytom network
        self.btc_network, self.btm_network = None, None
        # Bitcoin and Bytom wallet
        self.btc_wallet, self.btm_wallet = None, None
        # Bitcoin and Bytom HTLC
        self.btc_htlc, self.btm_htlc = None, None
        # Bitcoin and Bytom fund transaction
        self.btc_fund_tx, self.btm_fund_tx = None, None
        # Bitcoin and Bytom claim transaction
        self.btc_claim_tx, self.btm_claim_tx = None, None
        # Bitcoin and Bytom refund transaction
        self.btc_refund_tx, self.btm_refund_tx = None, None
        # Bitcoin and Bytom fund solver
        self.btc_fund_solver, self.btm_fund_solver = None, None
        # Bitcoin and Bytom claim solver
        self.btc_claim_solver, self.btm_claim_solver = None, None
        # Bitcoin and Bytom refund solver
        self.btc_refund_solver, self.btm_refund_solver = None, None

    def set_network(self, args, currency):
        if args[2] == "mainnet":
            self.btc_network = "mainnet"
        elif args[2] == "testnet":
            self.btc_network = "testnet"
        elif args[2] == "solonet" and currency == "bytom":
            self.btc_network = "solonet"
        else:
            print("Invalid %s network." % args[2])
            return

    def set_wallet(self, args, currency):
        if args[2] in ["--passphrase", "--pass", "passphrase", "pass"] \
                and currency == "bitcoin":
            passphrase = args[3].split('"')[1].encode() \
                if len(args[3].split('"')) == 3 else args[3].encode()
            if passphrase:
                self.btc_wallet = BTCWallet(network=self.btc_network)\
                    .from_passphrase(passphrase=passphrase)
            else:
                print("No data found, passphrase is none.")
        elif args[2] in ["--private", "--prv", "private", "prv"] \
                and currency == "bitcoin":
            private_key = args[3].split('"')[2] \
                if len(args[3].split('"')) == 3 else args[3]
            if private_key:
                self.btc_wallet = BTCWallet(network=self.btc_network) \
                    .from_private_key(private_key=private_key)
            else:
                print("No data found, private key is none.")
        elif args[2] in ["--xprivate", "--xprv", "xprivate", "xprv"] \
                and currency == "bytom":
            xprivate_key = args[3].split('"')[2] \
                if len(args[3].split('"')) == 3 else args[3]
            if xprivate_key:
                self.btc_wallet = BTMWallet(network=self.btc_network) \
                    .from_xprivate_key(xprivate=xprivate_key)
            else:
                print("No data found, xprivate key is none.")
        elif args[2] in ["--mnemonic", "--mne", "mnemonic", "mne"] \
                and currency == "bytom":
            if len(args[3].split('"')) == 3:
                self.btc_wallet = BTMWallet(network=self.btc_network) \
                    .from_mnemonic(mnemonic=args[3].split('"')[1])
            else:
                print("Invalid mnemonic seed, mnemonic is none.")
        else:
            print("Set wallet error, only from passphrase or private key.")
            return

    def do_bitcoin(self, bitcoin: str):
        args = bitcoin.split(" ")
        if args[0] == "set":
            if len(args) not in [3, 4]:
                print("set needs 3 or 4 more agreement's")
                return
            if args[1] == "network":
                self.set_network(args, "bitcoin")
            elif args[1] == "wallet":
                self.set_wallet(args, "bitcoin")
        elif args[0] == "create":
            pass
        elif args[0] == "wallet":
            pass
        elif args[0] == "fund":
            pass
        elif args[0] == "claim":
            pass
        elif args[0] == "refund":
            pass

    def help_bitcoin(self):
        pass

    def do_bytom(self, bitcoin: str):
        args = bitcoin.split(" ")
        if args[0] == "set":
            if len(args) not in [3, 4]:
                print("set needs 3 or 4 more agreement's")
                return
            if args[1] == "network":
                self.set_network(args, "bytom")
            elif args[1] == "wallet":
                self.set_wallet(args, "bytom")
        elif args[0] == "create":
            pass
        elif args[0] == "wallet":
            pass
        elif args[0] == "fund":
            pass
        elif args[0] == "claim":
            pass
        elif args[0] == "refund":
            pass

    def help_bytom(self):
        pass

    @staticmethod
    def do_exit(_):
        print("Quit shuttle done.")
        return True

    @staticmethod
    def help_exit():
        print('Exit the shuttle application.')

    @staticmethod
    def do_add(inp=None):
        print("adding '{}'".format(inp))
        prompt = "Meheret"

    @staticmethod
    def help_add():
        print("Add a new entry to the system.")

    @staticmethod
    def do_clear(self):
        call("clear")

    @staticmethod
    def help_clear():
        print("To clear shell.")

    def default(self, inp):
        if inp in ["exit", "quit"]:
            return self.do_exit(inp)

        print("Default: {}".format(inp))

    do_EOF = do_exit
    help_EOF = help_exit
