'''
	Minify Files And process templates via the data-load attributes.
	basically load the data-load url in html inline...
'''
import modulex as mx
import re
mx.require(['bs4', 'htmlmin', 'minify-html', 'lxml', 'css-html-js-minify'])

try:
	# from css_html_js_minify import html_minify, js_minify, css_minify
	import minify_html
except Exception:
	pass


def multiple_replace(dict, text):
	# Create a regular expression  from the dictionary keys
	regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

	# For each match, look-up corresponding value in dictionary
	return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


mx.os.chdir('../')


template = open('./index-dev.html', 'r', encoding="utf-8").read()
soupobj = mx.make_soup(template)

for section in soupobj.select('[data-load]'):
	try:

		if (proxypath:= section.get('data-load', None)):  # noqa: E225
			fileViewData = open(proxypath).read()
			del section['data-load']
			# fileViewData = soupobj.new
			# print(fileViewData)
			section.append(mx.make_soup(fileViewData))
	except:
		pass


def individual_passes():
	for style in soupobj.select('style'):
		style.string = css_minify(style.string, noprefix=True)
		# print(style)
	for script in soupobj.select('script'):
		script.string = js_minify(script.string)
		print(script)


minified = minify_html.minify(str(soupobj),
                              do_not_minify_doctype=False,
                              ensure_spec_compliant_unquoted_attribute_values=False,
                              keep_closing_tags=True,
                              keep_comments=False,
                              keep_html_and_head_opening_tags=True,
                              keep_spaces_between_attributes=False,
                              minify_css=True,
                              minify_js=True,
                              remove_bangs=True,
                              remove_processing_instructions=True,)


mx.fwrite('index.html', minified)
print("==========> DEV.HTML FILES HAVE BEEN MINIFIED")
# print(soupobj.prettify())

