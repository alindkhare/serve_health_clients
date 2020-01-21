import argparse
import os
import subprocess
package_directory = os.path.dirname(os.path.abspath(__file__))
parser = argparse.ArgumentParser(description="Script for firing Go clients")
parser.add_argument("--ip", type=str, default="0.0.0.0",
                    help="IP address of server")
parser.add_argument("--port", type=str, default="5000",
                    help="port at which server is listening")
parser.add_argument("--num-patients", metavar="N", type=int, default=1,
                    help="Number of clients to fire the queries")

if __name__ == "__main__":
  args = parser.parse_args()
  client_path = client_path = os.path.join(package_directory,
                              "patient_client.go")
  server_path = args.ip + ":" + args.port
  procs = []
  for patient_id in range(args.num_patients):
    patient_name = "patient" + str(patient_id)
    ls_output = subprocess.Popen(["go", "run", client_path,
                                  patient_name, server_path])
    procs.append(ls_output)

  for p in procs:
        p.wait()