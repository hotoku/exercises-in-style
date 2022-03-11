from jinja2 import Environment

template = Environment().from_string("""{%- for n in range(1, 101) -%}
{%- if n % 15 == 0 %}
FizzBuzz
{%- elif n % 3 == 0 %}
Fizz
{%- elif n % 5 == 0 %}
Buzz
{%- else %}
{{ n }}
{%- endif %}
{%- endfor -%}""")

print(template.render())
