1.  removing the crowdsec_service section

    auto_registration:
      enabled: true
      token: "32  characters token"
      allowed_ranges:
        - X.X.X.X/24


cscli lapi register --machine MyMachineName --url <lapi_url>
2.  remove the api.server


https://docs.crowdsec.net/u/user_guides/multiserver_setup/

https://blog.lrvt.de/configuring-crowdsec-with-traefik/

https://plugins.traefik.io/plugins/6335346ca4caa9ddeffda116/crowdsec-bouncer-traefik-plugin
