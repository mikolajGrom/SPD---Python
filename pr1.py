#!/usr/bin/env python3

import argparse
import sys
import itertools
from data_parser import DataParser
from instance import Instance
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str,
                    help="data file to be parsed")
parser.add_argument("-a", "--algorithm", type=str,
                    help="algorithm type (bruteforce, johnson, neh, simulated_annealing)")
parser.add_argument("-s", "--json", type=str,
                    default="results.json",
                    help="json file for results")
args = parser.parse_args()


def main():
    if args.filename is None or args.algorithm is None:
        parser.print_help()
        sys.exit(1)
    data_parser = DataParser(args.filename)
    jobs, machines, tasks, neh_prio = data_parser.get_instance_parameters()
    instance = Instance('Roxanne', machines, jobs, tasks, neh_prio)
    instance.print_info()
    jsonfile = "data/results/" + args.filename.split('/')[1].split('.txt')[0] + "_" + args.algorithm + "_" + args.json
    if args.algorithm == 'bruteforce':
        instance.generate_best_cmax()
        instance.save_results(args.filename, args.algorithm, jsonfile)
    elif args.algorithm == 'johnson':
        instance.johnsons_algorithm()
        instance.save_results(args.filename, args.algorithm, jsonfile)
    elif args.algorithm == 'neh':
        order = instance.neh()
        instance.save_results(args.filename, args.algorithm, jsonfile)
    elif args.algorithm == 'sim_annealing':
        #queue = instance.neh()
        order = instance.neh_prio[:]
        print("INFO: SIMULATED ANNEALING: Starting with order: {}".format(str(order)))
        instance.simulated_annealing(50, order, 0.01, 0.8)
    else:
        print("ERROR: Wrong algorithm type")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
