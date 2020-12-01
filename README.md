# Benzema

Benzema is a minimal python3 bencoding library. It supports the most common
python data structures such as `int`, `str`, `dict`, `list` and even `bytes`.
It's perfect if you want to encode / decode data from `.torrent` files.


Why Benzema ? [Here's your answer](https://www.youtube.com/watch?v=erz5dB2IPbo)


### Installation

for pip

```sh
pip install benzema
```

for poetry

```sh
poetry add benzema
```


### Usage

```python

# decode
from benzema.decoder import Decoder
>>> data = Decoder(b'l7:Benzema8:Ben Arfa6:Mahrez5:Aouare').decode()
>>> data
>>> ["Benzema", "Ben Arfa", "Mahrez", "Aouar"]

# encode
from benzema.encoder import Encoder
>>> data = Encoder(["Benzema", "Ben Arfa", "Mahrez", "Aouar"]).encode()
>>> data
>>> b'l7:Benzema8:Ben Arfa6:Mahrez5:Aouare'
```


### Credits

Massive credits to the [unofficial BitTorrent specification](https://wiki.theory.org/BitTorrentSpecification) and to [Markus Eliasson](https://github.com/eliasson/) whose package `pieces` included an implementation that I referenced to get started.


### License
This project is distributed under the DO WHATEVER THE FUCK YOU PLEASE public
license.


### Tests

Tests can be run using the following command

```bash
pytest -vv -s tests/  # for verbosity and catching print statements
```

### Contributing

All contributions are welcome. If you see anything you think should be changed,
don't be shy and either open an issue or even better, submit a PR.
I'd be most happy to review them and collaborate with the community.
