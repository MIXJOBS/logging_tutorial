"""
yamlファイルに書き込む設定
web_server:
    host:127.0.0.1
    port:80

db_server:
    host:127.0.0.1
    port:3306
"""
import yaml

# yamlファイルの作成
with open('config.yaml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
        # yamlファイルないの記述をブロックスタイルにするにはdefault_flow_style=Falseに
    }, yaml_file, default_flow_style=False)
