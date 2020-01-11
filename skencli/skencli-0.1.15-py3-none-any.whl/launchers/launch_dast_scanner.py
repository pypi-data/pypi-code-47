import os
import docker 
import time

def run_dast_scanner(dast_url,is_dast_full_scan,build_tool):
    print('Launching DAST scanner')
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    #set working dir
    print('Setting build directory')
    if build_tool == 'jenkins':
        build_dir=os.environ['WORKSPACE']
    elif build_tool == 'travis':
        build_dir=os.environ['TRAVIS_BUILD_DIR']

    print(build_dir)

    if is_dast_full_scan:
        print('full scan started')
        cs='zap-full-scan.py -t url_value -J sken-dast-output.json'
        cs=cs.replace('url_value',dast_url)
        container = client.containers.run('nixsupport/dast:v1',cs,volumes={build_dir:{'bind':'/zap/wrk','mode':'rw'}}, detach=True, tty=False, stdout=False) 
        container.wait()
        container.logs()
        output_file='sken-dast-output.json'
    elif not is_dast_full_scan:
        print('quick scan started')
        cs='zap-cli -p 8090 quick-scan -r url_value'
        cs=cs.replace('url_value',dast_url)
        print(cs)
        cs_report='zap-cli -p 8090 report -f xml -o /scan/sken-dast-qs-output.xml'
        cmd = '/bin/sh -c "echo hello stdout ; echo hello stderr >&2"'

        container1 = client.containers.run('nixsupport/dast:v1',command='zap.sh -daemon -port 8090 -host 0.0.0.0 -config api.disablekey=true',name='zap-proxy',user='root',volumes={build_dir: {'bind':'/scan','mode':'rw'}}, ports={'8090/tcp':8090},detach=True, tty=False, stdout=False)

        time.sleep(50)
        #res=container1.exec_run(cs, stdout=True, stderr=True, stream=True, demux=False)
        res=container1.exec_run(cs)
        print(res.output)
        res1=container1.exec_run(cs_report)
        print(res1.output)
        container1.stop()
        client.containers.prune()
        output_file='sken-dast-qs-output.xml'
    return output_file



#if __name__ == "__main__":
#    dast_url='https://demo.testfire.net'
#    is_dast_full_scan='no'
#    build_tool='jenkins'
#    run_dast_scanner(dast_url,is_dast_full_scan,build_tool)

