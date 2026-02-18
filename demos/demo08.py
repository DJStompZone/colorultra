import fixpath
from colorultra import colorultra_text, Fore


def main():
    """automatically reset stdout"""
    with colorultra_text():
        print(Fore.GREEN + 'text is green')
        print(Fore.RESET + 'text is back to normal')

    print('text is back to stdout')

if __name__ == '__main__':
    main()
