"""Constants used by PyBlueBOLT"""

BLUEBOLT_USER_AGENT = 'PyBlueBOLT (https://github.com/rsnodgrass/pybluebolt/)'

BB_ENDPOINT = 'https://www.mybluebolt.com'

BB_AUTH_URL = BB_ENDPOINT + '/data-svc/login_check_svc.php?svc=authenticateUser&data[username]={username}&data[password]={password}'

BB_LOCATION_LIST_URL = BB_ENDPOINT + '/middleware/locations/dataSvc.php?svc=getSitesData&pageNo=1&recordsPerPage=18'
BB_LOCATION_DETAILS_URL = BB_ENDPOINT + '/data-svc/siteManagement/data-svc.php?siteId={site_id}&svc=settings'

BB_DEVICE_LIST_URL = BB_ENDPOINT + '/data-svc/siteManagement/data-svc.php?siteId={site_id}&svc=devList&detailed=true&isCached=false'
BB_DEVICE_STATUS_URL = BB_ENDPOINT + '/data-svc/cv1.deviceControls/data-svc.php?siteId={site_id}&devClass={device_class}&devId={device_id}&svc=status'
BB_OUTLETS_URL = BB_ENDPOINT + '/data-svc/cv1.deviceControls/data-svc.php?siteId={site_id}&devClass={device_class}&devId={device_id}&svc=labels'
