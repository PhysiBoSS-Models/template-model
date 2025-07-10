import yaml, os
with open('model.yml') as file:
    model = yaml.safe_load(file)

with open('README.md') as file:
    readme_content = file.read()

if 'binary' not in model:
    raise ValueError("Model metadata must contain a 'binary' key.")
else: 
    print(f"Model binary: {model['binary']} : OK")
    
if 'short_name' not in model:
    raise ValueError("Model metadata must contain a 'short_name' key.") 
else:
    print(f"Model short name: {model['short_name']} : OK")
    
if 'version' not in model:
    raise ValueError("Model metadata must contain a 'version' key.")
else:
    print(f"Model version: {model['version']} : OK")
    
if len(readme_content) < 100:
    raise ValueError("README.md must contain at least 100 characters.")
else:
    print(f"README.md content length: {len(readme_content)} characters : OK")

with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'model_binary={model['binary']}', file=fh)
        print(f'model_short_name={model['short_name']}', file=fh)
        print(f'model_version={model['version']}', file=fh)
        
exit(0)
