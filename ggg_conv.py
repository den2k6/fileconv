#! /usr/bin/env python3

import os, sys, shutil, tarfile

def main():
  args = sys.argv

  if len(args) != 3:
    print('概要：\n　GGG からダウンロードした CSV ファイルを BBB ダウンロード用に変換する\n　(.tar.gz, .tar.gz.ok を出力)\n')
    print('Usage:')
    print(f'　{args[0]} <GGG.csv> <BBB.csv>\n')
    print(f'　<GGG.csv>: GGG からダウンロードした CSV ファイル')
    print(f'　<BBB.csv>: GGG にアップロードした CSV ファイル（ファイル名を参照するだけ）\n')
    print(f'　　※拡張子(.csv)まで必要\n')
    print(f'例：\n　python3 {args[0]} Arai20210907101347.csv araitshop0002884920210901.csv\n')
    exit()

  sname_csv = args[1]
  tname = 'R' + '.'.join(args[2].split('.')[:-1])
  tname_txt = tname + '.txt'

  if not os.path.exists(sname_csv):
    print(f'File({sname_csv}) not exist.\n')
    exit()

  shutil.copy(sname_csv, tname_txt)
  tname_tar_gz = tname + '.tar' + '.gz'

  # make a .tar.gz file
  gz = tarfile.open(tname_tar_gz, 'w|gz', format=tarfile.GNU_FORMAT)
  gz.add(tname_txt)
  gz.close()

  tname_ok = tname_tar_gz + '.ok'
  shutil.copy(tname_tar_gz, tname_ok)

if __name__ == '__main__':
  main()
