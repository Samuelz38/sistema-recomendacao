import requests

import os

def getFilepathFromURL(url: str, game_name: str) -> str:

  response = requests.get(url=url)

  if response.status_code == 200:

    data: bytes = response.content

    images_dirpath: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                      "static", 
                                      "images")
    
    
    # Remove todas as imagens de static/images, caso a quantidade for maior que 10
    if len(os.listdir(images_dirpath)) > 10:
           
      for filename in os.listdir(images_dirpath):
                  
        os.remove(os.path.join(images_dirpath, filename))

    filepath: str = os.path.join(images_dirpath, f"{game_name}.png")

    if data:
      
      if not os.path.isfile(filepath):

        with open(filepath, "wb") as file_stream:

          file_stream.write(data)
      
      return filepath

    return ""