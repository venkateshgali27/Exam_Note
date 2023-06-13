class Config:
  DEBUG =False
  DEVELOPMENT=True
  CSRF_ENABLED=True
  ASSETS_DEBUG=False
class Prodution(Config):
  pass
class Developmemt(Config):
  DEBUG=True
  DEVELOPMENT=True
  TEMPLATES_AUTO_RELOAD=True
  ASSETS_DEBUG=True
