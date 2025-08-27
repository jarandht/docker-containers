# Semaphore

## Fill out .env for config

## SSL
put certs in ./certs forlder named fullchain and privkey

## SSO

**Map config file in docker**


    volumes:
      - /config/:/etc/semaphore:rw

And add OICD config form config.json

## Ofical docs 
https://docs.semaphoreui.com/

## Check versions
https://github.com/semaphoreui/semaphore/releases