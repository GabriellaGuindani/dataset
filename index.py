import os
import requests
import zipfile

dataset_url = "https://dacl10k.s3.eu-central-1.amazonaws.com/dacl10k-challenge/dacl10k_v2_devphase.zip"
dataset_path = "dataset-devphase.zip"
extracted_path = "dataset-devphase"

# Verifica se o arquivo já foi baixado
if not os.path.exists(dataset_path) or not os.path.exists(extracted_path):
    print("Dataset não encontrado, baixando...")
    response = requests.get(dataset_url, stream=True)
    with open(dataset_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Download completo!")

# Verifica se o arquivo foi descompactado
if not os.path.exists(extracted_path):
    print("Descompactando o dataset...")
    with zipfile.ZipFile(dataset_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_path)
    print("Descompactação completa!")

print("Indexação completa!")