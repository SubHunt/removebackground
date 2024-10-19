# 1. Плохо удаляет фон
# from rembg import remove
# from PIL import Image
#
# input_path = './test.jpg'
# output_path = './test.png'
#
# input = Image.open(input_path, mode='r')
# output = remove(input)
# output.save(output_path)

# 2. Удаление фона через сервисы по API
import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_ACETONE = os.getenv("API_ACETONE")
API_PHOTOROOM = os.getenv("API_PHOTOROOM")


def ask_acetone(img_path: str):
    with open(img_path, 'rb') as file:
        return requests.post(
            # ACETONE
            url='https://api.acetone.ai/api/v1/remove/background?format=png',
            files={
                'image': (img_path, file.read()),
            },
            headers={'Token': API_ACETONE}

            # PHOTOROOM
            # url='https://sdk.photoroom.com/v1/segment',
            # files={'image_file': file},
            # headers={'Token': 'sandbox_5e2e60196078fd35e978100522414e24039c6728'}
            # headers={
            #     "Accept": "image/jpg, application/json",
            #     "x-api-key": API_PHOTOROOM,
            # }
        )



for filename in os.listdir('input'):
    print(f'Обрабатываем файл {filename}')
    ans = ask_acetone('./input/' + filename)

    if ans.headers['content-type'] in ('image/png', 'image/webp', 'image/jpeg'):
        with open('./output/' + filename[:-4] + '.png', 'wb') as file:
            file.write(ans.content)
    else:
        print(ans.json())


