from pprint import pprint
import libcloud
from libcloud import DriverType

print("hello world")

cls = libcloud.get_driver(DriverType.COMPUTE, DriverType.COMPUTE.EC2)

pprint(cls)


