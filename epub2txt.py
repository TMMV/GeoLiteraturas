#encoding=utf8

import sys
import re
import zipfile
import HTMLParser

class GetContent(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)	#HTMLParser不是new class，无法使用super
		self.content = ""

	def handle_data(self, data):
		self.content += data

re_digits = re.compile(r'(\d+)')
def embedded_numbers(s):
	pieces = re_digits.split(s)
	pieces[1::2] = map(int, pieces[1::2])
	return pieces

def sort_with_embedded_numbers(zipinfo_list):
	aux = [(embedded_numbers(zipinfo.filename), zipinfo) \
		for zipinfo in zipinfo_list]
	aux.sort()
	return [zipinfo for _, zipinfo in aux]

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "epub2txt.py sample.epub"
	fh = zipfile.ZipFile(sys.argv[1])
	html_list = [zip_info for zip_info in fh.filelist \
		if zip_info.filename.endswith("html")]
	html_list = sort_with_embedded_numbers(html_list)
	content_obj = GetContent()
	for html in html_list:
		content_obj.feed(fh.read(html))
	output_filename = sys.argv[1].replace(".epub", ".txt")
	out_fh = open(output_filename, 'w')
	out_fh.write(content_obj.content)
	out_fh.close()
