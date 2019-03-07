X_FRAME_OPTIONS = 'ALLOWALL'
## 跨域
CORS_ALLOW_CERDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = ('*')

CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:9000',
)

from corsheaders.defaults import default_methods, default_headers

CORS_ALLOW_METHODS = default_methods + (
    'POKE',
)

CORS_ALLOW_HEADERS = default_headers + (
    'my-custom-header',
)
