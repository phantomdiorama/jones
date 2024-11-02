# jones

Give me the whip.

Throw me the idol.

A **bash** script that uses Pandoc to download web pages as plain text.
Filenames are truncated versions of the page title, grabbed with htmlq.

Another in a series of things that could be a gist.

## requirements

- [htmlq](https://github.com/mgdm/htmlq)
- [pandoc](https://github.com/jgm/pandoc)
- [curl](https://curl.se/)
- [sed](https://www.gnu.org/software/sed/)[^1]

## usage

```
jones [url]  # add [url] to archive ('~/jones' by default)
jones list   # list added files
```

[^1]: the easiest way to get this and other standard linux tools on Windows is to install git
