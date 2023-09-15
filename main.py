import sys , requests , colorama
def main(fn,ln,dob):
    sc = ["","-","_"]
    glist = []
    for i in sc:
        for j in sc:
            gmail = f"{fn}{i}{ln}{j}{dob}@gmail.com"
            glist.append(gmail)
    return glist
def check(gmail):
    url = "https://mail.google.com/mail/gxlu?email=" + gmail + "&zx=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    r = requests.head(url)
    cc = str(r.cookies.get_dict())
    if "COMPASS" in cc :
        print(f"{colorama.Fore.GREEN}[+] {gmail} is valid :){colorama.Fore.RESET}")
    else:
        print(f"{colorama.Fore.RED}[-] {gmail} is not valid :({colorama.Fore.RESET}")

if __name__ == "__main__":
    colorama.init()
    if len(sys.argv) == 4 :
        gl = main(sys.argv[1],sys.argv[2],sys.argv[3])
        for gmail in gl:
            check(gmail=gmail)
    else:
        print(colorama.Fore.CYAN+"python3 main.py <FirstName> <LastName> <DateOfBirth"+colorama.Fore.RESET)

    
