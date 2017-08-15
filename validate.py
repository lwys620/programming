#!/home/j987139/python3.5.2/bin/python3.5

import csv
import collections
import pprint
import sys
from optparse import OptionParser

# build lookup table
# luTable[source_host:target_host][source_user:target_user] = true
# UUID,Zone,Service,Source Id,Target Id,Source Host,Target Host,Command,Period Ending,Number Of Activities

def optParse():
    parser = OptionParser()
    parser.add_option("-s", "--source", type="string", dest="source", help="source file to lookup from")    
    parser.add_option("-d", "--dest",   type="string", dest="dest",   help="dest file that needs lookup")
    (options, args) = parser.parse_args()
    return  (parser, options)    
 
def main():
    (parser, options) = optParse()
    if None in [options.source, options.dest]:
        print("source and dest are required")
        parser.print_help()
        sys.exit(1)
    pp = pprint.PrettyPrinter(indent=4)   
    print('build look up table')
    luTable = collections.OrderedDict()
    with open("{}".format(options.source), 'r') as srcFile:
        srcReader = csv.DictReader(srcFile)
        for line in srcReader:
            key = "{}:{}:{}:{}".format(line['Source Host'], line['Target Host'], line['Source Id'], line['Target Id'])
            luTable[key] = True
            
    
    print('start to lookup')        
    with open("{}".format(options.dest), 'r') as dstFile:
        dstReader = csv.DictReader(dstFile)
        for line in dstReader:
            key = "{}:{}:{}:{}".format(line['Source Host'], line['Target Host'], line['Source Id'], line['Target Id'])
            if key not in luTable:
                pp.pprint(line)
          
    
if __name__ == '__main__':
    main()
