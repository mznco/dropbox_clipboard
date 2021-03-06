import time
import pyperclip
from subprocess import call


def is_dropbox_link(clipboard_content):
    if (
        clipboard_content is not None and
        clipboard_content.startswith("https://")
        and "www.dropbox.com" in clipboard_content
        and "dl=0" in clipboard_content
    ):
        return True
    return False


def make_dl_link(url):
    pyperclip.copy(url.replace("www", "dl").replace("?dl=0", ""))


def watch_clipboard():
    recent_value = ''
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            if is_dropbox_link(recent_value):
                make_dl_link(recent_value)
        time.sleep(1)


def main():
    call(['killall', 'ScriptMonitor'])  # see the readme
    watch_clipboard()


if __name__ == "__main__":
    main()
