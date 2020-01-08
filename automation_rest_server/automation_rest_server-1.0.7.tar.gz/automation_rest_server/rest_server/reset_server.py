# coding=utf-8
from flask import Flask
from flask_restful import Api
from Lib.driver.rest_server.resource.test_resource import TestResource
from Lib.driver.rest_server.resource.operation_resource import OperationResource
from Lib.driver.rest_server.resource.state_resource import StateResource
from Lib.driver.rest_server.resource.benchmark_resource import BenchmarkResource
from Lib.driver.rest_server.resource.iometer_benchmark_resource import IometerBenchmarkResource
from Lib.driver.rest_server.resource.models.ftp_server import thread_start_ftp_server
from Lib.driver.test_framework.database import update_abnormal_end_tests


APP = Flask(__name__)
API = Api(APP)


API.add_resource(OperationResource, "/operation")
API.add_resource(StateResource, "/state")
API.add_resource(TestResource, '/test/<filter_>', '/test', '/test/<type_>/<filter_>', '/test/results/<key_>',
                 '/test/testsuite/<test_name_>')
API.add_resource(BenchmarkResource, "/benchmark", "/benchmark/results/<key_>")
API.add_resource(IometerBenchmarkResource, "/benchmark/iometer/testlist")


if __name__ == '__main__':
    update_abnormal_end_tests()
    thread_start_ftp_server()
    APP.run(host="0.0.0.0", debug=False)
