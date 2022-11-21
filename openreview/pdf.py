import argparse
import json
import os
from collections import defaultdict
from tqdm import tqdm
import openreview
import json
import csv

def download_iclr19(client, outdir='./'):

    num=1

    with open('./forum.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            forum = row
            pdf_outdir = os.path.join(outdir, 'iclr_pdfs')
            pdf_binary = client.get_pdf(forum)
            pdf_outfile = os.path.join(pdf_outdir, (''+str(num)+'.pdf').format(forum))
            with open(pdf_outfile, 'wb') as file_handle:
                file_handle.write(pdf_binary)
            print(num)
            num+=1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', '--outdir', default='./', help='directory where data should be saved')
    parser.add_argument('--baseurl', default='https://api.openreview.net')
    parser.add_argument('--username', default='', help='defaults to empty string (guest user)')
    parser.add_argument('--password', default='', help='defaults to empty string (guest user)')

    args = parser.parse_args()

    outdir = args.outdir

    client = openreview.Client(
        baseurl=args.baseurl,
        username=args.username,
        password=args.password)

    download_iclr19(client, outdir)