FROM python:3.6.8-stretch as builder

RUN pip install jinja2

WORKDIR /app

COPY generate_website.py generate_website.py
COPY website_template.html website_template.html
COPY applications.json applications.json
RUN python generate_website.py

FROM nginx:1.17.9 as server

COPY --from=builder /app/img /usr/share/nginx/html/
COPY --from=builder /app/index.html /usr/share/nginx/html/
