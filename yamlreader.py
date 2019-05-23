from ruamel.yaml import YAML
from ruamel.yaml.constructor import SafeConstructor
def construct_yaml_map(self, node):
	# test if there are duplicate node keys
	data = []
	yield data
	for key_node, value_node in node.value:
		key = self.construct_object(key_node, deep=True)
		val = self.construct_object(value_node, deep=True)
		data.append((key, val))


SafeConstructor.add_constructor(u'tag:yaml.org,2002:map', construct_yaml_map)
yaml_overwrited = YAML(typ='safe')

def reader(content):
    try:
        parsed = yaml_overwrited.load(content)
        print("syntax is ok")
    except:
        print("yaml syntax error")
    return parsed