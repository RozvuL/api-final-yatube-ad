import sys
import os

# Добавляем путь к папке с проектом
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'yatube_api'))

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_api.settings')
