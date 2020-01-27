import socket
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from fire_clients import run_patient_client
from jsonrpc import JSONRPCResponseManager, dispatcher

server_port=4000

@dispatcher.add_method
def fire_client(**kwargs):
    resp = ""
    if ("npatient" in kwargs.keys()) and ("serve_ip" in kwargs.keys()) and ("serve_port" in kwargs.keys()):
        num_patients = kwargs.get("npatient")
        serve_ip = kwargs.get("serve_ip")
        serve_port = kwargs.get("serve_port")

        resp += "runing valid request npatient={}, serve_ip={}, serve_port={} ".format(num_patients, serve_ip, serve_port)
        server_path = serve_ip + ":" + str(serve_port)
        run_patient_client(server_path, num_patients)
    else:
        resp += "invalid request, use default npatient=1, ip=localhost, port=8000 "
        server_path =  "localhost:8000"
        run_patient_client(server_path, 1)

    print(resp)
    return resp

@Request.application
def application(request):
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')

if __name__ == '__main__':
    print("RPC server unning on IPv4 addr: {}".format(socket.gethostbyname(socket.gethostname())))
    run_simple('localhost', server_port, application)