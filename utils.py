import getopt
import sys
import os.path
import argparse

def get_host_options(desc, config=True, hosts='+'):
    parser = argparse.ArgumentParser(description=desc)
    if config:
        parser.add_argument('-c',
                            dest='config',
                            metavar='config.ini',
                            action='store',
                            default='config.ini',
                            help='path to ini file with config')
    parser.add_argument('host',
                        metavar='FQDN',
                        type=str,
                        nargs=hosts,
                        help='nova compute host')
    return parser.parse_args()

def get_options(argv, file):
    config = 'config.ini'
    host = ''
    action = ''
    help = '%s --host <compute host> --action <action> [--config <configfile>]' % file
    try:
        opts, args = getopt.getopt(argv,"hH:c:a:",["config=","host=","action="])
    except getopt.GetoptError:
        print help
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print help
            sys.exit()
        elif opt in ("-c", "--config"):
            config = arg
        elif opt in ("-H", "--host"):
            host = arg
        elif opt in ("-a", "--action"):
            action = arg
    if os.path.isfile(config) == False:
        print "ERROR: could not open ini config file %s" % config
        print help
        sys.exit()
    if action == '' or config == '' or action == '':
        print help
        sys.exit()
    return dict(config=config, action=action, host=host)

if __name__ == "__main__":
   print get_options(sys.argv[1:], sys.argv[0])
