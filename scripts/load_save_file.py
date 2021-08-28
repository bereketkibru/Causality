import dvc.api
import pandas as pd
import dvc.api
from f_logger import F_Logger


f_logger = F_Logger("load_save_file.log").get_f_logger()

def get_data(tag, Fpath, repo='https://github.com/bereketkibru/casualty.git'):
    rev = tag
    path=Fpath
    data_url = dvc.api.get_url(path=path, repo=repo, rev=rev)
    df = pd.read_csv(data_url)
    f_logger.info(f"Read data from {path}, version {tag}")
    return df

def save_csv(df, csv_path):
        try:
            df.to_csv(csv_path, index=False)
            print('File Successfully Saved.!!!')
            f_logger.info(f"File Successfully Saved to {csv_path}")

        except Exception:
            print("Save failed...")
            f_logger.error(f"saving failed")

        return df
