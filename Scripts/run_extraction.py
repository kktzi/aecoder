""" Script that extracts results using the autoencoder.
"""

import argparse
import configparser

from extract import extract


def preprocess_config(c):
    conf_dict = {}
    int_params = ['model.segment.thresh', 'data.batch_size',
                  'model.segment.opening_r', 'model.segment.area_min',
                  'model.segment.area_max']
    #float_params = ['train.lr']
    bool_params = ['data.rescale']
    int_list_params = ['data.shape', 'model.layers']
    str_list_params = ['data.in', 'out.mode']
    for param in c:
        if param in int_list_params:
            conf_dict[param] = [int(val) for val in c[param].split(',')]
        elif param in int_params:
            conf_dict[param] = int(c[param])
        elif param in bool_params:
            conf_dict[param] = c[param] == 'True'
        elif param in str_list_params:
            conf_dict[param] = [val for val in c[param].split(',')]
        else:
            conf_dict[param] = c[param]
    return conf_dict


parser = argparse.ArgumentParser(description='Run extraction')
parser.add_argument("--config", type=str, default="./Configs/default.INI",
                    help="Path to the configuration file.")
parser.add_argument("-v", dest="verbose", action='store_true', default=False,
                    help="Print traces/Verbose.")


# Run extraction
args = vars(parser.parse_args())
dbg = args['verbose']
if dbg: print("Going to carry on result extraction")
config = configparser.ConfigParser()
config.read(args['config'])
config = preprocess_config(config['EXTRACT'])
extract(config, dbg)

