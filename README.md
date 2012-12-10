# GoogleScholarTrend
A simple trend plot generator that plots the number publications that contain specific key words on a time plot. 
![Result](https://raw.github.com/funsim/GoogleScholarTrends/master/results/trend_1990_2012.jpg)

Usage
=====

```bash
python google_scholar_tren .py [options]

Options:
  -h, --help            show this help message and exit
  -t SEARCHTERM, --term=SEARCHTERM
                        the search term
  -s STARTYEAR, --start-year=STARTYEAR
                        year at which trend starts
  -f FINALYEAR, --final-year=FINALYEAR
                        year at which trend stops
```


Example
=======

Running:
```bash
 python google_scholar_trend.py -t 'PDE optimization adjoint' -s 1983 -f 2011
```
Produces following output:

```bash
Finding number of publications in year 1983... found 18
Finding number of publications in year 1984... found 19
[...]
Finding number of publications in year 2011... found 823

Saving plot to trend_1983_2011.pdf.
```

This is the result:

![Result](https://raw.github.com/funsim/GoogleScholarTrends/master/results/trend_1983_2011.jpg)



Warning
=======

This program is probably not in line with Google Terms and Conditions. Therefore, this software should only be used for 
research purposes.
