# Human Resources Everee API Integration

[![Beta](https://img.shields.io/badge/maturity-Beta-yellow.png)](https://odoo-community.org/page/development-status)
[![Pre-commit Status](https://github.com/macagua/odoo-everee-integration/actions/workflows/pre-commit.yml/badge.svg?branch=18.0)](https://github.com/macagua/odoo-everee-integration/actions/workflows/pre-commit.yml?query=branch%3A18.0)
![Translation Status](https://img.shields.io/badge/macagua/odoo-passing-integration?style=flat&logo=github&label=macagua/odoo-everee-integration&color=green&link=https://github.com/macagua/odoo-everee-integration/tree/18.0/everee_hr)
[![passing](https://img.shields.io/badge/translated-passing-green.png)](https://github.com/macagua/odoo-everee-integration/tree/18.0/everee_hr)

This is a Human Resources module that allows you via Everee API:

- Onboarding for the employees.

It is built using the `requests` library and for the moment, only provides `POST`
requests to the API.

## Configuration

To configure this module you have to:

1.  Install and configurare the _Everee Base_ addon. More information checkout the
    `everee_base` module information.

## Usage

To use this module, you only need to set up the connection to Everee API. To do so, see
the \"Configuration\" section for more information.

1.  If is New Employee
    - Go to Employees app and click on \"Add Employee\" button.
    - Please fill in the following fields:
      - Name.
      - Work Email.
        - Or Private Email (Go to `Private Information` tab -\> `Private Contact`).
      - Work Phone.
        - Or Private Phone (Go to `Private Information` tab -\> `Private Contact`).
      - Private Address (ONLY USA Address) (Go to `Private Information` tab -\>
        `Private Contact`).
      - Currency (Go to `Settings` app -\> `Users and Companies` -\> `Companies`).
    - Save the form.
2.  Or If Existing Employee
    - Go to `Employees` app and click on _Employee_ record.
    - Please fill in the following fields:
      - Name.
      - Work Email.
        - Or Private Email (Go to `Private Information` tab -\> `Private Contact`).
      - Work Phone.
        - Or Private Phone (Go to `Private Information` tab -\> `Private Contact`).
      - Private Address (ONLY USA Address) (Go to `Private Information` tab -\>
        `Private Contact`).
      - Currency (Go to `Settings` app -\> `Users and Companies` -\> `Companies`).
    - Save the form.
3.  Click on the \'Everee Onboarding\' button.
4.  Validate if it was successfully published on your account dashboard on the
    [Everee platform](https://app.everee.com/login).

## Bug Tracker

Bugs are tracked on
[GitHub Issues](https://github.com/macagua/odoo-everee-integration/issues). In case of
trouble, please check there if your issue has already been reported. If you spotted it
first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/macagua/odoo-everee-integration/issues/new?body=module:%20everee_hr%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

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
[macagua/odoo-everee-integration](https://github.com/macagua/odoo-everee-integration/tree/18.0/everee_hr)
project on GitHub.

You are welcome to contribute.
