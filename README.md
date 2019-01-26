# resultBot
----
A python script to download and email results from [North Maharashtra University results website](http://exam.nmu.ac.in/online%20result/aspx/online%20result.aspx).

### Usage Demonstration
![Demonstration](http://i.imgur.com/pnqI8uj.png)
### Sample Email
![Sample Email](http://i.imgur.com/d8tqoGY.png)
## Requirements
* [Python 2.7](https://www.python.org/downloads/)
* [PhantomJs](http://phantomjs.org/)
* [Selenium](http://selenium-python.readthedocs.io/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Installation
1. Clone repository `git clone https://github.com/jarifibrahim/resutBot.git`.
2. Python 2.7 download and installation instructions can be found [here](https://www.python.org/downloads/).
3. Download PhantomJS from [here](http://phantomjs.org/download.html). Extract the files and copy `phantomjs` file from `bin` directory inside extracted files to repository root folder.
4. Download and install Selenium using `pip install selenium`.
5. Download and install BeautifulSoup using `pip install bs4`.

## Setup
Edit the file *config.py* to change default configuration.

## Usage
`$ ./main.py <faculty>`

eg: `$ ./main.py "Engg and Tech"`

## Setup script to run periodically to check for results
### On Linux
To execute the script periodically setup `cron` as follows:

1. Execute `crontab -e` and append the line.

  To execute after every 5 minutes:

  `*/5 * * * * /path/to/main.py >> /path/to/save/logs 2&>1` 

  To execute after every 15 minutes:

  `*/15 * * * * /path/to/main.py >> /path/to/save/logs 2&>1` 

## On Windows
Use [Windows Task Scheduler](http://windows.microsoft.com/en-us/windows/schedule-task)
