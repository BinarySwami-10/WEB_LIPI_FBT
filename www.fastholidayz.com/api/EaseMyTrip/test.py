import re
string='\nRs.\n\r\n                                            2,821.00\r\n                                            \r\n                                                                                              \r\n                                            \n'
string=re.findall(r'(\d)+?',string)
print((string))