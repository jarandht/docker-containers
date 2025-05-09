FROM netboxcommunity/netbox:YOUR TAG

COPY ./plugin_requirements.txt /opt/netbox/
COPY ./plugin_requirements.txt /opt/netbox/
RUN /usr/local/bin/uv pip install -r /opt/netbox/plugin_requirements.txt

COPY configuration/configuration.py /etc/netbox/config/configuration.py
COPY configuration/plugins.py /etc/netbox/config/plugins.py
RUN SECRET_KEY="udfhgoiu40590+sldkfæsølkfpøisorpsdølkgjøsdiguirjtgøkjdøioj349tipojgpdojgøjølskjløkj9405" /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic --no-input