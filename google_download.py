#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T

import csv
import os
import sys
from google_images_download import google_images_download

# 实例化一个下载器
downloader = google_images_download.googleimagesdownload()

csv_file = csv.reader(open('keywords.csv', encoding='utf-8'))

def download_images(csv_file):
	'''
	csv_file: 关键字文件
	limit: 最大数目
	print_urls: 显示路径
	chromedriver: 安装路径
	output_directory: 保存位置
	'''
	for word in csv_file:
		arguments = {
			'keywords': str(word), 
			'limit': 2, 
			'print_urls': True, 
			'chromedriver': r'D:\chromedriver_win32\chromedriver.exe',
			'output_directory': ''}
		downloader.download(arguments)

if __name__ == '__main__':
	download_images(csv_file)
