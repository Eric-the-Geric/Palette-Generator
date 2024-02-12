class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[40m'
    OKCYAN = '\033[41m'
    OKGREEN = '\033[42m'
    WARNING = '\033[93m'
    BG = '\033[47m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"""
{bcolors.BG}     {bcolors.ENDC}
{bcolors.OKGREEN}     {bcolors.ENDC}
{bcolors.OKCYAN}     {bcolors.ENDC}
{bcolors.OKBLUE}     {bcolors.ENDC}
""")
