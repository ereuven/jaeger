import opentracing
import logging
from jaeger_client import Config
from opentracing.ext import tags
from opentracing.propagation import Format
import yaml
import os

def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    with open(os.path.join(os.path.dirname(__file__), 'jaeger.yaml'), 'r') as f:
        config = Config(
            # config={ # usually read from some yaml config
            #     'sampler': {
            #         'type': 'const',
            #         'param': 1,
            #     },
            #     'logging': True,
            #     'reporter_batch_size': 1,
            # },
            config=yaml.load(f),
            service_name=service,
            #validate=True
        )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

# Null tracer
# tracer = opentracing.tracer

# Real tracer
tracer = init_tracer('sample python service')

def say_hello(hello_to):
    with tracer.start_active_span('say-hello') as scope:
        scope.span.set_tag('hello-to', hello_to)
        hello_str = format_string(hello_to)
        print_hello(hello_str)
        scope.span.set_tag('my_tag', 123)
        # d={}
        # tracer.inject(scope.span, Format.HTTP_HEADERS, d)
        # print(d)

def format_string(hello_to):
    with tracer.start_active_span('format') as scope:
        hello_str = 'Hello, %s!' % hello_to
        scope.span.log_kv({'event': 'string-format', 'value': hello_str})
        return hello_str

def print_hello(hello_str):
    with tracer.start_active_span('println') as scope:
        print(hello_str)
        scope.span.log_kv({'event': 'println'})

if __name__ == "__main__":
    say_hello("Alice")
