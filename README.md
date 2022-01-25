# SNTC API CONNECTOR

## Description

This project is built using python and http requests, as a test for Cisco SNTC Collection APIs

## Architecture

### clientInfo

This module contains the information required to authenticate the requests to the Cisco SNTC APIs

### genToken

This module generates the authentication token for the collections using HTTP POST request to Cisco SSO Endpoint

### collections-api

This is the main module, imports genToken and clientInfo to make a request to Cisco APIs to upload inventory data

### inventory

This file contains sample inventory data, as is expected from the API. This data is hardcoded, but the idea is that the user can automate the recollection of this data