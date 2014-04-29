#!/usr/bin/env python
# encoding: utf-8
"""
File: split_models_from_genetrees.py
Author: Brant Faircloth

Created by Brant Faircloth on 19 September 2012 18:09 PDT (-0700)
Copyright (c) 2012 Brant C. Faircloth. All rights reserved.

Description:

"""


import argparse
from phyluce.helpers import FullPaths, is_file

#import pdb


def get_args():
    """Get arguments from CLI"""
    parser = argparse.ArgumentParser(
            description="""Split the substitution models from genetrees output by CloudForest""")
    parser.add_argument(
            "--genetrees",
            required=True,
            type=is_file,
            action=FullPaths,
            help="""The cloudforest genetree file containing models"""
        )
    parser.add_argument(
            "--output",
            required=True,
            action=FullPaths,
            help="""The output file to hold the parsed substitution model data"""
        )
    return parser.parse_args()


def main():
    args = get_args()
    with open(args.output, 'w') as outf:
        for line in open(args.genetrees, 'rU'):
            locus_and_model = line.split(' ')[1].strip("'").split(',')
            locus = locus_and_model[0].split('=')[1]
            model = locus_and_model[1].split('=')[1]
            outf.write("{0}\tAICc-{1}\n".format(locus, model))

if __name__ == '__main__':
    main()
