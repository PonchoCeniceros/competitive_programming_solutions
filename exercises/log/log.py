class Log:
    def red(self, mssg: str):
        print(f"\x1b[31m{mssg}\x1b[0m")

    def green(self, mssg: str):
        print(f"\x1b[32m{mssg}\x1b[0m")

    def blue(self, mssg: str):
        print(f"\x1b[34m{mssg}\x1b[0m")

    def magenta(self, mssg: str):
        print(f"\x1b[35m{mssg}\x1b[0m")

    def cyan(self, mssg: str):
        print(f"\x1b[36m{mssg}\x1b[0m")

    def teal(self, mssg: str):
        print(f"\x1b[33m{mssg}\x1b[0m")
