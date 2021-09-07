#! /usr/bin/env python3

import os, sys, shutil, tarfile

def main():
    args = sys.argv

    if len(args) != 2:
        print(f'Usage:\n {args[0]} <file>\n')
        exit()

    tname_ori = args[1]

    if not (os.path.exists(tname_ori)):
        print(f'file({tname_ori}) not exist.\n')
        exit()

    tname = 'new_' + tname_ori
    shutil.copy(tname_ori, tname)

    bname = '.'.join(tname.split('.')[:-1])
    # name_tar = bname + '.tar'
    name_gz  = bname + '.tar' + '.gz'

    # make a gzip file
    gz = tarfile.open(name_gz, 'w|gz')
    gz.add(tname)
    gz.close()

    # get file(s) from gzip
    gz = tarfile.open(name_gz, 'r|gz')
    gz.extractall()
    gz.close()


if __name__ == '__main__':
    main()
