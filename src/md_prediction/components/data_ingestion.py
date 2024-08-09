import os
import requests
import zipfile
from pathlib import Path
from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

def download_data(source_url: str, destination: Path) -> None:
    response = requests.get(source_url)
    response.raise_for_status()
    with open(destination, 'wb') as f:
        f.write(response.content)

def unzip_data(zip_file: Path, extract_to: Path) -> None:
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def prepare_data(config: DataIngestionConfig) -> None:
    config.unzip_dir.mkdir(parents=True, exist_ok=True)
    if not config.local_data_file.exists():
        download_data(config.source_URL, config.local_data_file)
    if not any(config.unzip_dir.iterdir()):
        unzip_data(config.local_data_file, config.unzip_dir)

