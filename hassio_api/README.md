# HassIO Server

## Host Controll

Communicate over unix socket with a host daemon.

- commands
```
# info
-> {'host', 'version'}
# reboot
# shutdown
# host-update [v]
# supervisor-update [v]

# network info
# network hostname xy
# network wlan ssd xy
# network wlan password xy
# network int ip xy
# network int netmask xy
# network int route xy
```

- Answer
```
{}|OK|ERROR
```

## HassIO REST API

Interface for HomeAssistant to controll things from supervisor.

### HassIO

- `/update`
Payload: {'version': '0.XX'}
If version is None it read last version from server.

### Host
- `/host/network`
Payload: {'hostname': '', 'mode': 'dhcp|fixed', 'ssid': '', 'ip': '', 'netmask': '', 'gateway': ''}

- `/host/reboot`

- `/host/shutdown`

- `/host/info`

- `/host/update`
On some device we support host upates. Like ResinOS.

### HomeAssistant

- `/homeassistant/info`

- `/homeassistant/update`
Payload: {'version': '0.XX.Y'}
If version is None it read last version from server.

### REST API addons

- `/addons/info`

- `/addons/reload`

- `/addons/{addon}/start`
Payload: {'options': {}}

- `/addons/{addon}/stop`

- `/addons/{addon}/install`
Payload: {'version': 'x.x'}

- `/addons/{addon}/uninstall`

- `/addons/{addon}/update`
Payload: {'version': 'x.x'}
If version is None it read last version from server.
