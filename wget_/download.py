# import wget
# wget.download("https://stackoverflow.com/questions/33886917/how-to-install-wget-in-macos")
# # wget.download("wget --user tipster --password cdroms https://trec.nist.gov/results/trec26/rts/summary-batchB-adv_lirmm-Run1.txt")
import urllib
response = urllib.urlopen('https://stackoverflow.com/questions/33886917/how-to-install-wget-in-macos')
html = response.read()