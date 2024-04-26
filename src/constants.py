# Dict keys
KEY_API                 = "api_key"
KEY_DATA                = "data"
KEY_FIRST_HIST_DATA     = "first_historical_data"
KEY_ID                  = "id"
KEY_IS_ACTIVE           = "is_active"
KEY_LAST_HIST_DATA      = "last_historical_data"
KEY_NAME                = "name"
KEY_PLATFORM            = "platform"
KEY_RANK                = "rank"
KEY_SLUG                = "slug"
KEY_SYMBOL              = "symbol"

# Coinmarketcap connection
CMC_BASE_URL            = "https://pro-api.coinmarketcap.com{}"
CMC_ICON_URL            = "https://s2.coinmarketcap.com/static/img/coins/{size}x{size}/{id}.png"
CMC_MAP_ENDPOINT        = "/v1/cryptocurrency/map"
CMC_PRO_API_KEY         = "X-CMC_PRO_API_KEY"
HTTP_SESSION_HEADER     = {"Accepts": "application/json", CMC_PRO_API_KEY: ""}

# Directories
DIR_OUTPUT              = "../output"
DIR_ICONS               = "{}/icons".format(DIR_OUTPUT)
DIR_ICONS_ID            = "{}/id".format(DIR_ICONS)
DIR_ICONS_NAME          = "{}/name".format(DIR_ICONS)
DIR_ICONS_SYMBOL        = "{}/symbol".format(DIR_ICONS)

# Filepaths
PATH_CONFIG_JSON        = "../config.json"
PATH_ICON_MAP_JSON      = "{}/icon_map.json".format(DIR_OUTPUT)
PATH_ICON_PNG           = "{}/{}.png"

# Log strings
STRING_API_KEY_INPUT    = "Enter CoinMarketCap api key: "
STRING_CONFIG_SAVED     = "Saved api key in: {}"
STRING_DOWNLOAD_MAP     = "\n[+] Downloading cryptocurrency map from Coinmarketcap\n"
STRING_EXIT             = "\nExit"
STRING_NO_ICON          = "[!] {} ({}) -> {}\n"
STRING_PERCENT          = "{:3.2f}%"
STRING_PROGRESS         = f"{'{:>8}'} {'{:>8}'} {'{:<14}'} {'{:<20}'}"
STRING_SCRAPE_TITLE     = "[+] Scraping icons from Coinmarketcap\n\n{}".format(STRING_PROGRESS.format("Progress", "ID", "SYMBOL", "NAME"))
STRING_SCRAPER_STATS    = "\nDownloaded {} icons ({:.2f}/second)\nRuntime: {}"
STRING_SKIPPED_ICONS    = "\nSkipped {} icons ({})"

# Exception messages
EXCEPTION_CMC_MAP       = "Unable to download icon id map from Coinmarketcap.\nRequest URL: {}".format(CMC_BASE_URL.format(CMC_MAP_ENDPOINT))
EXCEPTION_DEFAULT       = "\n[!] Something went wrong...\n{}"
EXCEPTION_HTTP          = "[!] HTTP {} -> {}"
EXCEPTION_HTTP_401      = "[!] HTTP 401 Unauthorized -> '{}' is not a valid API key"
EXCEPTION_NETWORK       = "Network error: {}"

# App startup header
HEADER_BITCOIN          = "\n".join([
"\n\n⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀ ",
"⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀ ",
"⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀",
"⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠟⠿⠿⡿⠀⢰⣿⠁⢈⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀",
"⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⠀⠀⠀⠈⠉⠀⠸⠿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀",
"⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⢠⣶⣶⣤⡀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⡆",
"⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠼⣿⣿⡿⠃⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷     Icon scraper in Python.",
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢀⣀⣀⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿",
"⢿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠁⠀⠀⣼⣿⣿⣿⣦⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⡿     For all currencies on Coinmarketcap!",
"⠸⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠛⠛⠿⠟⠋⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠇",
"⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⣤⡄⠀⣀⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⡟⠀",
"⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣄⣰⣿⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀",
"⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀",
"⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⢿⣿⣿⣿⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀\n\n"
])
