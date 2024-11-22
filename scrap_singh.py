import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/user/PewDiePie'
page = requests.get(url)
print(page, 'AAAAAAAAAAAAAAAAA')

soup = BeautifulSoup(page.text, "html.parser")
# print(soup, 'CCCCCc')

pew = soup.findAll("span", {"class": "masthead_custom_styles"})

print(pew, "BBBBBBBBBBBBBBB")



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vrinda',
        'USER': 'root',
        'PASSWORD': '<VrInDa@123>',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}



AUTH_USER_MODEL = 'home.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
