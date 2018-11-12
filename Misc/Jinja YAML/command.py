from jinja2 import Environment, FileSystemLoader
import yaml

#Load data from YAML
config = yaml.load(open('./BGP_data.yml'))

#Load Jinja2 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('./BGP.jinja2')

print(template.render(config))
