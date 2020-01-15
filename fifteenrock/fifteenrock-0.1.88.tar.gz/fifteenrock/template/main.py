# main.py
# deploy this for everyone and other apps!
import traceback

import fifteenrock

try:
    import fifteenrock_project_main
except ImportError:
    pass
except Exception as e:
    print(e)
    traceback.print_exc()
    pass

try:
    from . import fifteenrock_project_main
except ImportError:
    pass
except Exception as e:
    print(e)
    traceback.print_exc()
    pass


def main(context, event):
    try:
        result = fifteenrock_project_main.main(event)
    except Exception as e:
        tb = traceback.format_exc()
        context.logger.info(tb)
        print(tb)
        result = None
        pass

    return context.Response(body=result,
                            headers={},
                            content_type='text/json',
                            status_code=200)
