User
import sys
import requests
def main():
    link = sys.argv[1]
    try:
        with open("admin.txt", "r") as files:
            for url in files.read().splitlines():
                urls = link+url
               # print(f"\033[31m{urls}\033[0m")
                request = requests.get(urls)
                if request.status_code == 200:
                        print(f"\033[32m{urls}    {request.status_code} OK\033[0m")
                else:
                    print(f"{urls}   \033[31m{request.status_code} NOT FOUN\033[0m")
    except FileNotFoundError:
        print(f"The file {urls} was not found.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    main()