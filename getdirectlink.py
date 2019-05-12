# -*- coding:utf-8 -*-
import json
import csv


def change(ori_link):
    str_part = ori_link.split('/')
    args = str_part[7].split('?')
    out = 'https://' + str_part[2] + '/personal/' + str_part[6] + '/_layouts/15/download.aspx?' + args[1] + '&share=' + \
          args[0]
    return out


def generate_json(data, cover, artist):
    all_data = []
    for i in data:
        one = {}
        one['name'] = i[1]
        one['url'] = change(i[0])
        one['cover'] = change(cover)
        one['artist'] = artist
        all_data.append(one)
    json_data = json.dumps(all_data)
    print(json_data)


if __name__ == '__main__':
    filename = 'music.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
        generate_json(data,'https://vlityacid-my.sharepoint.com/:i:/g/personal/cc07_vlity_com/EZlIBganXw1Ll3Am52dRLhMB618-TzqoYqsKUlCxLF_jDg?e=avDeqZ','亚特兰蒂斯')