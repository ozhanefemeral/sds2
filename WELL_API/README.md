# WELL512a

## Docker
build
```console
$ docker build -t well-api .
```
run
```console
$ docker run -p 2115:8080 well-api
```
Instead of 2115, any available port can be used.

## API
Hosted on http://127.0.0.1:2115/,
API has only one endpoint (localhost:2115/) that accepts only POST requests with json body structured as:
```json
{
    "size": 4,
    "seed": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
}
```
- <b>size</b>: amount of 32bit positive numbers to be generated
- <b>seed</b>: list of 16 32bit positive numbers that should be used for seed, an empty list may also be provided []

Possible returns:
- 200 OK, and JSON with generated values. Example:
    ```
    [
        "2177396355",
        "833904058",
        "414776227",
        "3180089255"
    ]
    ```
- 400 Bad Request, and JSON with missing or invalid parameters. Example:
    ```
    {
        "ERROR": "(!) missing parameter: 'size'"
    }
    ```
- 500 Interial Server Error, and JSON with error message. Example:
    ```
    {
        "ERROR": f"(!) server error occurred: 'some_error_message'"
    }
    ```