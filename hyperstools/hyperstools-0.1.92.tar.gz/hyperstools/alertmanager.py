import requests
import json
import arrow

def send_mail(host="localhost",
              port="9093",
              receiver=None,
              interval=60,
              startsAt=None,
              endsAt=None,
              alertname="default_alertname",
              service=None,
              severity=None,
              instance=None,
              job=None,
              user=None,
              summary="default_summary",
              description="default_description"):
    alertApi = "http://" + host + ":" + str(port) + "/api/v1/alerts/"
    headers = {"Content-Type": "application/json"}
    utctime = arrow.utcnow()
    endtime = utctime.shift(seconds=+interval)
    alertData = {}
    if receiver:
        alertData.setdefault("receiver", receiver)
    if startsAt and endsAt:
        alertData.setdefault("startsAt", startsAt)
        alertData.setdefault("endsAt", endsAt)
    else:
        alertData.setdefault("startsAt", str(utctime))
        alertData.setdefault("endsAt", str(endtime))
    labels = {
        "alertname": alertname,
    }
    if service:
        labels.setdefault("service", service)
    if severity:
        labels.setdefault("severity", severity)
    if instance:
        labels.setdefault("instance", instance)
    if job:
        labels.setdefault("job", job)
    if user:
        labels.setdefault("user", user)
    annotations = {"summary": summary, "description": description}
    alertData.setdefault("labels", labels)
    alertData.setdefault("annotations", annotations)
    alertData = [alertData]
    data = json.dumps(alertData, ensure_ascii=False)
    response_data = requests.post(url=alertApi, data=data, headers=headers)
    try:
        results = response_data.json()
    except:
        results = {"status": "error"}
    return results

if __name__ == "__main__":
    results = send_mail(host="10.16.2.110", port=9093, receiver="live-monitoring")
    print(results)