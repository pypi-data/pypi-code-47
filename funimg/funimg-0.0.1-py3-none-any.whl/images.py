import aiohttp

session = aiohttp.ClientSession()

def achievement(text: str):
	url = f"https://api.alexflipnote.dev/achievement?text={text}"
	return url