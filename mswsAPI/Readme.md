Uruchamianie temp:
docker build -t mswsapi .
docker run -p 8090:8090 mswsapi

http://localhost:8090/api/generate?seed=1234&size=30