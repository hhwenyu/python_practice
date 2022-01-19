import yaml ## pip3 install pyyaml
import pprint as pp

with open('config.yml') as f:
	parse_yml = yaml.safe_load(f)

pp.pprint(parse_yml['person']['programming_languages'][0]['name'])
