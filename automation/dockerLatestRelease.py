##Automation script for minecraft docker
import docker,os,argparse


parser = argparse.ArgumentParser(description='Process to automate papers version docker update')
parser.add_argument('--id', dest='identifier', type=str, required=True, help='docker identifier, name or image')
parser.add_argument('--path', dest='volumePath', type=str, default="/home/", help='Volume path absolute to save paper server')
parser.add_argument('--MC_RAML', dest='MC_RAML', type=str,default="1024M", help='Min heap size')
parser.add_argument('--MC_RAMH', dest='MC_RAMH', type=str,default="1024M", help='Max heap size')
parser.add_argument('--javaOPTS', dest='JAVA_OPTS',default="",type=str, help='Java extra options')
parser.add_argument('--MC_VERSION', dest='MC_VERSION', type=str, help='MC version to keep, update only builds')
args = parser.parse_args()

client = docker.from_env()
for container in client.containers.list():
    contObj = client.containers.get(container.id)
    if args.identifier== contObj.attrs['Config']['Image'] or args.identifier== contObj.attrs['Config']['name']:
        contObj.stop()
        contObj.remove()
        break


if not args.MC_VERSION:
    os.system('docker run -p 25565:25565 -v '+args.volumePath+':/papermc --restart on-failure -e MC_RAML='+args.MC_RAML+' -e MC_RAMH='+args.MC_RAMH+' -e JAVA_OPTS="'+args.JAVA_OPTS+'" -d --name=paperMCserver amazoncorretto-minecraft')
else:
    os.system('docker run -p 25565:25565 -v '+args.volumePath+':/papermc --restart on-failure -e MC_VERSION='+args.MC_VERSION+' -e MC_RAML='+args.MC_RAML+' -e MC_RAMH='+args.MC_RAMH+' -e JAVA_OPTS="'+args.JAVA_OPTS+'" -d --name=paperMCserver amazoncorretto-minecraft')
