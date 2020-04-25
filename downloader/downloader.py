import requests
from tqdm import tqdm

url = 'https://get.videolan.org/vlc/3.0.8/win64/vlc-3.0.8-win64.exe'
print('Start')
r = requests.get(url, allow_redirects=True, stream=True)
total_size = int(r.headers.get('content-length', 0))
block_size = 1024
t = tqdm(total=total_size, unit='b', unit_scale=True)

with open('vlc.exe', 'wb') as f:
    for data in r.iter_content(block_size):
        t.update(len(data))
        f.write(data)

t.close()
if total_size != 0 and t.n != total_size:
    print('ERROR, something went wrong')
