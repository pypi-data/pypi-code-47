# main.py
# deploy this for everyone and other apps!
import fifteenrock

try:
    import fifteenrock_project_main
except:
    pass
try:
    from . import fifteenrock_project_main
except:
    pass


def main(context, event):
    return context.Response(body=fifteenrock_project_main.main(event),
                            headers={},
                            content_type='text/json',
                            status_code=200)
