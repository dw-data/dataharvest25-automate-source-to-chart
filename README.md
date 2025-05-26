# Dataharvest session: <br>Using free tools to automate your data flows from source to chart

*Session by Gianna-Carina Gruen from [DW's Data Journalism Team](https://dw.com/data)*

### What you will learn:

How to ...

* collect data from a url
* parse the data into the needed format using Python's `pandas` library
* use Python's [`datawrapper` library](https://datawrapper.readthedocs.io/en/latest/user-guide/api.html#datawrapper.Datawrapper.update_description) to create a chart
* set up the script to run automatically on [Github Actions](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#availability)


### Prerequesites for the session: 

*Basic coding or Python knowlegde is helpful but not required*

* required: Access to colab.google.com (if you already have a Google account, it's included), so you can open [this notebook](https://colab.research.google.com/drive/1ZHZ67xisRPs0fC4VW5FdudTogy9wzNeh?usp=sharing)
* required: [Datawrapper API token](https://academy.datawrapper.de/article/225-what-you-can-do-with-our-api-and-how-to-use-it) (please set it up in ahead of the session)
* required: Github Account (if you want to set up the workflow to be automated) (please set it up in ahead of the session)
* optional: Code Text editor (if you want to code along in the session), like Atom or Sublime Text
* optional: [Distill Browser Plugin](https://distill.io/) (if you want to set up the workflow on click)


### Code & Data

**Code**: To follow along, you'll need to make yourself a copy of [this jupyter notebook on Google colab](https://colab.research.google.com/drive/1ZHZ67xisRPs0fC4VW5FdudTogy9wzNeh?usp=sharing).

**Data source**: For this session, we'll be working with the [UNHCR data on arrivals to Europe via land and sea](https://data.unhcr.org/en/situations/europe-sea-arrivals), more specifically: with the URLs provided on the page to the json data

* all arrivals (sea + land): "https://data.unhcr.org/population/get/timeseries?widget_id=588956&sv_id=100&population_group=4797,4798,5634&frequency=month&fromDate=2016-01-01"
* sea arrivals: "https://data.unhcr.org/population/get/timeseries?widget_id=588957&sv_id=100&population_group=4797,5634&frequency=month&fromDate=2016-01-01"
* land arrivals: "https://data.unhcr.org/population/get/timeseries?widget_id=588958&sv_id=100&population_group=4798&frequency=month&fromDate=2016-01-01"

### Automation

To automatically run your script on [Github Actions](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration), you'll need three things (which are also included in this github repo and can be downloaded at the top.

* your script as a `.py` file
* a `requirements.txt` file
* a `.yml` file wrapped into a folder .github/workflows

You'll be adding all of them into a repository in your own Github account. Then switch to the "Actions" tab to see if your automation run started properly or whether there was an issue that needs debugging.
