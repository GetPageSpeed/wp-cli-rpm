# wp-cli-rpm

Install the most recent version of WP-CLI on CentOS/RHEL 6+.

## Synopsis

    sudo yum install https://extras.getpagespeed.com/release-latest.rpm
    sudo yum install wp-cli
    cd /path/to/wp
    # rename website URL, no problem:
    wp search-replace https://foo.example.com https://bar.example.com

Install bash completions:

    yum install wp-cli-completion-bash

## Push to repo via CircleCi

[![CircleCI](https://circleci.com/gh/GetPageSpeed/wp-cli-rpm.svg?style=svg)](https://circleci.com/gh/GetPageSpeed/wp-cli-rpm)



