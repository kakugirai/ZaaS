# zanryu
Fill in Zanryu card? NO MORE!

## Installation

```
brew install wkhtmltopdf
```
```
pip3 install -r requirements.txt
```

## Usage
It's a simple tool that can help you print out zanryu card when you are ZANRYUing in Delta. You can simply write a bash/python script to automate the process and let crontab helps you check your status everyday.

``` python
import subprocess
import fill
from check_ip import check_ip

def main():
    if check_ip("192.168.1.1/24"):
        fill.fill_date("info.json")
        fill.fill_html("blank.html", "info.json")
        subprocess.call(['wkhtmltopdf', 'zanryu.html', 'zanryu.pdf'])
        subprocess.call(['lpr', '-P', name_of_the_printer, '-o', 'media="a4"', 'zanryu.pdf'])

if __name__ == '__main__':
    main()
```
## TODOs
- [ ] Rewrite HTML with a model engine(EJS? Pug?)
- [ ] Decrease dependencies
