# Cryptocurrency icons from Coinmarketcap
Icon assets for cryptocurrencies 

<p float="left">
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/BTC.png" /> 
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/LTC.png" />
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/ETH.png" />
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/LINK.png" />
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/DOGE.png" />
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/XMR.png" />
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/NEO.png" />
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/TRX.png" />
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/FDUSD.png" />
    <img width="64px" src="https://raw.githubusercontent.com/IKTIKN/crypto-icons/main/output/icons/symbol/XRP.png" />
</p>

## Icons
As GitHub has a limit of 1000 files per folder, this repository contains only the top 100 icons from Coinmarketcap. Run the Python script to download all 9842 icons!

## Python3 script
Run the icon scraper to download all cryptocurrency icons from Coinmarketcap.

Clone this project to your local project folder:
```bash
  git clone https://github.com/IKTIKN/crypto-icons.git
```

Run the script

```bash
  cd crypto-icons/src
  python3 icon_scraper.py
```

### Output
This script generates an `output` folder with the following content: 
- Folder `icons` with subfolders `id`, `name` and `symbol`
- Json file named `icon_map.json`
#### Icons
Icons are stored as `.png` images and located in the `output/icons` folder. The script saves only unique filenames: The first occurence of `BTC.png` will be saved, skipping all other currencies who share the same name or symbol. The `id` folder contains all icons listed on Coinmarketcap. While the `name` and `symbol` folders contain only the unique filenames.


| Folder | Filename    | Unique |
|--------|-------------|-------|
| id     | 1.png       | 9842  |
| name   | Bitcoin.png | 9673  |
| symbol | BTC.png     | 8262  |

NOTE: The script downloads the largest pixelsize available: `128px`, `64px`, `32px` or `16px`. So not all icons share the same size. In rare cases a currency has no icon at all, these will be skipped.

#### Icon map
The icon map located at `output/icon_map.json` contains a list with all downloaded icons. Use this in your application to map unique Coinmarketcap id's to cryptocurrency names or symbols.
```json
[
    {
        "id": "1",
        "name": "Bitcoin",
        "symbol": "BTC"
    }
]
```
NOTE: The `name` and `symbol` values contain upper- and lowercase characters as provided by Coinmarketcap. If a value contains `/`, it will be replaced with `-`.
