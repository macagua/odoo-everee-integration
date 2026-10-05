This is a base module that allows you to connect to the [Everee API](https://developer.everee.com/docs/introduction). It
provides a simple interface for making requests to the API and handling
responses. It is designed to be used as a base class for other
connectors that need to interact with the [Everee API](https://developer.everee.com/docs/introduction).

It is built using the [requests](https://pypi.org/project/requests/) library and for the moment, only
provides `POST` requests to the API. It also includes methods
for handling authentication and error handling.
