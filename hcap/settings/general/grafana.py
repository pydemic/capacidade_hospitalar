from hcap.settings.env import env

_uid = env("GRAFANA_DASHBOARD_UID", default="OMynCUCWx")
_url = env("GRAFANA_URL", default="http://localhost:3000")

GRAFANA_DASHBOARD_URL = f"{_url}/d/{_uid}"
