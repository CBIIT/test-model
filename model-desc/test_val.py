from sys import path
path.append('../bento-mdf/validators/mdf-validate')
from MDFValidate.validator import MDFValidator

v = MDFValidator('../bento-mdf/schema/mdf-schema.yaml',
                   'bento_model_file.yaml','bento_model_properties.yaml')

def test():
  v.test_yaml_valid()
  v.test_model_valid()
