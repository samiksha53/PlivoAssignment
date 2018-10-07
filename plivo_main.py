import sys
import argparse
import random, string
import inspect
import requests
import json
import functions

def main(argv):
    obj=functions.MyClass()
    num1,num2=obj.get_number()
    print ("two number selected are :"+str(num1)+" and "+str(num2))
    uuid=obj.send_message()
    print ("UUID of sent message is :"+uuid)
    price_deducted=obj.get_message_details()
    print ("the amount deducted is :"+str(price_deducted))
    outbound_rate=obj.get_pricing()
    print ("the decided outbound rate is:"+str(outbound_rate))
    status=obj.compare_pricing()
    if (status == "true"):
        print "price deducted is same as outbound rate defined"
    else:
        print "rate verification failed"
    check=obj.get_account_details()
    if (check=="true"):
		print "cash credit is more than deducted amount"
	else:
		print "Cash Credit not sufficient"

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))