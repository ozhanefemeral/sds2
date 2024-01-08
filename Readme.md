To start docker image please navigate to solution directory and use this command: "docker build xoshiro:tag" "docker run -p 8080:80 xoshiro:tag".
This will run the application on localhost, port 8080.

API usage:

url: localhost:8080/api/generate
endpoint requires two query parameters:
- seed = seed of the generator
- size = length of generated binary string

Example: 
localhost:8080/api/generate?seed=30&size=50

result body example: (plain text)

"1110001100011010010100001010001000011001101000010001001100110101"

in case of any error e.g wrong input,the API will return no body.