path = 'venv/Lib/site-packages/gradio_client/utils.py'
code = open(path, encoding='utf-8').read()

# Replace the entire problematic function with a safe wrapper
old = 'def _json_schema_to_python_type(schema, defs=None):'
new = '''def _json_schema_to_python_type(schema, defs=None):
    if not isinstance(schema, dict):
        return "any"'''

# Only add if not already patched
if 'if not isinstance(schema, dict):' not in code:
    code = code.replace(old, new, 1)
    open(path, 'w', encoding='utf-8').write(code)
    print('Patched successfully')
else:
    print('Already patched - checking raise line')
    # Also patch the raise line
    old2 = '    raise APIInfoParseError(f"Cannot parse schema {schema}")'
    new2 = '    if not isinstance(schema, dict): return "any"\n    raise APIInfoParseError(f"Cannot parse schema {schema}")'
    if old2 in code:
        code = code.replace(old2, new2)
        open(path, 'w', encoding='utf-8').write(code)
        print('Patched raise line')
    else:
        print('Both already patched')