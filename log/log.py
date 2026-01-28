class Log:
    @staticmethod
    def red(mssg: str):
        print(f"\x1b[31m{mssg}\x1b[0m")

    @staticmethod
    def green(mssg: str):
        print(f"\x1b[32m{mssg}\x1b[0m")

    @staticmethod
    def blue(mssg: str):
        print(f"\x1b[34m{mssg}\x1b[0m")

    @staticmethod
    def magenta(mssg: str):
        print(f"\x1b[35m{mssg}\x1b[0m")

    @staticmethod
    def cyan(mssg: str):
        print(f"\x1b[36m{mssg}\x1b[0m")

    @staticmethod
    def teal(mssg: str):
        print(f"\x1b[33m{mssg}\x1b[0m")
