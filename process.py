import requests


def processing_user_data(username: str, reponame: str):

    try:
        url = f"https://api.github.com/repos/{username}/{reponame}"
        r = requests.get(url, timeout=10)

        # Kiem tra ton tai STATUS CODE 404
        if r.status_code == 404:
            return "Repository hoac username khong ton tai"

        # Kiem tra phan hoi STATUS CODE 200
        if r.status_code != 200:
            return f"Loi API Github: {r.status_code}"

        data = r.json()

        kb = data["size"]
        mb = kb / 1024
        gb = mb / 1024

        return f"Size: {kb} KB | {mb:.2f} MB | {gb:.2f} GB"

    # Kiem tra ket noi
    except requests.exceptions.RequestException as e:
        return f"Loi ket noi: {e}"