# Web Page Reader

This script allows you to read out loud the contents of a web page. You can specify the URL of the web page, the id or class name of the HTML element containing the main content of the page, and the playback rate of the audio file.

## Requirements

- `Python 3.6` or later
- The `requests` library
- The `beautifulsoup4` library
- The `gtts` library
- The `pygame` library

## Usage

To run the script, use the following command:

```
python read_web_page.py <page_url> [--id <id_name>] [--class <class_name>]
```

Replace `<page_url>` with the URL of the web page that you want to read out loud. If you want to specify the id or class name of the HTML element containing the main content of the page, you can use the `--id` or `--class` arguments, respectively, followed by the id or class name (e.g., `--id main-content` or `--class article-body`).

Here is an example of how you can call the script:

```
python read_web_page.py https://www.example.com --id main-content --class article-body
```

This command will run the read_web_page.py script and read out loud the contents of the web page at the URL https://www.example.com, extracting the main content of the page from the HTML element
