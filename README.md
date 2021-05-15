Minimal Dashboard to show manual escrow data

Live Site: http://tnbcrow.pythonanywhere.com/

### Local Development

Clone the repo.

Activate virtual environment.

Install the requirements.
```shell
pip install -r requirements.txt
```

Run migrations.
```shell
python manage.py migrate
```

Create Super User
```shell
python manage.py createsuperuser
```

Login to admin panel and add an entry in `Statistics` model.

Set the `debug=True` in `config/settings.py` if you want the static files to be loaded.

### Community
Join the community to stay updated on the most recent developments, project roadmaps, and random discussions about completely unrelated topics.

Discrod: https://discord.gg/F6JeuPtKRf

Twitter: https://twitter.com/tnbcrow

Facebook: https://www.facebook.com/tnbcorw

### Donate

All donations will go to thenewboston to help fund the team to continue to develop the community and create new content.

| Coin | Address |
|-|-|
| ![thenewboston Logo](https://github.com/thenewboston-developers/Website/raw/development/src/assets/images/thenewboston.png) | b6e21072b6ba2eae6f78bc3ade17f6a561fa4582d5494a5120617f2027d38797 |
| ![Bitcoin Logo](https://github.com/thenewboston-developers/Website/raw/development/src/assets/images/bitcoin.png) | 3GZYi3w3BXQfyb868K2phHjrS4i8LooaHh |
| ![Ethereum Logo](https://github.com/thenewboston-developers/Website/raw/development/src/assets/images/ethereum.png) | 0x0E38e2a838F0B20872E5Ff55c82c2EE7509e6d4A |