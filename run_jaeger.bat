@echo off

docker run --rm -d --name jaeger ^
  -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 ^
  -p 5775:5775/udp ^
  -p 6831:6831/udp ^
  -p 6832:6832/udp ^
  -p 5778:5778 ^
  -p 16686:16686 ^
  -p 14268:14268 ^
  -p 14250:14250 ^
  -p 9411:9411 ^
  jaegertracing/all-in-one:1.19.2


REM Port	Protocol	Component	Function
REM 5775	UDP	agent	accept zipkin.thrift over compact thrift protocol (deprecated, used by legacy clients only)
REM 6831	UDP	agent	accept jaeger.thrift over compact thrift protocol
REM 6832	UDP	agent	accept jaeger.thrift over binary thrift protocol
REM 5778	HTTP	agent	serve configs
REM 16686	HTTP	query	serve frontend
REM 14268	HTTP	collector	accept jaeger.thrift directly from clients
REM 14250	HTTP	collector	accept model.proto
REM 9411	HTTP	collector	Zipkin compatible endpoint (optional)
