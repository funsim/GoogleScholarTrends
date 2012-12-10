import urllib2
import re
import sys
import time, random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
import datetime
from numpy import array
from optparse import OptionParser

def main():
    usage = "Usage: google_scholar_trend.py [options]\n\nExample: google_scholar_trend.py -t 'biology optimization' -s 1990 -f 2012\n\nA simple trend generator that produces a plot showing how many papers have been published during a period of time."
    parser = OptionParser(usage)
    parser.add_option("-t", "--term", dest="searchterm", help="the search term")
    parser.add_option("-s", "--start-year", dest="startyear", type = int, help="year at which trend starts", default = 1990)
    parser.add_option("-f", "--final-year", dest="finalyear", type = int, help="year at which trend stops", default = 2012)
    (options, args) = parser.parse_args()
    if not options.searchterm:
        print "You need to provide a search term. Run 'google_scholar_trend.py -h' for help."
        sys.exit(1)

    results = []
    for year in range(options.startyear, options.finalyear + 1):
        print "Finding number of publications in year %i..." % year,
        nb_results = get_number_of_results(generate_url(options.searchterm, year))
        results.append((year, nb_results))
        print "found %i" % results[-1][1] 

    save_plot(results, options.searchterm)

def save_plot(results, searchterm):
    years, nb_results = array(results).T
    filename = "trend_" + str(years[0]) + "_" + str(years[-1]) 
    fileformat = "pdf"

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    fig.autofmt_xdate(rotation=90) 
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    dates = array([matplotlib.dates.date2num(datetime.datetime(y,1,1)) for y in years])
    ax1.plot_date(dates, nb_results, "ro", label = searchterm)
    ax1.legend()
    print "Saving plot to %s." % (filename + "." + fileformat)
    plt.savefig(filename + "." + fileformat)


def generate_url(term, year):
    url = "http://scholar.google.com/scholar?as_sdt=1,5&q=TERM&hl=en&as_ylo=YEAR&as_yhi=YEAR"
    url = url.replace("YEAR", str(year))
    term = term.replace(" ", "+")
    url = url.replace("TERM", term)
    return url

def get_number_of_results(url):
    # Wait a little to keep google happy
    wt = random.uniform(2, 5)
    time.sleep(wt)

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    content = opener.open(url).read()
    m = re.search('(?<=abc)results', content) 
    try:
        nb_results = re.search('([0-9,]*) results', content).group(1)
        nb_results = int(nb_results.replace(',', ''))
    except:
        print "Error: could not find the number of results in the google answer."
        sys.exit(1)
    return nb_results

if __name__ == "__main__":
        main()
