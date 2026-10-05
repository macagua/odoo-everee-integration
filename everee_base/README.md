# Everee Base

[![Beta](https://img.shields.io/badge/maturity-Beta-yellow.png)](https://odoo-community.org/page/development-status)
[![macagua/odoo-everee-integration](https://img.shields.io/badge/gitea-macagua%2Fodoo-everee-integration--integration-lightgray.png?logo=gitea)](https://github.com/macagua/odoo-everee-integration/tree/18.0/everee_base)

This is a base module that allows you to connect to the Everee API. It provides a simple
interface for making requests to the API and handling responses. It is designed to be
used as a base class for other connectors that need to interact with the Everee API.

It is built using the `requests` library and for the moment, only provides `POST`
requests to the API. It also includes methods for handling authentication and error
handling.

## Configuration

To configure this module you have to:

1.  Go to _Settings -\> General -\> Developer tools_, click on the
    `Enable developer mode (with assets)` link.

2.  Go to _Settings -\> General -\> Everee API Integration_, there you can configure the
    Everee connection data. You have to set the following fields:

    ![Everee API Integration](https://github.com/macagua/odoo-everee-integration/media/branch/18.0/everee_base/static/description/screenshots/screenshot_step_0.png)

        - \'Enable Everee Integration\': Check this field to enable the Everee integration.
        - \'API Base URL\': The API Base URL for Everee.
        - \'Company tenant ID\': Your Everee Company tenant ID.
        - \'API Token\': The API Token generated into Everee.
        - Save the form.

3.  Click on the \'Test Connection\' button.

- If you are unable to establish the Everee API connection, please check that the Everee
  platform is working correctly on its [Everee status](https://status.everee.com/)
  website.

## Usage

To use this module, you only need to set up the connection to Everee. To do so, see the
\"Configuration\" section for more information.

## Bug Tracker

Bugs are tracked on
[GitHub Issues](https://github.com/macagua/odoo-everee-integration/issues). In case of
trouble, please check there if your issue has already been reported. If you spotted it
first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/macagua/odoo-everee-integration/issues/new?body=module:%20everee_base%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

## Credits

### Authors

- BlueBonnet
- Leonardo J. Caballero G.

### Contributors

- [BlueBonnet](https://bluebonnet.io/).
- [Leonardo J. Caballero G.](https://github.com/macagua/).

### Maintainers

Current maintainer:

[![macagua](https://github.com/macagua.png?size=40px)](https://github.com/macagua)

This module is part of the
[macagua/odoo-everee-integration](https://github.com/macagua/odoo-everee-integration/tree/18.0/everee_base)
project on GitHub.

You are welcome to contribute.
