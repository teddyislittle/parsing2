import requests
import img2pdf

def get_data():
    headers = {
        "Accept": "image/avif,image/webp,*/*",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0"
    }

    img_list = []
    for i in range(1, 49):
        url = f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            img_list.append(f"media/{i}.jpg")
            print(f"Downloaded {i} of 48")
    print('#' * 20)
    print(img_list)

    with open("final.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))
    print("File created")

def write_to_pdf():
    img_list2 = []
    for i in range(1, 49):
        img_list2.append(f"media/{i}.jpg")

    with open("final2verse.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list2))
    print("File created")

def mane():
    get_data()
    write_to_pdf()


if __name__ == '__main__':
    mane()