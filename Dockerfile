FROM kathara/base
RUN apt-get update && apt-get install strongswan strongswan-pki strongswan-swanctl libstrongswan-extra-plugins libtss2-tcti-tabrmd0 -y
RUN systemctl enable strongswan-starter
ENTRYPOINT systemctl start strongswan-starter && /bin/bash