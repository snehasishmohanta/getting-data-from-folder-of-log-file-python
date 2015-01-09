""" as i am having a folder which contain some log files. from this folder i need to extract the values of timestand , initial query and numof sugessions from each log file.
here inside the folder i am having some log file "/home/snehasish/log/autosuggest1"
inside that i am having log files like below.
snehasish@ip-10-0-67-159:~/log/autosuggest1$ ls
nginx.log.2014-12-17-00  nginx.log.2014-12-17-05  nginx.log.2014-12-17-10  nginx.log.2014-12-17-15  nginx.log.2014-12-17-20
nginx.log.2014-12-17-01  nginx.log.2014-12-17-06  nginx.log.2014-12-17-11  nginx.log.2014-12-17-16  nginx.log.2014-12-17-21
nginx.log.2014-12-17-02  nginx.log.2014-12-17-07  nginx.log.2014-12-17-12  nginx.log.2014-12-17-17  nginx.log.2014-12-17-22
nginx.log.2014-12-17-03  nginx.log.2014-12-17-08  nginx.log.2014-12-17-13  nginx.log.2014-12-17-18  nginx.log.2014-12-17-23
nginx.log.2014-12-17-04  nginx.log.2014-12-17-09  nginx.log.2014-12-17-14  nginx.log.2014-12-17-19


what i need to do is to go through each log file and find out the require thing.
"""
# below is the code

import re
import os
auto_prefix = u'\u200B'
from collections import Counter
path = "/home/snehasish/log/autosuggest1/"

for path, dirs, files in os.walk(path):
        for data in files:
                with open("/home/snehasish/log/autosuggest1/"+data) as text:
                        for line in text:
                                date = re.match("^\[.*?]",line)
                                Iq = re.match(".*?Input query[^:]*:(.*?,)", line)
                                Ns = re.match(".*?NumSuggestions[^:]*:(.*?,)", line)


                                if date and Iq and Ns :
                                        q = Iq.group(1)
                                        q = q.decode('utf-8').replace(auto_prefix, "")
                                        result = Counter(q.encode('utf-8')).most_common()
                                        for date, Iq, Ns, freq in result:
                                                print date.group(0),q.encode('utf-8'),Ns.group(1),freq
