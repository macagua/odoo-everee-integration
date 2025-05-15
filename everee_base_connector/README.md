# Everee Base Connector

[![Beta](https://img.shields.io/badge/maturity-Beta-yellow.png)](https://odoo-community.org/page/development-status)
[![bluebonnet/everee-integration](https://img.shields.io/badge/gitea-bluebonnet%2Feveree--integration-lightgray.png?logo=gitea)](https://dev.gobonum.com/BlueBonnet/everee-integration/tree/18.0/everee_base_connector)

This is a base module that allows you to connect to the Everee API. It
provides a simple interface for making requests to the API and handling
responses. It is designed to be used as a base class for other
connectors that need to interact with the Everee API.

It is built using the requests library and provides methods for making
GET, POST, PUT, and DELETE requests to the API. It also includes methods
for handling authentication and error handling.

## Configuration

To configure this module you have to:

1.  Go to *Settings -\> General -\> Everee API Integration*, there you
    can configure the Everee connection data. You have to set the
    following fields:
    -   \'Enable Everee Integration\': Check this field to enable the
        Everee integration.
    -   \'API Base URL\': The API Base URL for Everee.
    -   \'Company tenant ID\': Your Everee Company tenant ID.
    -   \'API Token\': The API Token generated into Everee.
    -   Save the form.
2.  Click on the \'Test Connection\' button.

## Usage

To use this module, you only need to set up the connection to Everee. To
do so, see the \"Configuration\" section for more information.

## Bug Tracker

Bugs are tracked on
[Gitea Issues](https://dev.gobonum.com/BlueBonnet/everee-integration/issues). In case of
trouble, please check there if your issue has already been reported. If you spotted it
first, help us to smash it by providing a detailed and welcomed
[feedback](https://dev.gobonum.com/BlueBonnet/everee-integration/issues/new?body=module:%20everee_base_connector%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

## Credits

### Authors

- BlueBonnet

### Contributors

- [BlueBonnet](https://bluebonnet.io/):
  - Leonardo J. Caballero G.

### Maintainers

Current maintainer:

[![macagua](https://github.com/macagua.png?size=40px)](https://github.com/macagua)

This module is part of the
[bluebonnet/everee-integration](https://dev.gobonum.com/BlueBonnet/everee-integration/tree/18.0/everee_base_connector)
project on Gitea.

You are welcome to contribute.
