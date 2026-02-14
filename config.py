"""
Конфигурация бота - адаптировано для работы на телефоне
"""
import os
import logging
from pathlib import Path
from typing import Optional

# Загружаем переменные окружения из .env файла
from dotenv import load_dotenv

# Указываем путь к .env файлу
env_path = Path('.env')
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    print("✅ Файл .env загружен")
else:
    print("⚠️ Файл .env не найден, использую переменные окружения")

class Settings:
    """Класс для хранения всех настроек бота"""
    
    # Telegram настройки
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    
    # Google Gemini API ключ
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # Модель Gemini для генерации изображений (Nano Banana)
    GEMINI_MODEL: str = "gemini-2.5-flash-image-preview"
    
    # Настройки генерации изображений
    DEFAULT_ASPECT_RATIO: str = "1:1"  # 1:1, 16:9, 9:16, 4:3, 3:4
    
    # Настройки логирования
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # ID администратора (опционально)
    ADMIN_IDS: list = [int(id) for id in os.getenv("ADMIN_IDS", "").split(",") if id]
    
    def __init__(self):
        """Проверяем наличие обязательных настроек при создании объекта"""
        self._validate_settings()
        self._setup_logging()
    
    def _validate_settings(self):
        """Проверка наличия обязательных настроек"""
        missing = []
        
        if not self.TELEGRAM_BOT_TOKEN:
            missing.append("TELEGRAM_BOT_TOKEN")
        if not self.GEMINI_API_KEY:
            missing.append("GEMINI_API_KEY")
        
        if missing:
            error_msg = f"❌ Отсутствуют обязательные переменные: {', '.join(missing)}"
            print(error_msg)
            print("📁 Создайте файл .env и добавьте:")
            print("TELEGRAM_BOT_TOKEN=ваш_токен_от_BotFather")
            print("GEMINI_API_KEY=ваш_ключ_от_Google_AI_Studio")
            raise ValueError(error_msg)
        
        print("✅ Все необходимые настройки найдены")
    
    def _setup_logging(self):
        """Настройка логирования"""
        logging.basicConfig(
            level=getattr(logging, self.LOG_LEVEL),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        print(f"✅ Логирование настроено (уровень: {self.LOG_LEVEL})")

# Создаем глобальный объект настроек
settings = Settings()