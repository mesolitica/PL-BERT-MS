from glob import glob
from huggingface_hub import HfApi
import os

api = HfApi()

files = glob('Checkpoint/*.t7')
files = sorted(files, key = lambda x: int(x.split('_')[1].replace('.t7', '')))

api.upload_file(
    path_or_fileobj=files[-1],
    path_in_repo=os.path.split(files[-1])[1],
    repo_id="mesolitica/PL-BERT-MS",
    repo_type="model",
)