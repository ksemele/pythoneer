#!/usr/bin/env python3
import cmd
import os


def draw_map():
    print("this is map tmp...")


class Cli(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>> "
        self.intro = "Добро пожаловать\nДля справки наберите 'help'"
        self.doc_header = "Доступные команды (для справки по конкретной команде наберите 'help _команда_')"

    def do_show_disk(self, args):
        """show_disk - свободное место на диске"""
        os.system("df -h")

    def do_map(self, line):
        """show - showing map."""
        os.system("clear")
        draw_map()

    def do_exit(self, line):
        """exit - exit program."""
        print("Bye!")
        return True

    def default(self, line):
        os.system("clear")
        print(f'[{line}] Wrong command.')

    def emptyline(self):
        self.default("empty")


if __name__ == "__main__":
    cli = Cli()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print("завершение сеанса...")
