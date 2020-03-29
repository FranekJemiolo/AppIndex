import json

import jinja2


WEBSITE_TEMPLATE_PATH = "website_template.html"
APPLICATIONS_PATH = "applications.json"
RENDERED_TEMPLATE_PATH = "index.html"


def load_applications(applications_path):
    with open(applications_path, 'r') as f:
        applications = json.load(f)
        return applications


def load_template(template_path):
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    return template_env.get_template(template_path)


def main():
    html_template = load_template(WEBSITE_TEMPLATE_PATH)
    applications = load_applications(APPLICATIONS_PATH)
    rendered_html = html_template.render(applications=applications)
    with open(RENDERED_TEMPLATE_PATH, 'w') as f:
        f.write(rendered_html)


if __name__ == '__main__':
    main()
