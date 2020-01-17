from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import click
import time

from . import __version__

def format_help(help):
    """Formats the help string."""
    from pyfiglet import Figlet
    f = Figlet(font='slant')
    logo = click.style(f.renderText('MOMO'), bold=True, fg='green')
    help = help.replace("Options:", click.style("Options:", bold=True))
    help = help.replace("Usage: momo", click.style("momo", bold=True))
    help = help.replace("  run", click.style("  run", fg='cyan',bold=True))
    help = logo + "\n" +help
    return help



@click.group(invoke_without_command=True)
@click.version_option(message=click.style(__version__, bold=True), version=__version__, help=click.style("Show momo the version.", fg='green'))
@click.help_option(help=click.style("Just Tell You MOMO is Very Powerful.", fg='yellow'))
@click.pass_context
def momo(ctx):

    if ctx.invoked_subcommand is None:
        click.echo(format_help(ctx.get_help()))


@momo.command(help=click.style("Execute the momo Application.", fg='yellow'))
@click.option("--driver", '-d', default='chrome',show_default=True,help="WebDrvier of selenium.")
@click.option("--wait", '-w',  default=20, show_default=True, help="Locate Elements Wait Time(s).")
@click.option("--login", '-l', default=40, show_default=True, help="Login Wait Time(s).")
@click.option("--number", '-n',  default=10, show_default=True, help="Number of read links.")
@click.help_option()
def run(driver, wait, login, number):

    if driver == 'edge':
        browser = webdriver.Edge("C:\\Program Files (x86)\\Microsoft\\Edge Beta\\Application\\msedgedriver.exe")
    else:
        browser = webdriver.Chrome("E:\\selenium\\chromedriver.exe")
    click.secho("Launching "+browser.name , bg="blue")

    try:
        browser.get('https://www.xuexi.cn')
        click.secho("Opening Website -- https://www.xuexi.cn", bg='blue', bold=True)
        wait = WebDriverWait(browser, wait)
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='login']/a[2]")))
        login_button.click()
        click.secho("Starting to login...", fg="green")
        time.sleep(login)


        browser.switch_to.window(browser.window_handles[1])

        #表示刷新page后已经显示为已登录状态
        logined = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='logged-text']")))
        if not logined:
            click.secho("login failure!", fg="red")
        click.secho("login successfully" ,fg="green")

        links = browser.find_elements_by_xpath("//div[@class='text-link-item-title']//span[@class='text']")
        click.secho("find links "+str(len(links)), bg="blue", fg="white")
        click.secho("start to reading...")

        if links:
            with click.progressbar(length=number, label="Learning article ", fill_char=click.style('#',fg ="yellow")) as bar:
                for index, link in enumerate(links):
                    if index > number: break
                    link.click()
                    tabs = browser.window_handles
                    if not len(tabs) == 3:
                        continue
                    bar.update(1)
                    browser.switch_to.window(tabs[2])
                    action = ActionChains(browser)
                    time.sleep(4)
                    action.send_keys(Keys.ARROW_DOWN).pause(2).send_keys(Keys.ARROW_DOWN).pause(2).send_keys(
                        Keys.ARROW_DOWN).pause(2).send_keys(Keys.ARROW_DOWN).pause(2).send_keys(Keys.ARROW_DOWN).pause(
                        2).send_keys(Keys.ARROW_DOWN).pause(2).perform()
                    #action.key_down(Keys.ARROW_DOWN).
                    js = "var q = document.documentElement.scrollTop=10000" #下拉滚动条
                    browser.execute_script(js)
                    browser.close()
                    #drivere通过一系列动作（如：打开/关闭窗口）而显示的窗口不代表可以直接操作。定位各窗口元素前要先使用switch_to.window()切换，driver是不会自己跳转的哦。
                    #browser.switch_to_window(tabs[1])
                    browser.switch_to.window(browser.window_handles[1])

            print("ending......")

    except Exception as e:
        print(str(e))

#MOMO.add_command(run,name='run')

if __name__ == '__main__':
    momo()
