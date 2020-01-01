import threading
def run_server1(import_name):
    import wpkit
    from wpkit.web.bps import pan, MyBlueprint
    app = wpkit.web.get_default_app(import_name)

    bp_pan = pan.BluePan(import_name)

    app.add_blueprint(bp_pan)

    print(app.url_map)
    print(app.sitemap)
    app.run(port=80)
def run_server2(import_name):
    from wpkit.services import LocalFSServer

    app = LocalFSServer(import_name, path="./")
    print(app.url_map)
    app.run(port=8002)

def start_server(import_name):
    t1 = threading.Thread(target=run_server1,args=[import_name])
    t2 = threading.Thread(target=run_server2,args=[import_name])
    t1.start()
    t2.start()
    t1.join()
    t2.join()

