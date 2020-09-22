import http.cookiejar as cookielib
cj = cookielib.MozillaCookieJar('cookies.txt')
cj.load()
data = requests.get(url, cookies=cj)

